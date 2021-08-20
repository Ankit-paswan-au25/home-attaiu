#matrix
#two ways to create matrix 1 with comprehensive loop (loop in one line)
#2 with normal loop
"""matrix is a collection of list of equal length"""
#matrix with normal loop
#usrip=int(input("enter  value of row"))
#usrip1=int(input("enter value of column"))
row = int(input("Enter the number of rows:"))   
column = int(input("Enter the number of columns:"))   
  
# Initialize empty matrix   
matrix = []   
print("Enter the entries row wise:")   
  
# For user input   
for i in range(row):       # A outer for loop for row entries   
   a =[]   
   for j in range(column):     # A inner for loop for column entries   
      a.append(int(input()))   
   matrix.append(a)   
  
# For printing the matrix   
for i in range(row):   
   for j in range(column):   
      print(matrix[i][j], end = " ")   
   print()   
