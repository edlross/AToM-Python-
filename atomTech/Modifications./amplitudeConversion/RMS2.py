# PURPOSE: To track the audio input's amplitude then scale it to velocity
# Update~ Adds scaling component to be converted to velocity.
# ----------------------------------------------------------------------------------
# Import libraries. 
from __future__ import print_function
import pyaudio
import sys
import numpy as np
from sklearn.preprocessing import minmax_scale
import aubio
import time
import random
import mido
from mido import Message
from time import sleep
import struct
import wxPy

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
# define callback function to processing/analysis within this function definition. 
def callback(in_data, frame_count, time_info, flag):

    global pitch, isNoteOn, currentNote, port

    audio_data = np.fromstring(in_data, dtype=np.float32)
    signal = np.frombuffer(audio_data, dtype=np.float32)
    rms = np.sqrt(np.mean(np.absolute(signal)**2))

    pitch = pitch_o(signal)[0]
    confidence = pitch_o.get_confidence()
    type(pitch)

    def scale(num, minNum, maxNum, scaleMin = 0, scaleMax = 127):

            if num <= minNum:
                num = scaleMin

            if num >= maxNum:
                num = scaleMax

            return (num-minNum)/(maxNum-minNum) * (scaleMax-scaleMin) + scaleMin


    amplitude = scale(rms, 0, 1, 0, 127)

    velocity = int(amplitude)

    note = int(pitch)
    if note > 127:
        note = 0

    if velocity > 127:
        velocity = 127

    def octaveOp(direction, shiftAmount):
        shiftAmount = shiftAmount * 12

        if direction == up:
            notes + shiftAmount
        elif direction == down:
            notes + shiftAmount
        if notes < 24: 
            shiftAmount = 0
    

# Attempt at aubio's onset implementation. Currently doesn't send MIDI to DAW when formatted like this.
    if onset(signal) and not isNoteOn:
        isNoteOn = True
        currentNote = note
        on = Message('note_on', note=note, velocity=velocity)
        print('Sending {}'.format(on))
        port.send(on)
        
    elif velocity < 5:
        isNoteOn = False
        off = Message('note_off', note=currentNote)
        print('Sending {}'.format(off))
        port.send(off)

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

wx = wxPy
# wx.app
# wx.frm.Show()
wx.MainLoop()
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

