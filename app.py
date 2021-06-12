#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
from camera import OpencvCamera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__) #先是匯入了 Flask 相關的套件，並使用 "app" 這個變數賦予 Flask 這個物件。


@app.route('/') 
def index(): 
    """Video streaming home page."""
    return render_template('index.html') #網頁


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#Video
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(OpencvCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='140.124.13.11',port=22)