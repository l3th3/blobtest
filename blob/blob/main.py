import os


def bad_one():
    x = input("DIY code :D")
    eval(x)


def bad_two():
    y = input("Will code scanning allow us to suppress both warnings at once???")
    eval(y)


def main():
    bad_one()
    bad_two()


if __name__ == "__main__":
    main()