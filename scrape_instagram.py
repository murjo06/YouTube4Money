from datetime import timedelta, date, datetime
import instaloader
import config
import os
import memes_indexer

USERNAME = config.USERNAME
PROFILES = config.PROFILES
PATH = config.DOWNLOAD_PATH

def scrapeInstagram(username, days = 1):
    for file in os.listdir(PATH):
        os.remove(PATH + os.sep + file)
    dateLocal = date.today() - timedelta(days = days)
    print("Starting Scraping")
    instaLoader = instaloader.Instaloader()
    instaLoader.load_session_from_file(username)
    instaLoader.download_comments = False
    instaLoader.save_metadata = False
    instaLoader.download_geotags = False
    instaLoader.download_pictures = False
    instaLoader.metadata_string = False
    posts = []
    for profile in PROFILES:
        for post in instaloader.Profile.from_username(instaLoader.context, profile).get_posts():
            if post.date_utc >= datetime(dateLocal.year, dateLocal.month, dateLocal.day):
                posts.append(f"{post.caption} @ {post.url}")
                instaLoader.download_post(post, PATH)
            else:
                break
    memes_indexer.indexMemes()
    return posts

if __name__ == "__main__":
    scrapeInstagram(username = USERNAME)