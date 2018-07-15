import random


def flip():
    num = int(input("How many times do you want to flip the coin? "))
    arr = []
    for i in range(num):
        arr.append(random.choice(["heads", "tails"]))
        print(arr[-1])
    print("heads: ", arr.count("heads"))
    print("tails: ", arr.count("tails"))


flip()
