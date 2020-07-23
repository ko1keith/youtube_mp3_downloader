from pytube import YouTube
import sys
import os

class Download():

    def __init__(self):
        self.directory = os.getcwd() + "output_folder"

    def download_url(self, url):
        yt = YouTube(url)
        file_name = yt.streams[0].default_filename.replace(" ", "_").replace("(","[").replace(")","]")
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(self.directory, file_name)

        # Iterate through directory and delete files ending with .mp4
        for filename in os.listdir(self.directory):
            outputDir = self.directory + filename
            str = "ffmpeg -i " + outputDir + " -f mp3 -ab 192000 -vn " + outputDir.strip(".mp4") + ".mp3"
            if (filename.endswith(".mp4")):  # or .avi, .mpeg, whatever.
                os.system(str)
                os.remove(outputDir) # remove mp4 file
            else:
                continue
    
    # If there are old files in the output folder, delete them
    def empty_folder(self):
        for filename in os.listdir(self.directory):
            file = self.directory + filename
            os.remove(file)
