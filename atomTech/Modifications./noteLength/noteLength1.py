# PURPOSE: To fix the issue with note length being the same regardless of the audio input's data
# ----------------------------------------------------------------------------------
# Import libraries. 
from __future__ import print_function
import pyaudio
import sys
import numpy as np
import aubio
import time
import random
import mido
from mido import Message
from time import sleep
import struct

# initialise pyaudio
p = pyaudio.PyAudio()

# ----------------------------------------------------------------------------------
# Set stream parameters (PyAudio).
buffer_size = 512
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
# ----------------------------------------------------------------------------------
# Let user choose MIDI Port
if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    portname = None  # Use default port
# ----------------------------------------------------------------------------------
# set audio analysis variables and definitions.
tolerance = 1.
win_s = 4096 # fft size
hop_s = buffer_size # hop size
# initializes pitch_o to pitch detection function.
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
# initializes onset to onset detection function.
onset = aubio.onset("default", win_s, hop_s, samplerate)
# Converts frequencies to MIDI numbers.
pitch_o.set_unit("midi") 
# Sets sensitivity of pitch detection.
pitch_o.set_tolerance(tolerance)
pitch = 0
isNoteOn = False
currentNote = 0
# MIDI initialization
port = mido.open_output(portname, autoreset=True)
# ----------------------------------------------------------------------------------
# RMS: AMPLITUDE TRACKING ALGORITHM ATTEMPT
# # may be take out divided by 2?
# def rms( data ):
#     count = len(data)/2
#     format = "%dh"%(count)
#     shorts = struct.unpack( format, data )
#     sum_squares = 0.0
#     for sample in shorts:
#         n = sample * (1.0/32768)
#         sum_squares += n*n
#     return math.sqrt( sum_squares / count )

# ----------------------------------------------------------------------------------
# define callback function to processing/analysis within this function definition. 
def callback(in_data, frame_count, time_info, flag):

    global pitch, isNoteOn, currentNote, port

    audio_data = np.fromstring(in_data, dtype=np.float32)
    signal = np.frombuffer(audio_data, dtype=np.float32)
            
    pitch = pitch_o(signal)[0]
    confidence = pitch_o.get_confidence()
    type(pitch)

    # print('Using {}'.format(int(pitch)))

    # amplitude = rms(signal)
    # print(amplitude)

    note = int(pitch)
    if note > 127:
        note = 0
# *****Possible incorrect format/use of Aubio's onset detection*****
# Attempt at aubio's onset implementation. Currently doesn't send MIDI to DAW when formatted like this.
    if onset(signal) and not isNoteOn:
        isNoteOn = True
        currentNote = note
        # print("On?")
        on = Message('note_on', note=note)
        # print('Sending {}'.format(on))
        if isNoteOn == True
            port.send(on)
        
        # off = Message('note_off', note=note)
        # print('Sending {}'.format(off))
        # port.send(off)
        # time.sleep(0.1)
    elif isNoteOn:
        isNoteOn = False
        # print("off?")
        off = Message('note_off', note=currentNote)
        # print('Sending {}'.format(off))
        port.send(off)
    
        # if note > 0:
        #     on = Message('note_on', note=note)
        #     print('Sending {}'.format(on))
        #     port.send(on)

        #     off = Message('note_off', note=note)
        #     print('Sending {}'.format(off))
        #     port.send(off)
        #     time.sleep(0.1)
        # else:
        #         off = Message('note_off', note=note)

    return (in_data, pyaudio.paContinue)
# ----------------------------------------------------------------------------------
# Open and Start stream.
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size,
                stream_callback=callback)
                
stream.start_stream()
# ----------------------------------------------------------------------------------
# We will put our UI stuff in this while loop
while True:
    try:
        print("We will put UI here...")
        sleep(1)
    except KeyboardInterrupt:
        print("*** Ctrl+C pressed, exiting...")
        break
# ----------------------------------------------------------------------------------
# Exits program.
stream.stop_stream()
stream.close()
p.terminate()
# ----------------------------------------------------------------------------------

