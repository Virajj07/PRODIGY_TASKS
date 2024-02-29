import re


def check_password_strength(password):
    # Minimum length requirement
    min_length = 8

    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        return "Weak - Password should be at least {} characters long.".format(min_length)

    # Check for the presence of uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak - Password should contain at least one uppercase letter."

    # Check for the presence of lowercase letters
    if not any(char.islower() for char in password):
        return "Weak - Password should contain at least one lowercase letter."

    # Check for the presence of numbers
    if not any(char.isdigit() for char in password):
        return "Weak - Password should contain at least one number."

    # Check for the presence of special characters
    special_characters = re.compile('[!@#$%^&*()_-]')
    if not special_characters.search(password):
        return "Weak - Password should contain at least one special character."

    # If the password passes all criteria, consider it strong
    return "Strong - Password meets all criteria for strength."

# Example usage


def main():
    user_password = input("Enter your password: ")
    strength_feedback = check_password_strength(user_password)
    print(strength_feedback)


if __name__ == "__main__":
    main()
