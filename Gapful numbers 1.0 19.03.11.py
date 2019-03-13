from time import sleep

while True:
    number = int(input("Please enter a three digit number  "))
    print()
    print()
    gapfuls = []

    while number >= 100:
    
        snumber = str(number)
        gaptest = int(snumber[0] + snumber[2])
    
        if number%int(gaptest) == 0:
            gapfuls.append(snumber)

        number -= 1
    
    print(gapfuls)
    print()
    print()
    again= input("Would you like to try another number y/n   ")
    print()
    print()
    if again == "y":
        continue
    if again != "y":
        print()
        print()
        for x in range(32):
            print()
        print("Have a good day")
        for x in range(9):
            print()
        sleep(2)
        break