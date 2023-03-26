import chess
import chess.engine
import pygame
import os
import time

pygame.init()

d = "tatiana"
piece_images = []
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        piece_images.append(full_path)

 
board_size = 560
square_size = board_size / 8


def generate_chess_squares():
    board_rect_list = []
    for file in range(8):

        for rank in range(8):

            if file % 2 == rank % 2:
                colour = pygame.color.Color(222,227,230, 255)
            else:
                colour = pygame.color.Color(140,162,173, 255)

            rect = pygame.rect.Rect(200 + rank * square_size, 0 + file * square_size, square_size, square_size)
            board_rect_list.append([rect, colour])
    return board_rect_list

class base_piece(pygame.sprite.Sprite):
    def __init__(self, image_path, start_pos, colour) -> None:
        super().__init__()
        self.colour = colour
        self.image = pygame.image.load(image_path)
      
        self.image = pygame.transform.smoothscale(self.image, (square_size, square_size))
        self.rect = self.image.get_rect(topleft=start_pos)


class rook(base_piece):
    def __init__(self, black, start_pos) -> None:
        self.id = id
        if black:
            path = r"tatiana/bR.svg"
        else:
            path = r"tatiana/wR.svg"
        super().__init__(path, start_pos, black)
    def update(self):
        pass
        
class pawn(base_piece):
    def __init__(self, black, start_pos) -> None:
        if black:
            path = r"tatiana/bP.svg"
        else:
            path = r"tatiana/wP.svg"
        super().__init__(path, start_pos, black)

class bishop(base_piece):
    def __init__(self, black, start_pos) -> None:
        if black:
            path = r"tatiana/bB.svg"
        else:
            path = r"tatiana/wB.svg"
        super().__init__(path, start_pos, colour)

class queen(base_piece):
    def __init__(self, black, start_pos) -> None:
        if black:
            path = r"tatiana/bQ.svg"
        else:
            path = r"tatiana/wQ.svg"
        super().__init__(path, start_pos, colour)
class king(base_piece):
    def __init__(self, black, start_pos) -> None:
        if black:
            path = r"tatiana/bK.svg"
        else:
            path = r"tatiana/wK.svg"
        super().__init__(path, start_pos, colour)
class knight(base_piece):
    def __init__(self, black, start_pos) -> None:
        if black:
            path = r"tatiana/bN.svg"
        else:
            path = r"tatiana/wN.svg"
        super().__init__(path, start_pos, colour)

width = 1920 / 2
height = 560
window = pygame.display.set_mode(size=(width, height))
quit = False
engine = chess.engine.SimpleEngine.popen_uci(r"stockfish_15.1_linux_x64_avx2/stockfish-ubuntu-20.04-x86-64-avx2")
engine.configure({"Skill Level": 10})
board = chess.Board()
chess_squares = generate_chess_squares()

piece_group = pygame.sprite.Group()

for square_index in board.piece_map():

        piece = board.piece_map()[square_index]
        name = chess.piece_name(piece.piece_type)
        colour = piece.color
        if name == "rook":
            piece_group.add(rook(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
        if name == "bishop":

            piece_group.add(bishop(black=piece.color, start_pos=chess_squares[square_index][0].topleft))

        if name == "pawn":          
            piece_group.add(pawn(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
        if name == 'king':
            piece_group.add(king(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
        if name == 'queen':
            piece_group.add(queen(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
        if name == 'knight':
            piece_group.add(knight(black=piece.color, start_pos=chess_squares[square_index][0].topleft))

# for index, square in enumerate(chess_squares):
#     if index % 2 == 0:
#         piece_group.add(pawn(colour="white", start_pos=square[0].topleft))
#     else:
#         piece_group.add(pawn(colour="black", start_pos=square[0].topleft))
while not board.is_game_over() and not quit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    window.fill(pygame.color.Color(22,21,18, 255))
    for square in chess_squares:
        pygame.draw.rect(window, square[1], square[0])
    piece_group.empty()
    for square_index in board.piece_map():

            piece = board.piece_map()[square_index]
            name = chess.piece_name(piece.piece_type)
            colour = piece.color
            if name == "rook":
                piece_group.add(rook(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
            if name == "bishop":

                piece_group.add(bishop(black=piece.color, start_pos=chess_squares[square_index][0].topleft))

            if name == "pawn":          
                piece_group.add(pawn(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
            if name == 'king':
                piece_group.add(king(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
            if name == 'queen':
                piece_group.add(queen(black=piece.color, start_pos=chess_squares[square_index][0].topleft))
            if name == 'knight':
                piece_group.add(knight(black=piece.color, start_pos=chess_squares[square_index][0].topleft))

    piece_group.draw(window)
    pygame.display.update()
    result = engine.play(board, chess.engine.Limit(2))
    board.push(result.move)
    print(result.move)
    
    print(board)
    print("")
    if board.is_game_over():
        time.sleep(10)

engine.quit()