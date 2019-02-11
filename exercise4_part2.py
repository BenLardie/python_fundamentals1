print("What is your age?")
user_age = input()

if int(user_age) > 105:
    print("I'm not sure I belive you")
else:
    print("we are {} years apart".format(int(user_age) - 30))
