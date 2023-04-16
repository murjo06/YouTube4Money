import scrape_instagram
import scrape_reddit
import make_compilation
import upload_selenium
import memes_indexer
import time
import config
from colorama import Fore
import sys
import os

TIME_BETWEEN_SCRAPES = 0.5 * 24 * 60 * 60
TIME_BETWEEN_UPLOADS = 0.5 * 24 * 60 * 60

def main():
    while True:
        memes_indexer.deleteMemes()
        if config.USE_INSTAGRAM:
            print(Fore.GREEN + "Scraping Instagram" + Fore.RESET)
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            scrape_instagram.scrapeInstagram(username = config.USERNAME)
            sys.stdout = old_stdout
        if config.USE_REDDIT:
            print(Fore.GREEN + "Scraping Reddit" + Fore.RESET)
            old = sys.stdout
            sys.stdout = open(os.devnull, "w")
            scrape_reddit.scrapeReddit()
            sys.stdout = old
        for i in range(round(TIME_BETWEEN_SCRAPES / TIME_BETWEEN_UPLOADS)):
            print(Fore.GREEN + "Making compilation" + Fore.RESET)
            boomer = sys.stdout
            sys.stdout = open(os.devnull, "w")
            make_compilation.makeCompilation()
            sys.stdout = boomer
            print(Fore.GREEN + "Uploading" + Fore.RESET)
            upload_selenium.uploadVideo()
            print(Fore.GREEN + "Video sucessfully uploaded" + Fore.RESET)
            print("")
            time.sleep(TIME_BETWEEN_UPLOADS)

if __name__ == "__main__":
    main()