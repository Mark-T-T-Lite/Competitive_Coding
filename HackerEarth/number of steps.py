#number of steds

n = eval(input())
a= [int(x)for x in input().split()]
b = [int(x)for x in input().split()]
count = 0
bre = True

for t in range(n):
    if bre:
        for x in range(max(a)):
            if a[t] >= b[t]:
                a[t]= a[t]-b[t]
            else:
                


                  
##            if max(a)== min(a):
##                print(n)
##                bre=False
##                break
##            
##            
##                a[count]=x-b[count]
##                print(a)
##                #print(b)
##                
##            count += 1
##            n+=1
##        count = 0
##   
##print(-1)
