from password_checker import PasswordChecker

def main():
    print("Hello, welcome to the password strength tester!\n")

    password = input("Enter a password to test its strength:\n")
                     
    checker = PasswordChecker(password)

    if checker.input_validation:
        print('Password cannot be empty\n')
    else:
        result = checker.check_strength()

        print(result)

if __name__ == "__main__":
    main()