class MyClass1:
    def __init__(self):
        print("This is MyClass1")

class MyClass2:
    def __init__(self):
        print("This is MyClass2")
        

def main():
    while True:
        print("1. Class 1")
        print("2. Class 2")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            my_class = MyClass1()
        elif choice == '2':
            my_class = MyClass2()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
