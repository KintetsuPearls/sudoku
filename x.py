def check(i,j,number):
  #(i,j)にnumberが入ったときにルールを満たしているかのチェック
  for x in range(num):
    if board[x][j] == number:
      return False

  for y in range(num):
    if board[i][y] == number:
      return False
  if i == j:
    for k in range(num):
      if board[k][k] == number:
        return False
  
  if i+j == num-1:
    for k in range(num):
      if board[k][num-1-k] == number:
        return False

  block_i = (i // block) * block
  block_j = (j // block) * block

  for x in range(block):
    for y in range(block):
      if board[block_i + x][block_j + y] == number:
        return False

  return True
