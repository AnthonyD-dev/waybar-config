from pygame import mixer,error,movie
from random import randrange
import commands as com
import cv
import sys

name = "_ritszy_'s MediaPlayer y'all !! "
image = "/home/ritesh/Pictures/acdc.jpg"
prev = ""
mute,paused = False,False
count = 1
st = []

def select_song():
    global name,count,st
    cv.NamedWindow(name,0)
    if sys.argv[1] == '-f' :
	ret = play_file(sys.argv[2])
    elif sys.argv[1] == '-d':
	if count == 1:
	    count += 1
	    st = com.getoutput("ls "+sys.argv[2])
	    st = st.split('\n')
	ret = play_file(sys.argv[2]+st[randrange(0,len(st) ) ] )
	
    if ret == 1 or ret == 0: select_song()
    
	

def play_file(mfile):
    global name,paused,image,mute
    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 2, 2, 0, 3, 8)
    try:
	mixer.music.load(mfile)
    except error:
	print mfile+" Filetype Not Supported"
	return 0
    mixer.music.play()
    img = cv.LoadImage(image)
    while(mixer.music.get_busy() == True):
	cv.PutText(img,mfile, (50,50),font, 255)
	cv.PutText(img,str(mixer.music.get_volume()), (50,150),font, 255)
	cv.ShowImage(name,img)
	c = cv.WaitKey(1)
	if c == 113: 
	    mixer.music.stop()
	    cv.DestroyAllWindows()		
	    sys.exit() 
	elif c == 32:
	    if paused == False : 
		mixer.music.pause()
		paused = True
	    else: 
		mixer.music.unpause()
		paused = False
	elif c == 104: mixer.music.set_volume(mixer.music.get_volume() + 0.05)
	elif c == 108: mixer.music.set_volume(mixer.music.get_volume() - 0.05)
	elif c == 109: 
 		mixer.music.set_volume(mute*0.25)
		mute = not mute
        elif c == 110:
		cv.DestroyAllWindows()
		mixer.music.stop()
		return 1
        elif c == 112:
		#cv.DestroyAllWindows()
		mixer.music.rewind()
		#return 2
    return 0

if __name__ == '__main__':
    mixer.init(44100, -16, 2, 1024)
    mixer.music.set_volume(0.25)
    select_song()
