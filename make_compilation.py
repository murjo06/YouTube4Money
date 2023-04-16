import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, ImageClip, VideoClip
import random
import config

TOLERANCE = config.TOLERANCE
MAX_DURATION = config.MAX_DURATION

def makeCompilation():
    clips = []
    duration = 0
    usedClips = []
    usedRandoms = []
    maxHeight = 0
    for file in os.listdir(config.DOWNLOAD_PATH):
        clips.append(VideoFileClip(config.DOWNLOAD_PATH + os.sep + file))
    while duration < MAX_DURATION - TOLERANCE:
        rand = random.randint(0, len(clips) - 1)
        if clips[rand].duration + duration < MAX_DURATION and not (rand in usedRandoms) and (clips[rand].w / clips[rand].h >= config.ASPECT_RATIO_LIMIT):
            if maxHeight < clips[rand].h:
                maxHeight = clips[rand].h
            duration += clips[rand].duration
            usedClips.append(clips[rand])
            usedRandoms.append(rand)
        if len(usedRandoms) >= len(clips):
            break
    if maxHeight > config.MAX_HEIGHT:
        maxHeight = config.MAX_HEIGHT
    actualClips = []
    finalClips = []
    for clip in usedClips:
        ratio = clip.w / clip.h
        if ratio >= 1:
            actualClips.append(clip.resize(width = config.ASPECT_RATIO * config.MAX_HEIGHT))
        else:
            actualClips.append(clip.resize(height = config.MAX_HEIGHT))
    finalClip = concatenate_videoclips(actualClips, method = "compose")
    background = ImageClip("background.png")
    writeClip = CompositeVideoClip([background, finalClip.set_position("center")])
    writeClip = writeClip.set_start(0).set_duration(finalClip.duration)
    writeClip.write_videofile(filename = config.OUTPUT_PATH, codec = "libx264", audio_codec = "aac", audio = True, remove_temp = True, threads = 8)
    return config.OUTPUT_PATH

if __name__ == "__main__":
    makeCompilation()