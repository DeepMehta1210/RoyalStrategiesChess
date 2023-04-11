class chess():
    pieases={"white":"◻","w_king":"\u2654","w_queen":"\u2655","w_rook":"\u2656","w_bishop":"\u2657","w_knight":"\u2658","w_pawn":"\u2659",
                 "black":"◼","b_king":"\u265A","b_queen":"\u265B","b_rook":"\u265C","b_bishop":"\u265D","b_knight":"\u265E","b_pawn":"\u265F"}  
    board=[
        [f'{pieases["b_rook"]}',f'{pieases["b_knight"]}',f'{pieases["b_bishop"]}',f'{pieases["b_queen"]}',f'{pieases["b_king"]}',f'{pieases["b_bishop"]}',f'{pieases["b_knight"]}',f'{pieases["b_rook"]}'],
        [f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}',f'{pieases["b_pawn"]}'],
        [f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}'],
        [f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}'],
        [f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}'],
        [f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}',f'{pieases["black"]}',f'{pieases["white"]}'],
        [f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}',f'{pieases["w_pawn"]}'],
        [f'{pieases["w_rook"]}',f'{pieases["w_knight"]}',f'{pieases["w_bishop"]}',f'{pieases["w_queen"]}',f'{pieases["w_king"]}',f'{pieases["w_bishop"]}',f'{pieases["w_knight"]}',f'{pieases["w_rook"]}']
    ]
    def __init__(self):
        self.Player_One = input("Enter a Name Of First Player : ")
        self.player_Two=input("Enter a Name of Second Player : ")
        self.game_board = chess.board
        for i in self.game_board:
            for j in i:
                print(j,end=' ')
            print()

        self.game_start()

    def print_board(self,board:list,moveFrom: str,moveTo:str):
        self.col=["a","b","c","d","e","f","g","h"]
        self.row=[1,2,3,4,5,6,7,8]
        pieace_1=board[int(moveTo[1])-1][self.col.index(moveTo[0])]
        pieace_2=board[int(moveFrom[1])-1][self.col.index(moveFrom[0])]
        if pieace_1 in [f'{chess.pieases["white"]}',f'{chess.pieases["black"]}']:
            pass
        elif pieace_2 in [f'{chess.pieases["white"]}',f'{chess.pieases["black"]}']:
            pass
        else:
            pass
        return board
    def game_start(self):
         self.turn=self.Player_One
         while True:
            if self.turn==self.Player_One:
                move_from=input(f"{self.turn} which pieace you want to move : ")
                move_to=input(f"{self.turn} where you want to move : ")
                self.turn=self.player_Two
            else:
                move_from=input(f"{self.turn} which pieace you want to move : ")
                move_to=input(f"{self.turn} where you want to move : ")
                # print(self.print_board(board=self.game_board,moveFrom=move_from,moveTo=move_to))
                self.turn=self.Player_One
            self.game_board=self.print_board(board=self.game_board,moveFrom=move_from,moveTo=move_to)
            for i in self.game_board:
                for j in i:
                    print(j,end=' ')
                print()
game=chess()