for i in [1,4,6,9,7]:
    print(i)

for n in range(1):
    print("=")

for j in range(5):
    print("what are you doing ", j)

time = 0
while time <= 5:
    print(time)
    time = time + 2


max_number = 5
a = 1


while a < max_number:
    print("the maximum number is reached!")
    a = a + 1

print("programm exhausted")    
    
domestic_animals = ["Goats","Cattle","dogs","cats"]

for animals in domestic_animals:
    if animals == "dogs":
        break
    print(animals)
    
for animals in domestic_animals:
    if animals == "dogs":
        continue
    print(animals)
    
