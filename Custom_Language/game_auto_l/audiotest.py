import aubio
import numpy as np
import pyaudio

import time
import argparse

import queue

import music21  # yes! new favorite library


# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, input=True,
                frames_per_buffer=4096)
time.sleep(1)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

q = queue.Queue()
print("pDetectionpDetection",pDetection)

def get_current_note(volume_thresh=0.01, printOut=False):
    """Returns the Note Currently Played on the q object when audio is present
    
    Keyword arguments:

    volume_thresh -- the volume threshold for input. defaults to 0.01
    printOut -- whether or not to print to the terminal. defaults to False
    """
    current_pitch = music21.pitch.Pitch()
    print("current_pitch",current_pitch)

    bot_message = ""
    message=""
    while bot_message != "Bye" or bot_message!='thanks':

        data = stream.read(1024, exception_on_overflow=False)
        #print("#########",type(data))
        samples = np.fromstring(data,
                                dtype=aubio.float_type)
        #print("samples",samples)
        pitch = pDetection(samples)

        # Compute the energy (volume) of the
        # current frame.

        volume = np.sum(samples**2)/len(samples) * 100
        print("Volume",volume)
        print("pitch",pitch)
        if pitch and volume > volume_thresh:  # adjust with your mic!
            current_pitch.frequency = pitch
        else:
            continue

        if printOut:
            print(current_pitch)
        
        else:
            current = current_pitch.nameWithOctave
            q.put({'Note': current, 'Cents': current_pitch.microtone.cents})

if __name__ == '__main__':
    get_current_note(volume_thresh=0.001, printOut=True)