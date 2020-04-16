from prompt_toolkit import PromptSession

from pytube import YouTube
import ffmpy
import sys
import os


# Variables
run = False
urls = []
session = PromptSession()

# get list of urls from user
def case_1():
    global run
    global urls

    strPrompt = "Enter URL/'run' >>> "

    strInput = session.prompt(strPrompt)

    if(strInput == "run"):
        run = True
    elif(strInput == "exit"):
        sys.exit(1)
    else:
        urls.append(strInput)




# perform download and output to output folder
def case_2():
    global run
    global urls
    directory = os.getcwd() + "/output_folder/"
    # Iterate through urls List
    for url in urls:
        # Create Youtube obj with specified URL
        yt = YouTube(url)
        fileName = yt.title.replace(" ", "_")

        stream = yt.streams.filter(only_audio=True).first()
        stream.download(directory, fileName)

        print(fileName + " outputted to output_folder.")

    for filename in os.listdir(directory):
        outputDir = directory + filename
        str = "ffmpeg -i " + outputDir + " -f mp3 -ab 192000 -vn " + outputDir.strip(".mp4") + ".mp3"
        print(str)
        if (filename.endswith(".mp4")):  # or .avi, .mpeg, whatever.
            os.system(str)
            os.remove(outputDir) # remove mp4 file
        else:
            continue


    strPrompt = "Download more(yes/no)? >>>"
    strInput = session.prompt(strPrompt)

    if(strInput == "yes"):
        run = False
        urls = []
    elif(strInput == "no"):
        print("Goodbye")
        sys.exit(1)





#
def switch():
    global run

    if (run == False):
        return switcher.get(1)()
    elif(run == True):
        return switcher.get(2)()


switcher = {
    1: case_1,
    2: case_2
}

def main():
    # os.system('cls')

    while True:
        switch()

if __name__ == '__main__':
    main()