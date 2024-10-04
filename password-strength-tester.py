from password_checker import PasswordChecker


# Defining main, calls class PasswordChecker
# Input validation to make sure string is not emptys

def main():
    print("Hello, welcome to the password strength tester!\n")

    password = input("Enter a password to test its strength:\n")

    if input == '':
        print('Password cannot be empty')
                     
    checker = PasswordChecker(password)

    result = checker.check_strength()

    print(result)

if __name__ == "__main__":
    main()
