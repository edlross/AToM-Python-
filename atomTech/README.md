## *ATOM Technology* (Documentation)


### Edward Ross

### Uploaded on:
2:45PM on 3/26/2020

### Files Included
- atomTech.py
- README.md 


### ATOM Tech
The purpose of this program is to convert audio from a given input into a MIDI message that can be used as a MIDI output. The intention of the program is allow all musicians to naturally utilize MIDI without having to learn how to play the piano. This allows for innovation in both production and performance.

### Description
The ATOM program takes a signal from the given audio input, analyzes the pitch and amplitude, then converts that information into MIDI Note and Velocity. The program then sends the data as a MIDI Message to the user's desired MIDI port, which makes the program accessible as a MIDI controller.

### Caveats
Recognition of some timbres and registers are faulty, future implementation will include presets for different instruments. In this version of the software, aftertouch needs to be implemented. Aftertouch and pitch wheel parameters are both attempted inside of the "Modifications." folder.

### Dependencies
This program requires the Aubio, wxPython, and Mido python libraries.
