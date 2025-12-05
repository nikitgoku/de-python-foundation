from ..greeting.greeting import say_hello


def main():
    name_input = input("Say you name: ")
    say_hello(name=name_input)

if __name__ == "__main__":
    main()