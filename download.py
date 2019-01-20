import json
import os
from multiprocessing import Pool
from config import VIDEO_DIR


def log_file(video):
    print(video)
    comand = "ffmpeg -i {url}  \"{dir}/{name}.mp4\""
    name = video[1]
    comandStr = comand.format(url=video[0], name=name, dir=VIDEO_DIR)
    os.system(comandStr)


file = open('./video_list.json', 'r')
data = json.loads(file.read())

p = Pool(processes=os.cpu_count())
p.map(log_file, data)
p.close()
p.join()
