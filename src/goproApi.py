#!/usr/bin/python

# goproApi.py
# Nacho Carnicero <ignacio.carnicero@sterblue.com>
# February 2017
from goprohero import GoProHero
import time
import logging
import asyncio

class GoproApi(GoProHero):

    def __init__(self,ip='10.5.5.9', password='password', log_level=logging.ERROR) :
        GoProHero.__init__(self,ip=ip, password=password, log_level=log_level)


    def getStatus(self):
        "Gets the camera status"
        try:
            status = self.status()
            while status['summary']=='notfound':
                status = self.status()
            return status
        except Exception as e:
            logging.error("Error getting the Gopro status with error %s"%e)
        return False


    async def takePicture(self):
        "Takes a picture with the camera, ensuring that the photo has been taken"
        logging.info("Taking a picture with the Gopro")
        try:
            currentNumberOfPictures = self.getStatus()['npics']
            self.command('record', 'on')
            while (self.getStatus()['npics']==currentNumberOfPictures):
                await asyncio.sleep(0.3)
                self.command('record', 'on')
            return True
        except Exception as e:
            logging.error("Error taking a picture with the Gopro with error %s"%e)
        return False


    def powerOn(self):
        "Powers on the camera"
        logging.info("Powering on the Gopro")
        try:
            while (self.getStatus()['power']!='on'):
                time.sleep(0.3)
                self.command('power', 'on')
            # Check if parameters have been populated to status message and thus the camera is initialized
            #(here it supposes that once the 'mode' parameter has been populated all parameters have been populated as well)
            while ('mode' not in self.getStatus()):
                time.sleep(0.3)
            return True
        except Exception as e:
            logging.error("Error powering on the Gopro with error %s"%e)
        return False


    def changeMode(self,mode='still'):
        """
        Changes the mode of the camera, possible modes are:
        - still
        - video
        - burst
        - timelapse
        - timer
        - hdmi
        """
        logging.info("Setting the Gopro mode to %s"%mode)
        try:
            while (self.getStatus()['mode']!=mode):
                time.sleep(0.3)
                self.command('mode', mode)
            return True
        except Exception as e:
            logging.error("Error changing the Gopro mode with error %s"%e)
        return False

    def powerOff(self):
        "Powers off the camera"
        logging.info("Powering off the Gopro")
        try:
            while (self.getStatus()['power']!='sleeping'):
                time.sleep(0.3)
                self.command('power', 'sleep')
            return True
        except Exception as e:
            logging.error("Error powering off the Gopro with error %s"%e)
        return False
