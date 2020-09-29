def check():
    user_inputs = input("Enter a string: ")
    user_input = user_inputs.lower()
    print(user_input)
    for i in user_input:
        if(user_input.count(i) > user_input.count(i+1)):
            print(user_input.count(i))


check()