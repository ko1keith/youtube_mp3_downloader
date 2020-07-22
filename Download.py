from pytube import YouTube
import sys
import os

class Download():

    def __init__(self):
        pass

    def download_url(self, url):
        directory = os.getcwd() + "/output_folder/"

        yt = YouTube(url)
        file_name = yt.streams[0].default_filename.replace(" ", "_").replace("(","[").replace(")","]")
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(directory, file_name)

        for filename in os.listdir(directory):
            outputDir = directory + filename
            str = "ffmpeg -i " + outputDir + " -f mp3 -ab 192000 -vn " + outputDir.strip(".mp4") + ".mp3"
            print(str)
            if (filename.endswith(".mp4")):  # or .avi, .mpeg, whatever.
                os.system(str)
                os.remove(outputDir) # remove mp4 file
            else:
                continue
