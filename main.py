score_counter = 0

print("1. (Kristoffer Anipan) What is my favorite snack? ")
print("a. Jumpee")
print("b. Loaded ")
print("c. Pillows")
print("d. Piattos")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'a': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
    print ("")
else: 
    print(f"{user_choice} is incorrect. The correct answer is a.")
    print ("")

print("2. (Kristoffer Anipan) What is my age?")
print("a. 20")
print("b. 19 ")
print("c. 21")
print("d. 18")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'a': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
    print ("")
else: 
    print(f"{user_choice}is incorrect. The correct answer is a.")
    print ("")

print(f"Your score is {score_counter}/10")
