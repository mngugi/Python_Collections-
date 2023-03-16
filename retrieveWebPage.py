import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://<xxxxxx.com>/ffff.txt')

counts = dict()
for line in fhand:

    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
