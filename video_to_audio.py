# import package 
#  to install run - pip install moviepy
import moviepy.editor

# select the video file
video = moviepy.editor.VideoFileClip('video.mov')
# convert it into audio
audio = video.audio
# saving the audio file
audio.write_audiofile('extractedvidop.mp3')
