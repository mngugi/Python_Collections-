from datetime import datetime

print(f'This is the current time: {datetime.now()}')

print(f'===== Using a Function =========')

def show_date() -> None:
    print(f'This is the current time: {datetime.now()}')

show_date()


def greet(name: str) -> None:
    print(f'Hello, {name}!')


greet('Peter')
greet('Ngugi')