def str(name):
    for x in range(0,len(name)):
        if name[:2] == name[:x]:
            print("yes")


str("hixxhi")