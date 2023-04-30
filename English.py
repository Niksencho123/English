import random
import time
num1C = 0
num2C = 0
num3C = 0
num4C = 0
num5C = 0
num6C = 0
num7C = 0
CNum = 0
Random_numbers = random.sample(range(1, 50), 7)
Random_numbers.sort()
print("Welcome to 1 through 49!")
time.sleep(2)
print("")
print("Please choose seven numbers!")
Num1 = (int(input("Enter the first number: ")))
Num2 = (int(input("Enter the second number: ")))
Num3 = (int(input("Enter the third number: ")))
Num4 = (int(input("Enter the fourth number: ")))
Num5 = (int(input("Enter the fifth number: ")))
Num6 = (int(input("Enter the sixth number: ")))
Num7 = (int(input("Enter the seventh number: ")))
POSNum = random.sample(range(1,50),49)
POSNum.sort()
if Num1 not in POSNum:
    print("The first number is not from 1 to 49!")
    exit()
if Num2 not in POSNum:
    print("The second number is not from 1 to 49!")
    exit()
if Num3 not in POSNum:
    print("The third number is not from 1 to 49!")
    exit()
if Num4 not in POSNum:
    print("The fourth number is not from 1 to 49!")
    exit()
if Num5 not in POSNum:
    print("The fifth number is not from 1 to 49!")
    exit()
if Num6 not in POSNum:
    print("The sixth number is not from 1 to 49!")
    exit()
if Num7 not in POSNum:
    print("The seventh number is not from 1 to 49!")
    exit()
PNum = [int(Num1),int(Num2),int(Num3),int(Num4),int(Num5),int(Num6),int(Num7)]
PNum.sort()
OtherNum1 = int(Num2),int(Num3),int(Num4),int(Num5),int(Num6),int(Num7)
OtherNum2 = int(Num1),int(Num3),int(Num4),int(Num5),int(Num6),int(Num7)
OtherNum3 = int(Num2),int(Num1),int(Num4),int(Num5),int(Num6),int(Num7)
OtherNum4 = int(Num2),int(Num3),int(Num1),int(Num5),int(Num6),int(Num7)
OtherNum5 = int(Num2),int(Num3),int(Num4),int(Num1),int(Num6),int(Num7)
OtherNum6 = int(Num2),int(Num3),int(Num4),int(Num5),int(Num1),int(Num7)
OtherNum7 = int(Num2),int(Num3),int(Num4),int(Num5),int(Num6),int(Num1)
if Num1 in OtherNum1:
    print("You have two identical numbers!")
    exit()
if Num2 in OtherNum2:
    print("You have two identical numbers!")
    exit()
if Num3 in OtherNum3:
    print("You have two identical numbers!")
    exit()
if Num4 in OtherNum4:
    print("You have two identical numbers!")
    exit()
if Num5 in OtherNum5:
    print("You have two identical numbers!")
    exit()
if Num6 in OtherNum6:
    print("You have two identical numbers!")
    exit()
if Num7 in OtherNum7:
    print("You have two identical numbers!")
    exit()
if Num1 in Random_numbers:
    CNum += 1
    num1C += 1
if Num2 in Random_numbers:
    CNum += 1
    num2C += 1
if Num3 in Random_numbers:
    CNum += 1
    num3C += 1
if Num4 in Random_numbers:
    CNum += 1
    num4C += 1
if Num5 in Random_numbers:
    CNum += 1
    num5C += 1
if Num6 in Random_numbers:
    CNum += 1
    num6C += 1
if Num7 in Random_numbers:
    CNum += 1
    num7C += 1
correct_numbers = []

if num1C == 1:
    correct_numbers.append(Num1)
if num2C == 1:
    correct_numbers.append(Num2)
if num3C == 1:
    correct_numbers.append(Num3)
if num4C == 1:
    correct_numbers.append(Num4)
if num5C == 1:
    correct_numbers.append(Num5)
if num6C == 1:
    correct_numbers.append(Num6)
if num7C == 1:
    correct_numbers.append(Num7)


print("")
print("Your numbers were:",PNum)
if CNum == 1:
    print("You have",CNum,"correct number")
else:
    print("You have",CNum,"correct numbers")
print("The correct numbers were:", Random_numbers)
if len(correct_numbers) > 0:
    print("Your correct numbers were:",correct_numbers)
else:
    print("You have no correct numbers!")
if CNum == 0:
    print("You win nothing")
if CNum == 1:
    print("You win 5$!")
if CNum == 2:
    print("You win 10$!")
if CNum == 3:
    print("You win 100$!")
if CNum == 4:
    print("You win 1000$!")
if CNum == 5:
    print("You win 10000$!")
if CNum == 6:
    print("You win 100000$!")
if CNum == 7:
    print("You win 1000000$!")

