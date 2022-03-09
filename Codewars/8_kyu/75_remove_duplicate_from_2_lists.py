def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [x for x in birds if x not in geese]


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]))

