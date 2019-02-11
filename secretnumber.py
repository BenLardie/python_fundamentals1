secret_number = 91
print("Guess the secret number")
user_guess = int(input())

if secret_number == user_guess:
    print("what a guess")
elif (abs(secret_number- user_guess) == 1) :
    print("that was close")
else:
    print("try again")
