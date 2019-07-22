x,y=map(int,input().split())
for a in range(x+1,y):
  for b in range(2,a):
    if(a%b==0):
      break
  else:
    print(a,end=" ")
