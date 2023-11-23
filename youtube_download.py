#import pytube
from pytube import YouTube

url = str(input("Enter the URL to be downloaded"))
#pytube.YouTube(url).streams.get_highest_resolution()
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(url) 
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 
  
#to set the name of the file
yt.set_filename('GeeksforGeeks Video')  
  
# get the video with the extension and
# resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 
