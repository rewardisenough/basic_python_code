arr = [[1,2,5,7,8],[10,3,4,6,9],[11,12,13,14,15],[25,22,20,19,16],[24,23,21,18,17]]


# len(arr) = number of rows
# len(arr[0]) = number of columns

def check(x,y,arr):
  if(arr[x][y]==(len(arr) * len(arr[0]))):
    return
  if(y>0): # check left
    if(arr[x][y]+1==arr[x][y-1]):
      return
  if(y<len(arr[0])-1): # check right
    if(arr[x][y]+1==arr[x][y+1]):
      return
  if(x>0): # check up
    if(arr[x][y]+1==arr[x-1][y]):
      return
  if(x<len(arr)-1): # check down
    if(arr[x][y]+1==arr[x+1][y]):
      return
  return arr[x][y]
  



output_arr = []
for i in range(len(arr)):
  for k in range(len(arr[0])):
    if(check(i,k,arr)!=None): # python returns none if returned blank.
      output_arr.append(check(i,k,arr))

output_str = ""
output_str += f"INCORRECT: {len(output_arr)} "
output_str += str(tuple(output_arr))

print(output_str)



# if(y>0):
#   check left
# if(y<column.length):
#   check right
# if(x>0):
#   check up
# if(x+1<row.length):
#   check down
