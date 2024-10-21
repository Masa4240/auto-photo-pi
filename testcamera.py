from picamera2 import Picamera2
import time
from datetime import datetime
import pytz

# 日本標準時（JST）のタイムゾーンを設定
japan_tz = pytz.timezone('Asia/Tokyo')

# 現在の日本時間を取得
japan_time = datetime.now(japan_tz).strftime("%Y%m%d_%H%M%S")

# フォーマットして文字列として表示
# japan_time_str = japan_time.strftime('%Y-%m-%d %H:%M:%S')
print(japan_time)

pc2=Picamera2()
pc2.configure(pc2.create_preview_configuration(main={"size":(1920, 1080)}))
pc2.start_preview(True, width = 300, height =200)
pc2.start()
time.sleep(1)
pc2.capture_file("./" + japan_time + ".jpg")
pc2.close()
