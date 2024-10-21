from picamera2 import Picamera2
import time
pc2=Picamera2()
pc2.configure(pc2.create_preview_configuration(main={"size":(1920, 1080)}))
pc2.start_preview(True, width = 300, height =200)
pc2.start()
time.sleep(1)
pc2.capture_file("./test_image.jpg")
pc2.close()
