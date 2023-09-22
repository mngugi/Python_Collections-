import random

print("-------------")
if 20 > 10:
    print("Done!")

print("-------------")

if 10 > 20:
    print("Done!")
else:
    print("Not Done!")

print("-------------")
print("============================if=============else============elif=======")

homeTeam = 0
awayTeam = 0

if homeTeam < awayTeam:
    print("Increase intensity and the final 3rd")
elif homeTeam == awayTeam:
    print("Retreat to defensive mode to avoid conceding more goals!")
else:
    print("All in attacks!")

print("============================================================")
print("==========================For=================================")

Teamhome = ["Inaki", "Casemiro", "Hererra"]
TeamAway = ["Williams", "Rodriguez", "Ander"]

for j in Teamhome:
    print("Lets Get in: " + j)
    for i in TeamAway:
        print("Get in: " + i)

print("============================while===============================")

possession = True
ballRetention = 85
passCompletion = 95

while possession:
    if random.randint(0, 100) > ballRetention:
        possession = False
    else:
        passCompletion += 1
        print(passCompletion)
