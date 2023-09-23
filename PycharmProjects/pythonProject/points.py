
pointsGained = 0
goadDiff = 0

goalsFor =     [1,3,3,0,2,1,4,3,2,3,0]
goalsAgainst = [1,3,2,1,0,2,2,1,3,1,2]

for j in range(11):
    if goalsFor[j] > goalsAgainst[j]:
        pointsGained  +=3
        goadDiff += (goalsFor[j] - goalsAgainst[j])


    elif goalsFor[j] == goalsAgainst[j]:
        pointsGained += 1

    else:
        goadDiff += (goalsFor[j] - goalsAgainst[j])

print(" Points ",pointsGained)
print("Goal difference", goadDiff)

