import mido
from time import sleep

outport = mido.open_output('atomCtrl', virtual=True)

while True:
  outport.send(mido.Message('note_on', note=100, velocity=3))
  sleep(1)
  outport.send(mido.Message('note_off', note=100, velocity=0))