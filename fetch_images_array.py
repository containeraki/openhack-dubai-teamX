import os
from IPython.display import display, Image, SVG, Math, YouTubeVideo
rootdir = '/data/home/openhack/notebooks/gear_images'


#for subdir, dirs, files in os.walk(rootdir):
for ddir in os.listdir(rootdir):
    folder = rootdir+'/'+ddir
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            filename=os.path.join(folder, filename)
            i = Image(filename,width=100, height=100)
            print("Class - ",ddir)
            display(i)
            break
