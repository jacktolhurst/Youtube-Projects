from pytubefix import YouTube

def DownloadVideo(url:str):
    YouTube(url).streams.first().download()
    video = YouTube(url)
    videoStream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if videoStream:
        videoStream.download("OutputFiles/Videos")

videoURL = input("Video URL: ")
DownloadVideo(videoURL)