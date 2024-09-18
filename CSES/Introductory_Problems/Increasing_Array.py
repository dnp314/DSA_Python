n =int(input())
 
a = list(map(int, input().split()))
 
res =0
prev =a[0]
for i in range(1,n):
  if a[i]<=prev:
    res+=prev-a[i]
  else:
    prev=a[i]
 
print(res)