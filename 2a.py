import re
cnt = 0
bruh = set()
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
       gameId = int(re.search('\d+',line).group())
       line = re.sub('Game \d+:','',line)
       line = re.sub('[,;]','',line)
       line = line.strip()
       line = line.split(' ')
       vals = {
           "green" : 13,
           "blue" : 14,
           "red" : 12
       }
       for i in range(1,len(line),2):
           color = line[i]
           valofcol = int(line[i-1])
           if(valofcol > vals[color]):
               bruh.add(gameId)  
    print(5050-sum(bruh))