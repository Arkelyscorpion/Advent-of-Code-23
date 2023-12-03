import re

re = re.compile(r"\d+")
def find(line):
    end = 0
    while m:=re.search(line,end):
        start = max(m.start()-1,0)
        end = m.end()+1
        yield start,min(end,len(line)-1),int(m[0])

def hasSym(y,start,end,check):
    return[
        f"{x+start} - {ln}"
        for ln in [max(y-1,0),y,min(y+1,len(input)-1)]
        for x,char in enumerate(input[ln][start:end])
        if check(char)
    ]

with open("input.txt") as f:
    input = f.read().strip().split("\n")
    print(sum(
        number
        for y,line in enumerate(input)
        for start,end,number in find(line)
        if any(hasSym(y,start,end,lambda c:c not in "1234568790."))
    ))
    numbers = [
        (number,coord)
        for y,line in enumerate(input)
        for start,end,number in find(line)
        for coord in hasSym(y,start,end,lambda c:c=="*")
    ]
    check = []
    def append(c,number):
        check.append(c)
        return number
    result =[
        append(c1,n1*n2)
        for i,(n1,c1) in enumerate(numbers)
        for j,(n2,c2) in enumerate(numbers)
        if j!=i and c1 == c2 and c1 not in check
    ]
    print(sum(result))






    


