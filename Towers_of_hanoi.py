from stack import Stack

print("\n Let's play Towers of Hanoi!")

#  Create the Stacks

stacks = []

left_stack = Stack("Left")

middle_stacks = Stack("Middle")

right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stacks)
stacks.append(right_stack)

#   Set up the game
while True:
    try:
        num_disks = int(input("\nHow many disks do you want to play with?\n"))
    except ValueError:
        print("\n Oops, looks like you didn't enter an integer number\n")
        continue
    while num_disks < 3:
        try:
            num_disks = int(input("\nEnter a number greater than or equal to 3\n"))
        except ValueError:
            print("Oops, looks like you didn't enter an integer number")
            continue
    break


for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = 2**num_disks - 1

print("\n\n  The fastest you can solve this game is in {number} moves".format(number = num_optimal_moves))

# Get user input

def get_input():
    choices = [item.get_name()[0] for item in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))
        user_input = input("").upper()
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Play the Game

num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for item in stacks:
        item.print_items()
    while True:
        print("\n  Which stack do you want to move from?\n")
        from_stack = get_input()
        print("\n\n  Which stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n  Invalid Move. Try again")
        elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\n  Invalid Move. Try Again")

print("\n\n You completed the game in {0} moves, and the optimal number of moves was {1}".format(num_user_moves, num_optimal_moves))
