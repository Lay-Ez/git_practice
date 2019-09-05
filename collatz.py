while True:
    user_number = int(input("\n What's your number for conjecture?\n"))

    def collatz(number):
        if number == 1:
            return 0
        if number%2 == 0:
            return 1 + collatz(number / 2)
        return 1 + collatz(number * 3 + 1)

    collatz_result = collatz(user_number)
    print("\n The result for number {} is {} iterations\n".format(user_number, collatz_result))
