d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}


def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")


print(get_drink_by_profession("raPPer"))
