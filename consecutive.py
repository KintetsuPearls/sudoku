lines_beside = [
  [1,0,1,0,1,0,0,1],
  [1,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0],
  [0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,1],
  [0,0,1,0,0,1,0,0],
  [0,1,0,1,0,0,0,0],
  ]

lines_vertical = [
  [0,0,1,1,0,1,0,0,0],
  [1,1,0,0,1,1,0,1,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,1,0,1,0,0,0],
  [0,0,1,0,1,1,0,0,0],
  [0,1,0,0,0,0,1,1,0],
  [0,0,0,1,0,1,0,0,0],
  [1,1,0,0,1,0,0,1,1],
  ]

def check(i,j,number):
  #(i,j)にnumberが入ったときにルールを満たしているかのチェック
  for x in range(num):
    if board[x][j] == number:
      return False

  for y in range(num):
    if board[i][y] == number:
      return False
    
  if i != 0:
    if board[i-1][j] != 0:
      if lines_vertical[i-1][j] == 0:
        if abs(board[i-1][j]-number) <= 1:
          return False 
      else:
        if abs(board[i-1][j]-number) > 1:
          return False
  
  if i != num-1:
    if board[i+1][j] != 0:
      if lines_vertical[i][j] == 0:
        if abs(board[i+1][j]-number) <= 1:
          return False 
      else:
        if abs(board[i+1][j]-number) > 1:
          return False

  if j != 0:
    if board[i][j-1] != 0:
      if lines_beside[i][j-1] == 0:
        if abs(board[i][j-1]-number) <= 1:
          return False 
      else:
        if abs(board[i][j-1]-number) > 1:
          return False

  if j != num-1:
    if board[i][j+1] != 0:
      if lines_beside[i][j] == 0:
        if abs(board[i][j+1]-number) <= 1:
          return False 
      else:
        if abs(board[i][j+1]-number) > 1:
          return False

  block_i = (i // block) * block
  block_j = (j // block) * block

  for x in range(block):
    for y in range(block):
      if board[block_i + x][block_j + y] == number:
        return False

  return True
