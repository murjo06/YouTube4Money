from datetime import timedelta, date, datetime
import instaloader
import config
import os

USERNAME = config.USERNAME
PROFILES = config.PROFILES
PATH = config.DOWNLOAD_PATH

def scrapeVideos(username, days = 1):
    dateLocal = date.today() - timedelta(days = days)
    print("Starting Scraping")
    instaLoader = instaloader.Instaloader()
    instaLoader.load_session_from_file(username)
    instaLoader.download_comments = False
    instaLoader.save_metadata = False
    instaLoader.download_geotags = False
    instaLoader.download_pictures = False
    instaLoader.metadata_string = False
    for profile in PROFILES:
        for post in instaloader.Profile.from_username(instaLoader.context, profile).get_posts():
            if post.date_local >= datetime(dateLocal.year, dateLocal.month, dateLocal.day):
                instaLoader.download_post(post, PATH)
            else:
                break
    for file in os.listdir(PATH):
        if file.endswith(".txt"):
            os.remove(PATH + os.sep + file)
    i = 0
    for file in os.listdir(PATH):
        os.rename(PATH + os.sep + file, f"{PATH + os.sep + str(i)}.mp4")
        i += 1

if __name__ == "__main__":
    scrapeVideos(username = USERNAME)