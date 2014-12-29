"""Stage 5: Puzzle 10 of 10

You made it! Now, draw anything you want. Some fun ideas: a stick figure,
snowflake, or spiral. Also try the new `artist.width` setting. Have fun!

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level33')
a = artist
artist.speed = 'fastest'

for count in range(1000):
    artist.color = artist.random_color()
    artist.width = 1
    artist.move_forward(1)
    a.turn_right(1)
    
artist.wait()
