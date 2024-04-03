def main():
    correct_password="asap"
    attempts_allowed=4
    attempts=0
    while attempts<attempts_allowed:
        password=input("Enter password")
        if password==correct_password:
            print("Access Granted")
            break
        else:
            attempts +=1 
            remaining_attempts= attempts_allowed-attempts
            print(f"Invalid Password:{remaining_attempts}attempts_remaining.")
            if attempts==attempts_allowed:
                print("Try again tommorrow")

if __name__=="__main__":
    main()



