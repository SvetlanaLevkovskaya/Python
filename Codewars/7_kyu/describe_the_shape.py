def describe_the_shape(angles):
    return 'this will be a line segment or a dot' if angles <= 2 \
        else 'This shape has {} sides and each angle measures {}'.format(angles, angles * 20)


print(describe_the_shape(3))


def describe_the_shape(n):
    return  "this will be a line segment or a dot" if n < 3 else \
            "This shape has %s sides and each angle measures %s" % (n, (n-2)*180//n)


print(describe_the_shape(3))
