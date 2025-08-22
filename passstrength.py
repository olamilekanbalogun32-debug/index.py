import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password too short (minimum 8 characters).")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc.).")

    # Evaluate strength
    if strength <= 2:
        verdict = "Weak"
    elif strength <= 4:
        verdict = "Moderate"
    else:
        verdict = "Strong"

    return verdict, feedback


# Run the tool
password = input("Enter a password to test: ")
verdict, feedback = assess_password_strength(password)

print(f"\nPassword Strength: {verdict}")
if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)
else:
    print("Great job! Your password is strong.")
