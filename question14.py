import matplotlib.pyplot as plt

labels = ('python','katolin', 'C++', 'C', 'java')
index = (1,2,3,4,5)

sizes = [45,5,15,20,30]

plt.ylabel('Usage')
plt.xlabel('Programming Language')

plt.bar(index, sizes)
plt.xticks(index, labels)
plt.show()