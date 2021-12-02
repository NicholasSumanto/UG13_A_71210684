input = int(input("Input:"))
for i in range (1,input+1):
   for j in range (1,2*input) :
       if (i==input and j%2!=0) or i+j==input+1 or j-i==input-1:
          print("*",end='')
       else:
          print(" ",end='')
   print()

