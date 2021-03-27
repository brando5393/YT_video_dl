import re
from pytube import YouTube as yt
class Downloader:
  def download_video(self,url):
    try:
      if url != None or "":
        yt(url).streams.get_highest_resolution().download("./downloads")
        print(f"Starting your download of {yt(url).title}")
      else:
        print(f"Sorry but your request to download the video {yt(url).title} could not be completed at this time. Please try again later, thank you.")
    except:
      pass