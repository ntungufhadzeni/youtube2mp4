#! python
from pytube import YouTube
import sys
import os

PATH = os.path.join(os.path.expanduser('~'), 'Downloads/Youtube')

def main():
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    os.chdir(PATH)

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print('Usage: youtube2mp4 [url]')
        sys.exit()

    print('Downloading...')
    YouTube(url).streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download()
    print(f'Video saved in {PATH}')