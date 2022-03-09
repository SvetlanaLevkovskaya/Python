"""Write a function iceBrickVolume that will accept these parameters:
radius - bottle's radius (always > 0);
bottleLength - total bottle length (always > 0);
rimLength - length from bottle top to brick (always < bottleLength);"""


def ice_brick_volume(radius, bottle_length, rim_length):
    return radius * radius * 2 * (bottle_length-rim_length)


print(ice_brick_volume(5, 30, 7))
            