import time
import io
import threading

import cv2

class OpencvCamera(object):
    def __init__(self):
        self.camera = cv2.VideoCapture(0) 
        if not self.camera.isOpened():
            raise RuntimeError('Could not start camera!')
    
    def __del__(self):
        self.camera.release()
    
    def get_frame(self):
        success, img = self.camera.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()

