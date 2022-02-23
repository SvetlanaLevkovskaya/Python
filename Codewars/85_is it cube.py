""" Return true if the cuboid could have equal sides, return false otherwise.
Return false for invalid numbers too (e.g volume or side is less than or equal to 0)."""


def cube_checker(volume, side):
    if volume > 0 and side > 0:
        if volume % side == 0:
            return True
    return False


print(cube_checker(12, 3))
print(cube_checker(-12, 3))
