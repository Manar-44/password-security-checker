password = input("Enter your password: ")
score = 0
suggestions = []
password_lenght = 15

length = len(password)
if length >= password_lenght:
    score += 1
else:
    suggestions.append("Increase password length")


has_uppercase = any(char.isupper() for char in password)
if has_uppercase:
    score += 1
else:
    suggestions.append("Consider adding uppercase letters")

has_lowercase = any(char.islower() for char in password)
if has_lowercase:
    score += 1
else:
    suggestions.append("Consider adding lowercase letters")

has_number = any(char.isdigit() for char in password)
if has_number:
    score += 1
else:
    suggestions.append("Consider adding numbers")

has_special_char = any(not char.isalnum() and not char.isspace() for char in password)
if has_special_char:
    score += 1
else:
    suggestions.append("Consider adding special characters")




if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"


print(f"Password strength: {strength}")
print(f"Score: {score}/5")

if suggestions:
    print("\nSuggestions: ")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("\nNo improvement suggestions. ")
