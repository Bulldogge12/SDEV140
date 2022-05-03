theSum = 0
f = open("steps.txt", 'r')
for num in range(31):
    line = f.readline().strip()
    num = int(line)
    theSum += num
    theAvg = theSum / 31
print(f'{"Month":10}{"Steps":10}{"Daily AVG":10}')
print(f'{"January":8}{theSum:10,d}{theAvg:10,.1f}')
num = 0
theSum = 0
theAvg = 0
for num in range(28):
    line = f.readline().strip()
    num = int(line)
    theSum += num
    theAvg = theSum / 28
print(f'{"February":8}{theSum:10,d}{theAvg:10,.1f}')
num = 0
theSum = 0
theAvg = 0
for num in range(31):
    line = f.readline().strip()
    num = int(line)
    theSum += num
    theAvg = theSum / 31
print(f'{"March":8}{theSum:10,d}{theAvg:10,.1f}')
f.close()
