"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = get_user_score()
    print_score(score)
    score = get_rand_score()
    print_score(score)


def print_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Pass")
        else:
            print("Bad")


def get_user_score():
    score = float(input("Enter score: "))
    return score


def get_rand_score():
    score = random.randint(0, 100)
    return score


main()
