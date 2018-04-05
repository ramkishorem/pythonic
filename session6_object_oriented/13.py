"""
Keyword for safety

It is a good idea to start using keyword arguments once a
function or method has three more parameters. Especially,
if there are optional parameters.

Let us assume that we have to set the last maintenance date
but we don't have an ad reel
"""
from screen_control import Screen3DControl

screen6_3d = Screen3DControl(
    'Ready Player one',
    '2018-04-01',
    )

screen6_3d.view_last_3d_maintenance()
# Output: No record of maintenance
screen6_3d.play_ad()
# Output: Ad 2018-04-01 is being played
# WHAT???

# Could you rectify this issue?

screen6_3d = Screen3DControl(
    'Ready Player one',
    last_3d_maintenance='2018-04-01',
    )
screen6_3d.view_last_3d_maintenance()
# Output: Last 3D maintenance was performed on 2018-04-01
screen6_3d.play_ad()
# Output: This screen currently has no ad reel


# It is better to pass everything as keyword argument
# The code will be more readable and you don't have to 
# worry about parameter order
screen6_3d = Screen3DControl(
    movie='Ready Player one',
    last_3d_maintenance='2018-04-01',
    ad_reel="Documentaries"
    )

# We have changed parameter order but we are fine
# since we are passing keyword arguments
screen6_3d.play_ad()
# Output: Ad Documentaries is being played