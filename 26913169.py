n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
sum=0
m=n-1
for i in range(n):
    sum+=m*a[i] 
    m-=2 
print(sum)