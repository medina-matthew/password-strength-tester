# Password Strength Tester

This project is a password strength tester written in Python. It aims to evaluate the strength of passwords based on multiple factors, providing feedback and recommendations for improvement. This is my first project and will be published on my GitHub.

## Project Overview

The password strength tester evaluates passwords by checking for:

	•	Length (minimum recommended length)
	•	Uppercase letters
	•	Lowercase letters
	•	Numbers
	•	Special characters
	•	Commonly used passwords (the tester checks against a list of common passwords to prevent weak choices)
	•	Password Entropy (a measure of how unpredictable the password is)

### Ratings:

The tester provides the following ratings based on the password’s strength:

	•	Super Weak
	•	Weak
	•	Okay
	•	Strong
	•	Extra Strong

## Usage Examples

Here are some examples of passwords and their expected strength ratings:

	•	123456 – Super Weak
	•	Password123! – Okay
	•	G#k4L%p9z – Strong

Simply input your password in the terminal, and the program will analyze it and provide feedback on how to strengthen it.

## Future Improvements

In future updates, I plan to add:

	•	A recommended password generator to suggest strong passwords.
	•	Feedback on how long it would take for the password to be cracked using brute force.
	•	Integration with external APIs (like HaveIBeenPwned) to check if the password has been compromised.
