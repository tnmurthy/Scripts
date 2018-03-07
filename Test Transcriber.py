#Step 1 - Import library

import cmu_sphinx4
#Step 2 - read audio file
audio_URL = 'https://freewavesamples.com/files/Bass-Drum-1.wav'
transcriber = cmu_sphnix4.transcriber(audio_URL)
#Step 3 - Print it out
for line in transcriber.transcrip_stream():
	print (line)

