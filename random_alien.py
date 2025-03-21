import random

aliens = []
color = ['red', 'green', 'dark', 'blue']

for alien in range(0,4):
    rand_color = random.choice(color)
    new_alien = {'color' : rand_color, 'points' : 5}
    aliens.append(new_alien)

for color in aliens :
     if color['color'] == 'green':
          print ('green! Let them em ')
     elif color['color'] == 'dark':
          print ('Kill EM !!')
