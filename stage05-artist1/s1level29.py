"""Stage 5: Puzzle 6 of 10

Can you figure out how draw this triangle and square? Hint: Do the
triangle first, then figure out how much to turn before drawing the
square.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level29')
a = artist

for count in range(3):
    a.forward(100)
    a.turn_right(120)
a.turn_left(90)
for count in range(4):
    a.forward(100)
    a.turn_left(90)
    
artist.check()
