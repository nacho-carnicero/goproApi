from goproApi import goproApi
import logging
import binascii


camera = goproApi.GoproApi(password='sterblue', log_level=logging.ERROR)

camera.powerOn()
camera.takePicture()
camera.changeMode('video')
camera.powerOff()
