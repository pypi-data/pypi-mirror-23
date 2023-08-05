# Project: PyUsbLamp
# Author: onelife

import sys
from time import sleep
from queue import Queue, Empty
from threading import Thread

import usb.core
import usb.backend.libusb1
from usb.core import USBError

if sys.version_info >= (3, ):
   from .applog import AppLog
else:
   from applog import AppLog

DEBUG = 0
STEPS = 32
logger = AppLog().getLogger(__name__)
logger.setLevel(DEBUG and AppLog.DEBUG or AppLog.INFO)


# R+2G+4B -> riso kagaku color index
riso_kagaku_tbl = (
    0, # [0] black 
    2, # [1] red 
    1, # [2] green 
    5, # [3] yellow 
    3, # [4] blue 
    6, # [5] magenta 
    4, # [6] cyan 
    7  # [7] white 
)
RISO_KAGAKU_IX = lambda r, g, b: riso_kagaku_tbl[(r and 1 or 0)+(g and 2 or 0)+(b and 4 or 0)]


class USBLamp(object):
   ENDPOINT       = 0x81
   ID_VENDOR      = 0x1d34
   ID_PRODUCT_OLD = 0x0004
   ID_PRODUCT_NEW = 0x000a
   ID_VENDOR_2    = 0x1294
   ID_PRODUCT_2   = 0x1320
   RGB_MAX        = 0x40
   error          = None

   @staticmethod
   def getSteps(maxValue, steps):
      x = list(range(0, maxValue + 1, max(1, int(maxValue / (steps - 1)))))
      if len(x) >= steps:
         x = x[:steps - 1]
         x.append(maxValue)
      else:
         x.extend([maxValue] * (steps - len(x)))
      return x

   @staticmethod
   def fading(usblamp):
      step = 0
      dir = 1
      idle = True
      while True:
         if usblamp.__class__.error: 
            break
            # raise usblamp.__class__.error
         try:
            delay, newColor = usblamp.task.get(block=idle)
            if delay <= 0: 
               idle = True
               if newColor is not None:
                  usblamp.setColor(newColor)
               continue
            elif usblamp.led_type == 1:
               idle = False
               r = usblamp.getSteps(newColor[0], STEPS)
               g = usblamp.getSteps(newColor[1], STEPS)
               b = usblamp.getSteps(newColor[2], STEPS)
               state = list(zip(r, g, b))
         except Empty:
            pass
         
         sleep(delay)
         if usblamp.led_type == 1:
            # Do fading
            usblamp.setColor(state[step])
            step += dir
            if step == STEPS - 1 or step == 0:
               dir = -dir
         elif usblamp.led_type == 2:
            setColor(newColor)

   def send(self, bytes):
      try:
         if self.led_type == 1:
            logger.debug("send(%d) %02X %02X %02X %02X %02X %02X %02X %02X" % (len(bytes), bytes[0], bytes[1], bytes[2], bytes[3], bytes[4], bytes[5] ,bytes[6], bytes[7]))
            # requesttype = USB_TYPE_CLASS | USB_RECIP_INTERFACE
            # request = USB_REQ_SET_CONFIGURATION
            # value = 0x200
            # index = 0x00
            # timeout = 1000
            ret = self.lamp.ctrl_transfer(0x21, 0x09, 0x200, 0x00, bytes, 1000)
         elif self.led_type == 2:
            logger.debug("send(%d) %02X %02X %02X %02X %02X" % (len(bytes), bytes[0], bytes[1], bytes[2], bytes[3], bytes[4]))
            ret = self.lamp.write(0x02, bytes, 1000)
      except USBError as e:
         self.__class__.error = e
         raise

      if (ret != len(bytes)):
         logger.error("Get %d VS. send %d" % (ret, len(bytes)))
   
   def __init__(self):
      if sys.platform != 'win32':
         raise NotImplementedError('Currently, only MS Windows is supported!')
         
      from os import path
      import re
      backend = usb.backend.libusb1.get_backend(find_library=lambda x: path.join(
         path.dirname(__file__),
         'libusb', 
         'MS' + re.search('(\d+) bit', sys.version).groups()[0], 
         'dll', 'libusb-1.0.dll'))
      
      self.led_type = -1
      self.lamp  = None
      self.color = (0, 0, 0)
      self.task = Queue()
      
      # get device
      while True:
         devs = list(usb.core.find(idVendor=self.ID_VENDOR, idProduct=self.ID_PRODUCT_NEW, find_all=True,backend=backend))
         if devs:
            self.led_type = 1
            logger.info("idVendor %d, idProduct %d" % (self.ID_VENDOR, self.ID_PRODUCT_NEW))
            break
         devs = list(usb.core.find(idVendor=self.ID_VENDOR, idProduct=self.ID_PRODUCT_OLD, find_all=True,backend=backend))
         if devs:
            self.led_type = 1
            logger.info("idVendor %d, idProduct %d" % (self.ID_VENDOR, self.ID_PRODUCT_OLD))
            break
         devs = list(usb.core.find(idVendor=self.ID_VENDOR_2, idProduct=self.ID_PRODUCT_2, find_all=True,backend=backend))
         if devs:
            self.led_type = 2
            logger.info("idVendor %d, idProduct %d" % (self.ID_VENDOR_2, self.ID_PRODUCT_2))
         break
      logger.info("LED Type is %d" % (self.led_type))
      
      if not devs:
         raise SystemError('No device found!')
      self.lamp = devs[0]

      # send init cmd
      if self.led_type == 1:
         self.send((0x1f, 0x02, 0x00, 0x2e, 0x00, 0x00, 0x2b, 0x03))
         self.send((0x00, 0x02, 0x00, 0x2e, 0x00, 0x00, 0x2b, 0x04))
         self.send((0x00, 0x02, 0x00, 0x2e, 0x00, 0x00, 0x2b, 0x05))
         
      # create thread for fading
      self.t = Thread(target=self.fading, args=(self, ))
      self.t.daemon = True
      self.t.start()
            
   def getColor(self):
      return self.color
      
   def setColor(self, newColor):
      self.color = newColor
      logger.debug("Set color %s" % str(self.color))

      if self.led_type == 1:
         self.send(self.color + (0x00, 0x00, 0x00, 0x00, 0x05))
      elif self.led_type == 2:
         self.send(RISO_KAGAKU_IX(*color) + (0x00, 0x00, 0x00, 0x00))
         
   def setFading(self, delay, newColor):
      self.color = newColor
      logger.debug("Set fading %f,%s" % (delay, str(self.color)))
      self.task.put((delay, newColor))

   def switchOff(self):
      self.setColor((0,0,0))
      
   def exit(self):
      self.__class__.error = SystemExit('USBLamp exit.')
      self.setFading(0, (0, 0, 0))
      self.t.join()
      logger.debug("*** Fading thread exited.")
