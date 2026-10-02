import random
print("welcome to the coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

choice = input("Enter your choice (1 or 2):")

if choice == "1":
  random_number = random.randint(1,2)
  if random_number >= 0.5:
    computer_result = "Heads"
  else:
    print("Invalid choice. please select either 1 or 2.")
    
elif choice == "2":
  if random.randint(0,1) == 0:
    computer_result = "Heads"
else:
  print("Invalid choice. please select either 1 or 2.")
  
user_choice = input("Enter your Guess (Heads or Tails):")

if user_choice.lower() == computer_result.lower():
  print("Congratulations! you won!")
else:
  print("sorry, you lost!")
  
print(f"the computer's coin toss result was:{computer_result}")

