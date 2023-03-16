import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import config

TOLERANCE = config.TOLERANCE
MAX_DURATION = config.MAX_DURATION

clips = []
duration = 0
usedClips = []
usedRandoms = []
maxHeight = 0

for file in os.listdir(config.DOWNLOAD_PATH):
    clips.append(VideoFileClip(config.DOWNLOAD_PATH + os.sep + file))
while duration < MAX_DURATION - TOLERANCE:
    rand = random.randint(0, len(clips) -1)
    if clips[rand].duration + duration < MAX_DURATION and not (rand in usedRandoms):
        if maxHeight < clips[rand].h:
            maxHeight = clips[rand].h
        duration += clips[rand].duration
        usedClips.append(clips[rand])
        usedRandoms.append(rand)
    if len(usedRandoms) >= len(clips):
        break
if maxHeight > config.MAX_HEIGHT:
    maxHeight = config.MAX_HEIGHT
finalClips = []
for clip in usedClips:
    width = round(config.ASPECT_RATIO * maxHeight)
    if width % 2 == 1:
        width += 1
    finalClips.append(clip.resize((width, maxHeight)))
finalClip = concatenate_videoclips(finalClips, method="compose")
finalClip.write_videofile(filename=config.OUTPUT_PATH, codec="libx264", audio_codec="aac", audio=True)