do = input("What will you do? (type LOOK) ")                                                  1
if do == "LOOK":                                                   2
    print("You are stuck in a sand ditch.")
    print("Crawl out LEFT or RIGHT.")

    do = input(":: ")                                              3
    if do == "LEFT":                                               4
        print("You make it out and see a ship!")
        print("You survived!")
    elif do == "RIGHT":                                            5
        print("No can do. That side is very slippery.")
        print("You fall very far into some weird cavern.")
        print("You do not survive :(")
else:                                                              6
    print("You can only do actions shown in capital letters.")
    print("Try again!")