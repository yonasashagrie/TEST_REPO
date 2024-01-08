sum_values = 0
count = 0

while True:
    user_input = input("Enter a number: ")

    if user_input == "-1":
        break  # Exit the loop if -1 is entered

    # Convert the user input to an integer
    number = int(user_input)

    sum_values += number
    count += 1

if count > 0:
    average = sum_values / count
    print(f"The average is: {average}")
else:
    print("No numbers were entered.")
