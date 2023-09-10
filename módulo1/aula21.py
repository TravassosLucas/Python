import pydub
from pydub.playback import play

audio = pydub.AudioSegment.from_mp3("Aula-Python/módulo1/We Are.mp3")

play(audio)