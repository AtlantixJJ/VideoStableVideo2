import os
import glob

avilist=glob.glob('*.avi')
avilist.sort()

for avifile in avilist:
    mp4file=avifile[:-3] + 'mp4'
    # os.system('ffmpeg -y -i %s -pix_fmt yuv420p %s'%(avifile,mp4file))
    os.system('ffmpeg -i {} -vcodec libx264 -vf "scale=trunc(iw/4)*2:trunc(ih/4)*2"  {}'.format(avifile, mp4file))
    #os.system("rm " + avifile)
