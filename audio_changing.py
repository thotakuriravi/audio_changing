import os
from moviepy.editor import VideoFileClip, AudioFileClip
paths = [ 'parent_path_name\\intro\\', 'parent_path_name\\outro\\' ]
audio_path = 'parent_path_name\\intro_audios\\'

for path in paths:
    i = 1
    for file in os.listdir(path):
        for audio in os.listdir(audio_path):
            # Load the video and audio files
            video = VideoFileClip(path + file )
            audio = AudioFileClip(audio_path + audio)

            # Set the duration of the audio clip to match the duration of the video clip
            audio = audio.set_duration(video.duration)

            # Combine the video and audio clips
            final_clip = video.set_audio(audio)
            
            file_name = path + f'new\\happy_and_healthy_intro_{i}.mp4'

            # Export the final clip
            final_clip.write_videofile(file_name)
            i = i + 1
            video.close()
