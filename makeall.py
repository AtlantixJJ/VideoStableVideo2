import os

os.system("mkdir data")
os.system("mkdir data/video_frames1int")
os.system("mkdir data/video_frames2int")
os.system("mkdir data/video_none")

# copy none
# os.system("cp ../VideoStableVideo/data/video_none/*.mp4 data/video_none/")

# copy avi frames1
os.system("cp ~/StyleBank/download/*vsfn* data/video_frames1int/")
os.system("cp ../avi2mp4.py  data/video_frames1int/")
os.system("cd  data/video_frames1int/ && python avi2mp4.py && rm *.avi") 

# copy avi frames2

