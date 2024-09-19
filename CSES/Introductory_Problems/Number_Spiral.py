n = int(input())
 
 
for i in range(n):
  a = list(map(int, input().split()))
  x = a[0]
  y = a[1]
  
  ans = 0
 
  if x>y:
    base = (x-1)**2
    if x%2!=0:
      ans = y
    else:
      ans = 2*x-y
      
    print(base+ans)
       
  else:
    base = (y-1)**2
    
    if y%2==0:
      ans = x
    else:
      ans = 2*y-x
    print(base+ans) 
 
  
