print("Please enter a positive integer:")
user_input = int(input())
print("The factors of", user_input, "are:")
for i in range(1, user_input + 1):
    if user_input % i == 0:
        print(i)