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
else: 
    print(f"{user_choice} is incorrect. The correct answer is a.")

print("\n2. (Kristoffer Anipan) What is my age?")
print("a. 20")
print("b. 19 ")
print("c. 21")
print("d. 18")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'a': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is a.")

print("\n3. (Ma. Rose L. Tolentino) Which naming convention is used in Python?")
print("a. Pascal Case")
print("b. Snake Case")
print("c. Camel Case")
print("d. Eagle Case")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'b': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is b.")

print("\n4. (Ma. Rose L. Tolentino) ")
print("What data type is the following?")
print("a. Boolean")
print("b. String")
print("c. Integer")
print("d. Float")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'b': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is b.")
    
print(f"\nYour score is {score_counter}/10")
