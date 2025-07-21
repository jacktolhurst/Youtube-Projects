from pytubefix import YouTube
from Defaults import *

def DownloadVideo(url:str):
    try:
        YouTube(url).streams.first().download()
        video = YouTube(url)
        videoStream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if videoStream:
            videoStream.download("OutputFiles/Videos")
    except Exception as err:
        LogError(err)

videoURL = input("Video URL: ")
DownloadVideo(videoURL)