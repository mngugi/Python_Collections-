'''
this program creates an array of 5 elements
'''
import array as arr
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Array Test")

# create an array of 5 integers using a function arr1()
def arr1():
    array1 = arr.array('i', [4, 6, 7, 9, 8])
    row = ''
    for n in array1:
        row += str(n) + ' '
    return array1

print("================================")
print('row', arr1())
print("________________________________")

