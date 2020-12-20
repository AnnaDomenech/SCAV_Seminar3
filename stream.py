import os

def stream(input):
    command = f'ffmpeg -re -i {input}  -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000'
    os.system(command)
    