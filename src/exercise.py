def main():
    #write your code below this line

    total = 0

    while True:

        number = int(input("Enter a number: "))

        if number < 0:
            total = total + number
        elif number > 0:
            total = total + number
        elif number == 0:
            print(f"The sum of the numbers is {total}.")

if __name__ == '__main__':
    main()
