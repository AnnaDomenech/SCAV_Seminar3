import os
import S3

def displayVideo(dir):
    x = str(input("Do you want to display the video?[y/n]"))
    if 'y'==x:
        command=f'ffplay {dir}'
        os.system(command)
    else:
        pass

def transcode(output,input):
    name,_=S3.check_ext_name(input)

    AVI_output = output / '{}_avi.avi'.format(name)
    command = f"ffmpeg -i {input} -c:v copy -c:a copy {AVI_output}"
    os.system(command)
    #displayVideo(AVI_output)

    VP9_output = output / '{}_vp9.mp4'.format(name)
    command = f'ffmpeg -i {input} -c:v libvpx-vp9  {VP9_output}'
    os.system(command)
    #displayVideo(VP9_output)

    VP8_output = output / '{}_vp8.mkv'.format(name)
    command =  f"ffmpeg -i {input} -c:v libvpx -qmin 0 -qmax 50 -crf 5 -b:v 1M -c:a libvorbis {VP8_output}"
    os.system(command)
    #displayVideo(VP8_output)

    H265_output = output / '{}_h265.mp4'.format(name)
    command = f'ffmpeg -i {input} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k {H265_output}'
    os.system(command)
    #displayVideo(H265_output)

 