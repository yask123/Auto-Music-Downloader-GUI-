from Tkinter import *
import math
import os
import glob

import urllib2

root = Tk()     
top = Frame(root)
top.pack(side='top') 

hwframe = Frame(top)
hwframe.pack(side='top')
font = 'times 18 bold'
hwtext = Label(hwframe, text='Yasks Music Downloader ! V:1.0 (aplpha) ', font=font)
hwtext.pack(side='top', pady=20)

rframe = Frame(top)
rframe.pack(side='top', padx=1, pady=20)

r_label = Label(rframe, text='I want to download song ')
r_label.pack(side='left')

r_entry = Entry(rframe, width=30)
r_entry.pack(side='left')
r_entry.insert('end', 'Taylor Swift Song ')

def comp_s(event=None):
    #s = (r_entry.get())
  
    #s_label.configure(text='%s' % s)

    search = r_entry.get()

    search = r_entry.get()
    search = search.replace(' ','%20')
    s_label.configure(text='Making a Query Request! ')


   
    response = urllib2.urlopen('https://www.youtube.com/results?search_query='+search)
    html = response.read()
    a =html.find('<h3 class="yt-lockup-title"><a href="/watch?')
    raw_link= (html[a+43:a+57]) # May change when Youtube Website may get updated in the future.
    proper_linl = 'https://www.youtube.com/watch'+raw_link

	#youtube-dl --extract-audio --audio-format mp3
	#command='youtube-dl -t --format bestaudio '+proper_linl
    command = 'youtube-dl --extract-audio --audio-format mp3 '+proper_linl
    s_label.configure(text='Processed Querying , Starting Phase 2')
    v.set("Downloaded !! Enjoy!")

    os.system(command)
	



r_entry.bind('<Return>', comp_s)

compute = Button(rframe, text=' NOW! ', command=comp_s, relief='flat' , background='green')
compute.pack(side='left')

s_label = Label(rframe, width=30)
s_label.pack(side='left')

def quit(event=None):
    root.destroy()
quit_button = Button(top, text='Exit the App', command=quit,
                     background='red', foreground='blue')
quit_button.pack(side='top', pady=5, fill='x')
root.bind('<q>', quit)

root.mainloop()
