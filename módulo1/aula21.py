import pydub
from pydub.playback import play

audio = pydub.AudioSegment.from_mp3('audio.mp3')

play(audio)