#数独の大きさ
num = 9 
#ブロックのサイズ
block = 3

#マスの初期配置 0は空欄
board = [
  [8,0,0,0,0,0,0,0,0],
  [0,0,3,6,0,0,0,0,0],
  [0,7,0,0,9,0,2,0,0],
  [0,5,0,0,0,7,0,0,0],
  [0,0,0,0,4,5,7,0,0],
  [0,0,0,1,0,0,0,3,0],
  [0,0,1,0,0,0,0,6,8],
  [0,0,8,5,0,0,0,1,0],
  [0,9,0,0,0,0,4,0,0]
]

ans = 0

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
  if board[i][j] != number:
    if board[i][j] != 0:
      return False

    if check(i,j,number) == False:
      return False

    board[i][j] = number

  if i == num-1 and j == num-1:
    global ans
    ans += 1
    show()

  else:
    if j+1 >= num:
      nexj = 0
      nexi = i+1
    else:
      nexj = j+1
      nexi = i

    for nex in range(1,num+1):
      put(nexi,nexj,nex)

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
  print(ans)

if __name__ == '__main__':
  main()
