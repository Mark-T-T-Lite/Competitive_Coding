t = eval(input())
final =[]
for case in range(t):
    n,k = input().split()
    n,k = int(n),int(k)
    a = [int(x) for x in input().split()]

    for e in range(k):
        a = a[n-1:] + a[:-1]
        
    for num in a:
        print(num, end=' ')
    print()
