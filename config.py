USERNAME = "naoh.enjoyer"
PROFILES = ["daquan", "sarcasm_only", "funny_videos"]
DOWNLOAD_PATH = "downloaded_memes"
TOLERANCE = 25
MAX_DURATION = 45
MAX_HEIGHT = 1920
ASPECT_RATIO = 9 / 16

def inList(element, list: list):
    for i in list:
        if i == element:
            return True
    return False