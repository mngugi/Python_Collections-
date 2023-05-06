# find nlargest and nsmallest
import  heapq
results = [65,59,89,89.9999999,89.899977,90]
d = heapq.nlargest(3, results)
print('N largest Number ', d, '\n----------\n' )
e = heapq.nsmallest(3, results)
print('N smallest number',e )

