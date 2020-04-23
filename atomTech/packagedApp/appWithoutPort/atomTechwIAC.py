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
import wx

# Initialize PyAudio and Select Audio Input
p = pyaudio.PyAudio()
w = wx
# info = p.get_host_api_info_by_index(0)
# numdevices = info.get('deviceCount')
# for i in range(0, numdevices):
#         if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#             print(i, "Input Device I.D. ", " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# ask = input("Which audio input are you using?")
# print(ask)

# ----------------------------------------------------------------------------------
# Set stream parameters (PyAudio).
buffer_size = 1024
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
onset = aubio.onset("wphase", win_s, hop_s, samplerate)
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

    # def octaveOp(direction, shiftAmount):
    #     shiftAmount = shiftAmount * 12

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
# print(p.get_device_info_by_index(ask))
stream = p.open(format=pyaudio_format, 
# input_device_index=int(ask),
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size,
                stream_callback=callback)

start = stream.start_stream()
stop = stream.stop_stream()
# ----------------------------------------------------------------------------------
# We will put our UI stuff in this while loop
while True:
    try:
        class MyPanel(wx.Panel):
            """"""

            #----------------------------------------------------------------------
            def __init__(self, parent):
                """Constructor"""
                wx.Panel.__init__(self, parent)

                self.port = wx.StaticText(self, label="Port:")
                self.note_sent = wx.StaticText(self, label="Note", pos = (250, 225))
                self.velocity_sent = wx.StaticText(self, label="Velocity", pos = (250, 250))
                self.SetBackgroundColour((147, 136, 136))
                self.tbtn = wx.ToggleButton(self, -1, "Start Stream", pos = (200,200))
                self.tbtn.Bind(wx.EVT_TOGGLEBUTTON, self.onUpdate)
                self.tbtn.SetBackgroundColour((229, 18, 39))

                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(self.port, 0, wx.ALL, 5)
                sizer.Add(self.note_sent, 0, wx.ALL, 5)
                sizer.Add(self.velocity_sent, 0, wx.ALL, 5)
                sizer.Add(self.tbtn, 0, wx.ALL, 5)
                self.SetSizer(sizer)
            #----------------------------------------------------------------------
            def update_text(self, info):
                """"""
                # index = {
                    # "Port:":self.port,
                #     "stream status":self.note_sent,
                #     "dial status":self.velocity_Sent
                #     }
                # text = index[info]
                # data = info[1]
                # append = info[0]
                # self.note_sent.SetLabel(info)
                self.port.SetLabel(info[0])
                # self.tbtn.SetLabel("Stop Stream")

            #----------------------------------------------------------------------
            def onUpdate(self, event):
                """"""
                # Active State
                if self.tbtn.GetValue() == True:
                    whichPort = "Port: " + port.name
                    info = [whichPort]

                    self.tbtn.SetLabel('Stop Stream')
                    stream.start_stream()
                    self.update_text(info)
                    print('Stream Begun.')

                # Inactive State
                if self.tbtn.GetValue() == False:
                    whichPort = "Port: "
                    info = [whichPort]

                    self.tbtn.SetLabel('Start Stream')
                    stream.stop_stream()
                    self.update_text(info)
                    print('Stream Stopped.')

        ########################################################################
        class MainFrame(wx.Frame):
            """"""

            #----------------------------------------------------------------------
            def __init__(self):
                """Constructor"""
                wx.Frame.__init__(self, None, title="A.T.O.M. Controller")
                panel = MyPanel(self)
                self.Show()

        if __name__ == "__main__":
            app = wx.App(False)
            frame = MainFrame()
            app.MainLoop()

    except KeyboardInterrupt:
        print("*** Ctrl+C pressed, exiting...")
        break
# ----------------------------------------------------------------------------------
# Exits program.
stop = stream.stop_stream()
stream.close()
# print(p.get_device_info_by_index(ask))
p.terminate()
# ----------------------------------------------------------------------------------

