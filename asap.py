def main():
    # Predefined password
    correct_password = "password123"

    # Number of attempts allowed
    attempts_allowed = 4

    # Initialize attempt counter
    attempts = 0

    # Loop until either correct password is entered or attempts exhausted
    while attempts < attempts_allowed:
        # Prompt user for password
        password = input("Enter the password: ")

        # Check if password is correct
        if password == correct_password:
            print("Access granted.")
            break  # Exit the loop if password is correct
        else:
            attempts += 1
            remaining_attempts = attempts_allowed - attempts
            print(f"Invalid password. {remaining_attempts} attempts remaining.")

    # If all attempts are used without success
    if attempts == attempts_allowed:
        print("Try again tomorrow.")

if __name__ == "__main__":
    main()