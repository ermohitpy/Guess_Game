

h_no = 22#hidden number
y = 5
while y >= 0:
    x = int(input('guess the no:\n'))

    if x == h_no:
        print("you are right")
        print("you complete it in {} chances".format(y))
        break
    elif x > h_no:
        print("your no is greater than the req no\n")
        print("Try again")
        y = y - 1
        if y == 0:
            break
        print("you have {} chances".format(y))
        continue
    elif x < h_no:
        print("your no is less than the req no\n")
        print("Try again")
        y = y-1
        if y == 0:
            break
        print("you have {} chances".format(y))
        continue

print("GAME OVER")