import os
from datetime import datetime

def capture_image():
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
    os.system(f'fswebcam -r 1280x720 --no-banner {filename}')
    print(f"Captured image: {filename}")
    return filename
