
import random

NUM_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    num_of_lines = get_num_of_lines()
    for line in range(num_of_lines):
        quick_pick = get_quick_pick()
        print(" ".join("{:2}".format(number) for number in quick_pick))


def get_quick_pick():
    quick_pick = []
    for n in range(NUM_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def get_num_of_lines():
    num_of_lines = int(input("How many quick picks? "))
    while num_of_lines < 0:
        print("invalid input")
        num_of_lines = int(input("How many quick picks? "))
    return num_of_lines


main()
