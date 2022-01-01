import random
import time
import os

os.system('cls')

print("="*31)
print("\n### Scrissor - Paper - Rock ###")
print("\n        I Hope You \n     Enjoy This Game")
print("\n   Created by @Deavennn \n           2021      \n")
print("="*31)
while True:    
    time.sleep(1.7)
    os.system('cls')
    print("="*28)
    print("Action List:")
    print("1.Rock\n2.Scrissor\n3.Paper")
    print("="*28)
    player = int(input("\nChoose Your Action: "))
    comp = random.randint(1,3)

    time.sleep(1)
    os.system('cls')
    if player == 1:
        if comp == 1:
            print("# Result :: you choose ~Rock~ and computer choose ~Rock~\n")
            print("========")
            print("= Draw =")
            print("========")
        elif comp == 2:
            print("# Result :: you choose ~Rock~ and computer choose ~Scrissor~\n")
            print("===========")
            print("= You Win =")
            print("===========")
        elif comp ==  3:
            print("# Result :: you choose ~Rock~ and computer choose ~Paper~\n")
            print("============")
            print("= You Lose =")
            print("============")
    elif player == 2:
        if comp == 1:
            print("# Result :: you choose ~Scrissor~ and computer choose ~Rock~\n")
            print("============")
            print("= You Lose =")
            print("============")
        elif comp == 2:
            print("# Result :: you choose ~Scrissor~ and computer choose ~Scrissor~\n")
            print("========")
            print("= Draw =")
            print("========")
        elif comp ==  3:
            print("# Result :: you choose ~Scrissor~ and computer choose ~Paper~\n")
            print("===========")
            print("= You Win =")
            print("===========")
    elif player == 3:
        if comp == 1:
            print("# Result :: you choose ~Paper~ and computer choose ~Rock~\n")
            print("===========")
            print("= You Win =")
            print("===========")
        elif comp == 2:
            print("# Result :: you choose ~Paper~ and computer choose ~Scrissor~\n")
            print("============")
            print("= You Lose =")
            print("============")
        elif comp ==  3:
            print("# Result :: you choose ~Paper~ and computer choose ~Paper~\n")
            print("========")
            print("= Draw =")
            print("========")
    else:
        print("!!!   choose 1 or 2 or 3   !!!")
        continue

    lanjut = input("\nNew Game (y/n):  ")
    if lanjut == "y":
        print("\n")
        print("="*20)
        os.system('cls')
        continue
    else:
        os.system('cls')
        print("")
        print("="*33)
        print(" Thank You for Playing this Game")
        print("\n            My Team\n\n          Pisigo Corp.")
        print("="*33)
        time.sleep(1.9)
        os.system('cls')
        break


