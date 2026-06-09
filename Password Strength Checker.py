import string

print("Password Strength Checker\n")

print(
  """ 
  Password Requirements:
  - At least 1 uppercase
  - At least 1 number
  - Minimum 8 characters
  - At least 1 special character 
"""
)

password = input("Enter your password: ")
score = 0

# Check password length
def password_length(password):
  if len(password) < 8:
    print(f"Your password only has {len(password)} characters. Please create a password with 8 characters.❌")
    return 0
  else:
    print(f"Your password meets the minimum length requirement ✅")
    return 2
score += password_length(password) 

# Check lowercase, uppercase, and digit requirements
def password_check(password, condition, description):
    for char in password:
        if condition(char):
            print(f"Contains {description} ✅")
            return 2
    print(f"Does not contain {description} ❌")
    return 0

score += password_check(password, str.islower, "lowercase")
score += password_check(password, str.isupper, "uppercase")
score += password_check(password, str.isdigit, "number")

# Checks special characters 
def contain_special(char):
    return char in string.punctuation

score += password_check(password, contain_special, "special character")


# Print and check score
print(f"\nYour password strength score is: {score}/10")
if score < 4:
    print("Weak Password!")
elif score < 8:
    print("Moderate Password!")
else:
    print("Strong Password!")

