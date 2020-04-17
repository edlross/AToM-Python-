# PURPOSE: To track the audio input's amplitude then scale it to velocity
# Update~ Adds scaling component to be converted to velocity.
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
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print(i, "Input Device I.D. ", " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

ask = input("Which audio input are you using?")
print(ask)

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
ampOnset = aubio.onset("default", win_s, hop_s, samplerate)
pitchOnset = aubio.onset("wphase", win_s, hop_s, samplerate)
# Converts frequencies to MIDI numbers.
pitch_o.set_unit("Hz") 
# Sets sensitivity of pitch detection.
pitch_o.set_tolerance(tolerance)
pitch = 0
isNoteOn = False
currentNote = 0
prevNote=0
# MIDI initialization
port = mido.open_output('atomCtrl', virtual = True, autoreset=True)
# ----------------------------------------------------------------------------------
# define callback function to processing/analysis within this function definition. 
def callback(in_data, frame_count, time_info, flag):
# -------------------------------------------
# Initialize functions and variables within Callback
    global pitch, isNoteOn, currentNote, port, prevNote

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

# -------------------------------------------

    if pitch == 0:
        pitch = 1

    ftom = aubio.freqtomidi(pitch)

    remainder = ftom % 1

    if remainder > 0.5:
        mNote = ftom + 1
    else:
        mNote = ftom

    mFreq = aubio.miditofreq(int(mNote))

    if mFreq == 0:
        mFreq = 1

    
    ratio =  pitch/mFreq

    bend = int(4096 *(12 * np.log2(ratio)))

# -------------------------------------------

    amplitude = scale(rms, 0, 1, 0, 127)

    velocity = int(amplitude)

    note = int(mNote)
    if note > 127:
        note = 0
    if note == 1:
        note = 0

    if velocity > 127:
        velocity = 127

    if bend > 8191:
        bend = 8191
    if bend < -8192:
        bend = -8192

# -------------------------------------------

    if ampOnset(signal) and not isNoteOn:
        isNoteOn = True
        currentNote = note
        on = Message('note_on', note=note, velocity=velocity)
        print('Sending {}'.format(on))
        port.send(on)
        prevNote=note
        if pitchOnset(signal) and prevNote!=note:
            isNoteOn = True
            currentNote = note
            on = Message('note_on', note=note, velocity=velocity)
            print('Sending {}'.format(on))
            port.send(on)
            prevNote=note
        
    elif velocity < 5:
        isNoteOn = False
        off = Message('note_off', note=currentNote)
        print('Sending {}'.format(off))
        port.send(off)

    return (in_data, pyaudio.paContinue)
# ----------------------------------------------------------------------------------
# Open and Start stream.
stream = p.open(format=pyaudio_format, input_device_index=int(ask),
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
