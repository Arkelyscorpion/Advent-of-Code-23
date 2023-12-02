import re
cnt = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
       gameId = int(re.search('\d+',line).group())
       line = re.sub('Game \d+:','',line)
       line = re.sub('[,;]','',line)
       line = line.strip()
       line = line.split(' ')
       vals = {
           "green" : [],
           "blue" : [],
           "red" : []
       }
       for i in range(1,len(line),2):
           color = line[i]
           valofcol = int(line[i-1])
           vals[color].append(valofcol)
       cnt+=(max(vals['blue'])*max(vals['green'])*max(vals['red']))
    print(cnt)