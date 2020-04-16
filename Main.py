from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from pytube import YouTube
import sys


# Variables
run = False
urls = []

# get list of urls from user
def case_1():
    global run
    global urls
    session = PromptSession()
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
    pass

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
    while True:
        switch()

if __name__ == '__main__':
    main()