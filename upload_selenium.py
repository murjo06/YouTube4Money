from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import config

def uploadVideo():
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    profile = webdriver.FirefoxProfile("/Users/markmarjanovic/Library/Application Support/Firefox/Profiles/priw3els.default-release")
    profile.set_preference("general.useragent.override", useragent)
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.implicitly_wait(5)
    sleep(5)
    driver.implicitly_wait(5)
    sleep(5)

    driver.get("https://www.youtube.com/upload")
    upload = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    upload.send_keys(f"/Users/markmarjanovic/Desktop/Files/YouTube4Money/{config.OUTPUT_PATH}") #uploads video
    driver.implicitly_wait(5)
    sleep(5)

    title = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')
    driver.execute_script("arguments[0].innerText = 'Fine memes ☕️ #shorts #memes'", title) #add a title

    description = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')
    driver.execute_script("arguments[0].innerText = 'The best memes on the internet :)'", description) #add a description

    driver.implicitly_wait(5)
    sleep(5)
    driver.execute_script("arguments[0].innerText = 'Fine memes ☕️ #shorts #memes'", title) #add a title
    driver.execute_script("arguments[0].innerText = 'The best memes on the internet :)'", description) #add a description

    madeForKids = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]')
    madeForKids.click()

    next = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]')
    next.click()
    next.click()
    next.click()

    public = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]')
    public.click()

    driver.implicitly_wait(20)
    sleep(15)
    publish = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div')
    publish.click()

    sleep(10)
    driver.quit()