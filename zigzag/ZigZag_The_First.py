import time
def solution_1(minn=0, maxx=5, n=0, c=10, design = "********"):
    for _ in range(c):
        while n < maxx: #Counts Up
            time.sleep(0.1)
            display = " "*n + design
            print(display)
            n = n + 1
        while n > minn: #Counts Down
            time.sleep(0.1)
            display = " "*n + design
            print(display)
            n = n - 1

    print("\nDone with solution 1\n\n")








def solution_2(minn=0, maxx=5, c=10, design = "********"):
    #Here n is not something you can change
    #To count down first you need to swap the positions of the two fuctions
    for _ in range(c):
        for n in range(maxx): #Counts Up (e.g 0-4)
            time.sleep(0.1)
            display = " "*n + design
            print(display)
        for n in range(maxx, minn, -1): #Counts Down (e.g 5 - 1)
            time.sleep(0.1)
            display = " "*n + design
            print(display)
    print("\nDone with solution 2\n\n")

def solution_3(minn=0, maxx=5, reverse=False, n=0, c=10, design = "++++++++" ):
    #Lots of problem with this guy
    #Edit But I think I have fixed most of the problem here
    #Here c displays exactly the number of times needed to instead of 
    for _ in range(c):
        if n == maxx: # when at maxx you can only count down (At the peak the only place to go is down)
            reverse = True
        elif n == minn: # when at bottom you can only count up (at rock bottom the only place to go is up)
            reverse = False
        if n < maxx and reverse == False: #Counts Up
            time.sleep(0.1)
            display = " "*n + design
            # print(display + str(n))
            # print(_)
            print(display)
            n = n + 1
        if n > minn and reverse == True: #Counts Down
            time.sleep(0.1)
            display = " "*n + design
            # print(display + str(n))
            # print(_)
            print(display)
            n = n - 1
    print("\nDone with solution 3\n\n")

def solution_4(minn=0, maxx=5, reverse=False, n=0, c=10, design = "++++++++" ):
    # Just realized that solution 4 is solution 3 without the fluffs
    for _ in range(c):
        if n==maxx:
            reverse = True
        elif n==minn:
            reverse = False
        if reverse == False:
            time.sleep(0.1)
            display = " "*n + design
            # print(display + str(n))
            # print(_)
            print(display)
            n = n + 1
        else:
            time.sleep(0.1)
            display = " "*n + design
            # print(display + str(n))
            # print(_)
            print(display)
            n = n -1
    print("\nDone with solution 4\n\n")

solution_1(c=1)
solution_2(c=1)
solution_3()
solution_4()