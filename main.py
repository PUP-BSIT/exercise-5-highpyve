score_counter = 0

print("Welcome to HighPYve Quiz!")
print("Answer the following questions by choosing the correct letter.")

print("\n1. (Kristoffer Anipan) What is my favorite snack? ")
print("a. Jumpee                c. Pillows")           
print("b. Loaded                d. Piattos")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'a': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is a.")

print("\n2. (Kristoffer Anipan) What is my age?")
print("a. 20                   c. 21") 
print("b. 19                   d. 18")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'a': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is a.")

print("\n3. (Ma. Rose L. Tolentino) Which naming convention is used in Python?")
print("a. Pascal Case           c. Camel Case")
print("b. Snake Case            d. Eagle Case")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'b': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is b.")

print("\n4. (Ma. Rose L. Tolentino) What data type is the following? my_value = \"True\"")
print("a. Boolean             c. Integer")
print("b. String              d. Float")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'b': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is b.")

print("\n5. (Mikaela Bartolome) Who is my favorite Sanrio Character?")
print("a. Hello Kitty          c. Keroppi")
print("b. My Melody            d. Kuromi")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'b': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is b.")

print("\n6. (Mikaela Bartolome) Where is the location of the first F1 Grand Prix track in 2025?")
print("a. Monaco              c. Australia")
print("b. China               d. Abu Dhabi")
user_choice = input("Enter your answer: ").lower()

if user_choice == 'c': 
    print("You got the correct answer. Congratulations.")
    score_counter += 1
else: 
    print(f"{user_choice} is incorrect. The correct answer is c.")

print(f"\nYour score is {score_counter}/10")