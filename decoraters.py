def my_decorator(func):
    def wrapper():
        print("Something is happeing before the function is called.")
        func()
        print("Somthing is happening after the function is called")

    return wrapper

@my_decorator
def say_hello():
    print('Helooo')

say_hello()
