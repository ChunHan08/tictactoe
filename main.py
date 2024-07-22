def TicTacToe():
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")

TicTacToe();
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def PrintBoard():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print(board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print(board[6], "|", board[7], "|", board[8])
    print()
PrintBoard()
TicTacToe()

def GetNumber():
  while True:
    number = input()
try:
  number int(number)
  if number not in range(1, 10):
    return number 
  else:
    print("\nNumber not on board")
except ValueError:
    print("\nThats not a number. Try again!")
    continue

end = False 

while not end:
  PrintBoard()
  end = CheckWin("o")
  if end == True:
    break
  print("Chose a box player X")
  Turn("X")
 
  PrintBoard
  end = checkWin("X")
  if end == True:
    break
  print("Choose a box player o")
Turn("o")

MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]

def CheckWin(player):
  count = 0
  for x in range(9):
    for y in range(9):
      for z in range(9):
        if x != y and y != z and z != x:
          if board[x] == player and board[y] == player and board[z] == player:
            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
              print("player", player, "wins!\n")
              return True
  
    for a in range(9):
      if board[a] =="X" or board[a] == "o":
        count += 1
    
      if count == 9:
        print("The game ends in a tie\n")
        return True

def Turn(player):
  placing_index = GetNumber() - 1
  if board[placing_index] == "X" or board[placing_index] == "o":
    print("\nBox already taken, try another one")
    Turn(player)
  else:
    board[placing_index] = player
  
      
          