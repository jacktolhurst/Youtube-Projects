from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def GetVideoID(url:str):
    try:
        parsedUrl = urlparse(url)
        videoID = parse_qs(parsedUrl.query).get("v", [None])[0]

        return videoID
    except:
        return None

def GetDataTranscriptFromID(id:str):
    api = YouTubeTranscriptApi()
    transcript = api.fetch(id)

    return transcript

videoURL = input("Video URL: ")
videoID = GetVideoID(videoURL)
transcriptFullData = GetDataTranscriptFromID(videoID)

for snippet in transcriptFullData:
    print(snippet.text)
