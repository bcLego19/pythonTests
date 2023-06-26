from pytube import YouTube
import os

def DownloadVideo(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        print("Starting download of ["+ytObject.title+"]")
        ytObject.download()
    except:
        print("An error has occurred")
    print("Download has completed successfully")

#link = 'https://www.youtube.com/watch?v=cjMAaEzS9Ys'
#DownloadVideo(link)

def DownloadVideoToLocation(link, filepath):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        print("Starting download of ["+ytObject.title+"]")
        ytObject.download(filepath)
    except:
        print("An error has occurred")
    print("Download has completed successfully")

def doesDirExist(path):
    if (os.path.exists(path) == False or os.path.isfile(path) == True): return False
    else: return True

def DownloadProgram():
    link = input("Enter the YouTube video URL: ")
    hasLocation = input("By defalut, the video will save to the current directory. Do you have a location you want to save to? (y/n) ")
    
    if(hasLocation != "y"):
        DownloadVideo(link)
    else: 
        filepathName = input("Enter a file location: ")
        pathExist = doesDirExist(filepathName)
        if(pathExist == False):
            DownloadVideo(link)
        else:
            DownloadVideoToLocation(link, filepathName)

DownloadProgram()