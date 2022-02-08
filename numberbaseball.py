import random

class Randomnumber:
    def __init__(self):
        self.answer = self.generate()
        self.first = self.answer[0]
        self.second = self.answer[1]
        self.third = self.answer[2]
    def generate(self):
        number = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(number)
        n1 = str(number.pop())
        random.shuffle(number)
        n2 = str(number.pop())
        random.shuffle(number)
        n3 = str(number.pop())
        answer = n1 + n2 + n3
        return answer
    def __repr__(self):
        return self.answer

a = Randomnumber().answer

def guess():
    guess_input = input("Enter your guess: ")
    return guess_input

def sandb(myguess, answer):
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


game_over = 0
a = Randomnumber()
goal = a.answer
round_counter = 1 
while not game_over:
    try:
        print(f'Round {round_counter}')
        my_guess = guess()
        strikes, balls = sandb(my_guess, goal)
        round_counter += 1
    except:
        print("Type a number with 3 different digits!")
        continue
    else:
        if strikes == 3:
            print(f"3strikes! you got the answer! The answer is {goal}!")
            game_over += 1
    

