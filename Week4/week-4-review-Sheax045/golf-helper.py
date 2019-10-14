print("Welcome to the Golf Club Helper!\nTell me your situation, and I'll recommend a club\n")
greenInput = input("Did you hit it on the green (y/n)? ")
yardInput = input("How far is the ball from the hole? ")

if greenInput == "n":
    if int(yardInput) >= 200:
        print("\nI recommend using your Driver")
    elif (int(yardInput) <= 199) and (int(yardInput) >= 140):
        print("\nI recommend using your 5-Iron")
    elif (int(yardInput) <= 139) and (int(yardInput) >= 100):
        print("\nI recommend using your 9-Iron")
    else:
        print("\nI recommend using your Pitching Wedge")
else:
    print("\nI recommend using your Putter")
    
