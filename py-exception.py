try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("The number you enter is not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)