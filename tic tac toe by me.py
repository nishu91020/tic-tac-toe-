
#tic tac toe

def display_board(board):
    for row in board:
        print()
        for col in row:
            print(col, end=' ')
    print()
def update_board(board,r,c,sym):
    if r>=len(board[r]) or r<0:
        return False
    elif c>=len(board[r]) or c<0:
        return False
    elif board[r][c] !='[ ]':
        return False
    board[r][c]='['+sym+']'
    return True
def isfull(board):
    for row in board:
        for col in row:
            if col=='[ ]':
                return False
    return True

def iswin(board,sym ):
    sym='['+sym+']'
    i=0
    while i<3:
        if board[i][0]==sym and board[i][1]==sym and board[i][2]==sym:
            return True
        i+=1
    i=0
    while i<3:
        if board[0][i]==sym and board[1][i]==sym and board[2][i]==sym:
            return True
        i+=1
        if board[0][0]==sym and board[1][1]==sym and board[2][2]==sym:
            return True
        if board[0][2]==sym and board[1][1]==sym and board[2][0]==sym:
            return True
    return False

def tic_tac_toe():
    board=[ ['[ ]']*3,['[ ]']*3,['[ ]']*3]
    player=[]
    symbol=['X','O']
    player.append(input("enter name of player 1"))
    player.append(input("enter name of player 2"))

    i=0
    while i<2:
        print('symbol of',player[i],'is',symbol[i])
        i+=1
    i=0
    flag=1
    while not isfull(board):
        display_board(board)
        print(player[i],"with symbol[",symbol[i],'] plays')
        r = int(input("enter row(0 to2):"))
        c = int(input("enter col(0 to2):"))
        if update_board(board,r,c,symbol[i]):
            if iswin(board,symbol[i]):
                display_board(board)
                print (player[i],'with symbol[',symbol[i],'] wins')
                flag=0
                break
            i=(i+1)%2
        else:
            print('invalid move')
    if flag==1:
        print('game draw')
        display_board(board)



def main():
    print('tic tac toe game')
    tic_tac_toe()
main()


