import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    while(True):
        a = input('photo: 1, video: 2, exit: 9 > ')
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if a=='1':
            print('사진 촬영')
            time.sleep(2)
            camera.capture('%s/%s photo.jpg' % (path,now_str))
        elif a=='2':
            print('동영상 촬영')
            camera.start_recording('%s/%s video.h264' % (path,now_str))
            input('press enter to stop')
            camera.stop_recording()
        elif a=='9':
            break
        else: print('wrong comment')
finally:
    camera.stop_preview()
