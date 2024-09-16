n = int(input())
 
a =a = list(map(int, input().split()))
 
cursum =0
for i in range(n-1):
  cursum+=a[i]
 
sum = n*(n+1)//2
 
print(sum-cursum)
