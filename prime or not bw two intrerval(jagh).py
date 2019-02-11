n,k=map(int,raw_input().split())
for j in range (n+1,k):
    flag=0
    for i in range(n+1,k):
            if n%i==0:
                flag=1
                break
    if flag==0:
         print n

            
