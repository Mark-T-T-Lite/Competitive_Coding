n = eval(input())
o=[]
if n>=1 and n<=100:
    for x in range(n):
        strx = input()
        if len(strx)>=1 and len(strx)<=100000:
            if ("a" in strx or "A" in strx) and ("e" in strx or "E" in strx)and ("i" in strx or "I" in strx) and ("o" in strx or "O" in strx) and ("u" in strx or "U" in strx):
                o.append("lovely string")
            else:
                o.append("ugly string")

    for x in o:
        print(x)
        
    
