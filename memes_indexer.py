import os
import config

def indexMemes():
    files = os.listdir(config.DOWNLOAD_PATH)
    index = 0
    for file in files:
        if(not file.endswith(".mp4")):
            os.remove(f"{config.DOWNLOAD_PATH}{os.sep}{file}")
            continue
        os.rename(f"{config.DOWNLOAD_PATH}{os.sep}{file}", f"{config.DOWNLOAD_PATH}{os.sep}{index}.mp4")
        index += 1

if __name__ == "__main__":
    indexMemes()