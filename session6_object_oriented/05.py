"""
Using attributes outside

You may directly use the attributes of an instance without 
having to call methods.
"""

screen1 = ScreenControl('Ready Player One', 'English Trailers')
# You can instantiate a class as many times as you want.
# That is the main selling point of classes.
screen2 = ScreenControl('Avengers', 'A list of commercials')

print('Screen 2 is playing {}'.format(screen2.movie))
# Output: Screen 2 is playing Avengers

print('Screen 1 will play reel {} during interval'.format(
    screen1.ad_reel))
# Output: 
# Screen 1 will play reel English Trailers during interval

