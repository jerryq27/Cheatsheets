import random
from Common import app

app.print_title("Guess The Number App")

secret_number = random.randint(0, 100)

user_number = None
while user_number != secret_number:
    user_number = int(input("Enter a number between 0 and 100: "))

    direction = None
    if user_number < secret_number:
        direction = "LOWER"
    elif user_number > secret_number:
        direction = "HIGHER"
    else:
        print("YES! You've got it. The number was", secret_number)
        break

    print("Sorry, but", user_number, "is", direction, "than the number")
