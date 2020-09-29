def upperCase(user_input):
    sentences = user_input.split('. ')
    sentences1 = [c[0].capitalize() + c[1:] for c in sentences]
    string = '. '.join(sentences1)
    return string


def main():
    user_input = input("Say Hello: ")
    result = upperCase(user_input)
    print(result)


main()