import numpy as np

# Using numpy in Entropy


class PasswordChecker:

    def __init__(self, password=""):
        self.password = password

    def length(self):
        password_length = len(self.password)

        if password_length < 8:
            return "Super Weak! Your password is less than 8 characters long. A hacker can crack this within days to weeks."
        elif 8 <= password_length < 10:
            return "Weak! Your password is 8-9 characters long. It could be cracked within weeks to months."
        elif 10 <= password_length < 12:
            return "Medium Strength. Your password is 10-11 characters long. It would take months for a hacker to crack this."
        elif 12 <= password_length < 14:
            return "Strong! Your password is 12-13 characters long. It would take several months to a year to crack this password."
        elif password_length >= 14:
            return "Super Strong! Your password is 14 or more characters long. It would take years or more for a hacker to crack this."

    def lowercase_letters(self):
        amount_of_lowercase_letters = sum(1 for c in self.password if c.islower())

        if amount_of_lowercase_letters < 1:
            return "Super Weak! You have 0 lowercase letters, and a hacker can crack this within days to weeks."
        elif 1 <= amount_of_lowercase_letters < 2:
            return "Weak! You have 1 lowercase letter, and it would take weeks to months for a hacker to crack this."
        elif 2 <= amount_of_lowercase_letters < 3:
            return "Medium Strength. You have 2 lowercase letters, and it would take months to crack this password."
        elif 3 <= amount_of_lowercase_letters < 4:
            return "Strong! You have 3 lowercase letters, and it would take several months to a year for a hacker to crack this."
        elif 4 <= amount_of_lowercase_letters:
            return "Super Strong! You have 4 or more lowercase letters, and it would take more than a couple of years to crack this password."

    def uppercase_letters(self):
        amount_of_uppercase_letters = sum(1 for c in self.password if c.isupper())

        if amount_of_uppercase_letters < 1:
            return "Super Weak! You have 0 uppercase letters, making your password easy to crack within days to weeks."
        elif 1 <= amount_of_uppercase_letters < 2:
            return "Weak! You have 1 uppercase letter, and it would take weeks to months for a hacker to crack this."
        elif 2 <= amount_of_uppercase_letters < 3:
            return "Medium Strength. You have 2 uppercase letters, and it would take months to crack this password."
        elif 3 <= amount_of_uppercase_letters < 4:
            return "Strong! You have 3 uppercase letters, and it would take several months to a year for a hacker to crack this."
        elif 4 <= amount_of_uppercase_letters:
            return "Super Strong! You have 4 or more uppercase letters, and it would take more than a couple of years to crack this password."

    def numbers(self):
        amount_of_numbers = sum(1 for c in self.password if c.isdigit())

        if amount_of_numbers < 1:
            return "Super Weak! You have 0 numbers in your password, and a hacker can crack this within days to weeks."
        elif 1 <= amount_of_numbers < 2:
            return "Weak! You have 1 number, and it would take weeks to months for a hacker to crack this."
        elif 2 <= amount_of_numbers < 3:
            return "Medium Strength. You have 2 numbers, and it would take months for a hacker to crack this password."
        elif 3 <= amount_of_numbers < 4:
            return "Strong! You have 3 numbers, and it would take several months to a year to crack this password."
        elif 4 <= amount_of_numbers:
            return "Super Strong! You have 4 or more numbers, and it would take more than a couple of years to crack this password."

    def special_characters(self):
        special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
        amount_of_special_characters = sum(
            1 for c in self.password if c in special_characters
        )

        if amount_of_special_characters < 1:
            return "Super Weak! You have 0 special characters, a hacker can crack this within days to weeks."
        elif 1 <= amount_of_special_characters < 2:
            return "Weak! You have 1 special character, a hacker can crack this within weeks to months."
        elif 2 <= amount_of_special_characters < 3:
            return "Medium Strength. You have 2 special characters, a hacker can crack this within months."
        elif 3 <= amount_of_special_characters < 4:
            return "Strong! You have 3 special characters, it would take a hacker several months to a year to crack this."
        elif 4 <= amount_of_special_characters:
            return "Super Strong! You have 4 or more special characters, it would take more than a couple of years to crack this."

    def is_common(self):
        with open("common-passwords.txt", "r") as file:
            common_passwords = set(file.read().splitlines())
        return self.password in common_passwords

    def entropy_calculator(self):
        character_set_size = 0

        if any(c.islower() for c in self.password):
            character_set_size += 26
        if any(c.isupper() for c in self.password):
            character_set_size += 26
        if any(c.isdigit() for c in self.password):
            character_set_size += 10
        if any(c in "!@#$%^&*()_+-=[]{}|;:',.<>/?" for c in self.password):
            character_set_size += 32

        password_length = len(self.password)

        if character_set_size > 0:
            entropy = password_length * np.log2(character_set_size)
        else:
            entropy = 0

        if entropy < 30:
            return "Super Weak! Entropy less than 30 bits, a hacker could brute force this type of password almost instantly!"
        elif 30 <= entropy < 40:
            return "Weak! Entropy between 30 and 40 bits, a hacker could brute force this type of password in the matter of hours."
        elif 40 <= entropy < 50:
            return "Medium Strength. Entropy between 40 and 50 bits, a hacker could brute force this type of password in the matter of days."
        elif 50 <= entropy < 60:
            return "Strong! Entropy between 50 and 60 bits, it would take a hacker years or even decades for a brute force attack to be successful."
        elif entropy >= 60:
            return "Super Strong! Entropy greater than 60 bits, it would be practically impossible for a hacker to be successful."

    def check_strength(self):
        length_feedback = self.length()
        lowercase_feedback = self.lowercase_letters()
        uppercase_feedback = self.uppercase_letters()
        numbers_feedback = self.numbers()
        special_characters_feedback = self.special_characters()
        entropy_feedback = self.entropy_calculator()

        feedback = (
            f"Length:\n     {length_feedback}\n"
            f"Lowercase Letters:\n     {lowercase_feedback}\n"
            f"Uppercase Letters:\n      {uppercase_feedback}\n"
            f"Numbers:\n        {numbers_feedback}\n"
            f"Special Characters:\n     {special_characters_feedback}\n"
            f"Entropy:\n        {entropy_feedback} bits"
        )
        return feedback
