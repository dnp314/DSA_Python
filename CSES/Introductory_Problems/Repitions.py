n = input()
 
cnt =1
maxi=1
for i in range(len(n)-1):
  if n[i]==n[i+1]:
    cnt+=1
  else:
    cnt=1
  maxi =max(maxi,cnt)
  
print (maxi)