import os
def multipleVideo(output,inputs):

    name = str(input("Enter desired name of multiple video:\n"))
    filename = output/"{}.mkv".format(name)
    command = f'ffmpeg -i {output/inputs[0][1]} -i {output/inputs[1][1]} -i {output/inputs[2][1]} -i {output/inputs[3][1]} -filter_complex " \
        [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
        [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
        [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; \
        [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; \
        [a0][a1][a2][a3]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[out]" -map "[out]" -c:v libx264 -t 30 -f matroska {filename}'
    os.system(command)
    os.system(f"ffplay {filename}")