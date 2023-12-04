import re

def intersection(l1,l2):
    return [val for val in l1 if val in l2]

cnt = 0
with open("input.txt") as f:
    input = f.read().strip().split("\n")
    Map = [1]*188
    Map[0] = 0
    Map[1] = 1
    for line in input:
        cardNum = int(re.search('\d+',line).group())
        line = re.sub("Card \d+: ",'',line)
        a,b = line.strip().split('|')
        a = a.split(" ")
        b = b.split(" ")
        newa = [val for val in a if val!='']
        newb = [val for val in b if val !='']
        vals = len(intersection(newa,newb))
        if vals != 0:
            for i in range(cardNum+1,cardNum+vals+1):
                Map[i] += Map[cardNum]

        if len(intersection(newa,newb)) != 0:
            cnt += (2**(len(intersection(newa,newb)) -1))
    print(f"The answer to part 1 is {cnt}")
    print(f"The answer to part 2 is {sum(Map)}")
        
        
        