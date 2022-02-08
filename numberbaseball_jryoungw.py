import random
from typing import Union
import numpy as np

class RandomNumber:
    def __init__(self):
        self.answer = self.generate()
        self.first = self.answer[0]
        self.second = self.answer[1]
        self.third = self.answer[2]
    def generate(self):
        number = [i for i in range(10)] # list comprehension
        n = np.random.choice(number, 3, replace=False)
        answer = ''.join([str(i) for i in n])
        return answer
    def __repr__(self):
        return self.answer

def guess() -> str:
    guess_input = input("Enter your guess: ")
    return guess_input

def sANDb(myguess:list, answer:list) -> tuple[int, int]:
    strike = 0
    ball = 0
    for n in range(0,3):
        if myguess[n] == answer[n]:
            strike += 1
    for n in range(0,3):
        if myguess[n] in list(answer) and myguess[n] != answer[n]:
            ball += 1
    if len(myguess) > 3:
        print("The answer has only 3 digits")
        return 'failure'
    elif len(set(myguess)) != 3:
        print("All digits are different")
        return 'failure'
    print(f"{strike}S {ball}B!")
    return strike, ball

if __name__ == '__main__':
    game_over = 0
    a = RandomNumber()
    goal = a.answer
    round_counter = 1 
    while not game_over:
        strikes = 0
        try:
            print(f'Round {round_counter}')
            my_guess = guess()
            strikes, balls = sANDb(my_guess, goal)
            round_counter += 1
        except:
            print("Type a number with 3 different digits!")
            continue
        if strikes == 3:
            print(f"3strikes! you got the answer! The answer is {goal}!")
            game_over += 1
            print("Game ended")
            break

