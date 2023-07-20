#数独の大きさ
num = 9 
#ブロックのサイズ
block = 3

#マスの初期配置 0は空欄
board = [
  [0,8,0,0,0,0,0,0,0],
  [4,0,2,0,0,1,0,0,0],
  [9,0,0,0,0,0,5,7,0],
  [0,0,0,8,0,4,0,0,0],
  [0,7,0,0,3,0,9,0,0],
  [0,0,1,2,0,0,0,3,0],
  [8,0,0,0,0,0,0,1,3],
  [0,0,3,0,8,6,0,0,0],
  [0,0,9,0,0,0,0,0,0]
]

def check(i,j,number):
  #(i,j)にnumberが入ったときにルールを満たしているかのチェック
  for x in range(num):
    if board[x][j] == number:
      return False

  for y in range(num):
    if board[i][y] == number:
      return False

  block_i = (i // block) * block
  block_j = (j // block) * block

  for x in range(block):
    for y in range(block):
      if board[block_i + x][block_j + y] == number:
        return False

  return True

def put(i,j,number):
  flag = False

  if board[i][j] != number:
    if board[i][j] != 0:
      return False

    if check(i,j,number) == False:
      return False
    if board[i][j] == 0:
      board[i][j] = number
  else:
    flag = True

  if i == num-1 and j == num-1:
    show()
    exit()

  else:
    if j+1 >= num:
      nexj = 0
      nexi = i+1
    else:
      nexj = j+1
      nexi = i

    for nex in range(1,num+1):
      put(nexi,nexj,nex)
  if flag == False:
    board[i][j] = 0

  return True

def start():
  for nex in range(1,num+1):
    put(0,0,nex)

def show():
  for row in board:
    print(*row)
  print()

def main():
  start()


if __name__ == '__main__':
  main()
