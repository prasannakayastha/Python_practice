#This program will download the youtube video from www.youtube.com
from pytube import YouTube

try:    
    user_input= input("Enter the URL of the YouTube video: ")
    yt=YouTube(user_input)
    #stream=yt.streams.get_highest_resolution()
    print("Title: ", yt.title)
    print("Views: ", yt.views) 
    yt.download()
    print("Video downloaded successfully!")

except Exception as e:
    print("An error occurred:", e)  
    
    