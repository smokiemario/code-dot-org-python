"""Stage 5: Puzzle 2 of 10

Now, draw a square. NOTE: tell the artist to use your favorite color pen
by assigning a color to the `artist.color` variable.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level25')
a = artist

artist.color = 'red'

a.forward(100)
a.turn_right(90)
a.forward(100)
a.turn_right(90)
a.forward(100)
a.turn_right(90)
a.forward(100)     

artist.check()
