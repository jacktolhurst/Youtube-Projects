from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from Defaults import *

def GetVideoID(url:str):
    try:
        parsedUrl = urlparse(url)
        videoID = parse_qs(parsedUrl.query).get("v", [None])[0]

        return videoID
    except Exception as err:
        LogError(err)
        return None

def GetDataTranscriptFromID(id:str):
    api = YouTubeTranscriptApi()
    transcript = api.fetch(id)

    return transcript

def TurnDataToText(fullData):
    transcript = ""
    for snippet in fullData:
        transcript += snippet.text
    return transcript

def CreateTXTFile(name:str, text:str):
    try:
        fileLocation = "OutputFiles/Transcriptions/"+name+"-Transcript.txt"
        open(fileLocation, "x")
        with open(fileLocation, "w") as newFile:
            newFile.write(text)
        return newFile
    except Exception as err:
        LogError(err)
        return None

videoURL = input("Video URL: ")
videoID = GetVideoID(videoURL)
transcriptFullData = GetDataTranscriptFromID(videoID)
transcript = TurnDataToText(transcriptFullData)
fileName = input("File Name: ")
file = CreateTXTFile(fileName,transcript)


