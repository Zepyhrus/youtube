from moviepy.editor import AudioFileClip
import hashlib
from glob import glob




if __name__ == "__main__":
  for video_name in glob('*.flv'):
    clip = AudioFileClip(video_name)

    md5 = hashlib.md5(video_name.encode('utf-8')).hexdigest()

    clip.write_audiofile(f'audios/{md5}.wav')


