def function1():
    print('stuff goes in here')

def main():
    while True:
        print("Menu:")
        print("1. Perform action 1")
        print("2. Perform action 2")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            function1()
        elif choice == '2':
            function2()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
