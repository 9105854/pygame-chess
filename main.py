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
animating = False


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
    def __init__(self, image_path, colour, square_id) -> None:
        super().__init__()
        self.square_id = square_id
        self.target_id = self.square_id
        self.colour = colour
        self.image = pygame.image.load(image_path)
      
        self.image = pygame.transform.smoothscale(self.image, (square_size, square_size))
        self.rect = self.image.get_rect(topleft=chess_squares[self.square_id][0].topleft)
    def update(self):
        global animating
        if self.target_id != self.square_id:
            animating = True
            current_pos = pygame.math.Vector2(self.rect.left, self.rect.top)
            target_pos = pygame.math.Vector2(chess_squares[self.target_id][0].left, chess_squares[self.target_id][0].top)
            original_pos = pygame.math.Vector2(chess_squares[self.square_id][0].left, chess_squares[self.square_id][0].top)
            original_distance = pygame.math.Vector2.distance_to(original_pos, target_pos) 
            distance = pygame.math.Vector2.distance_to(current_pos, target_pos) 
            if abs(distance) < 10:
                self.rect.topleft = (target_pos.x, target_pos.y)
                for sprite in piece_group:
                    if self.target_id == sprite.square_id:
                        sprite.kill()
                self.square_id = self.target_id
                animating = False
            else:
                new_pos = pygame.math.Vector2.move_towards(current_pos, target_pos, (original_distance / distance) * 5)
                self.rect.topleft = (new_pos.x, new_pos.y)
            print(distance)

class rook(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bR.svg"
        else:
            path = r"tatiana/wR.svg"
        super().__init__(path, black, square_id)

        
class pawn(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bP.svg"
        else:
            path = r"tatiana/wP.svg"
        super().__init__(path, black, square_id)

class bishop(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bB.svg"
        else:
            path = r"tatiana/wB.svg"
        super().__init__(path, colour, square_id)

class queen(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bQ.svg"
        else:
            path = r"tatiana/wQ.svg"
        super().__init__(path, colour, square_id)
class king(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bK.svg"
        else:
            path = r"tatiana/wK.svg"
        super().__init__(path, colour, square_id)
class knight(base_piece):
    def __init__(self, black, square_id) -> None:
        if black:
            path = r"tatiana/bN.svg"
        else:
            path = r"tatiana/wN.svg"
        super().__init__(path, colour, square_id)

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
            piece_group.add(rook(black=piece.color, square_id=square_index))
        if name == "bishop":

            piece_group.add(bishop(black=piece.color, square_id=square_index))

        if name == "pawn":          
            piece_group.add(pawn(black=piece.color, square_id=square_index))
        if name == 'king':
            piece_group.add(king(black=piece.color, square_id=square_index))
        if name == 'queen':
            piece_group.add(queen(black=piece.color, square_id=square_index))
        if name == 'knight':
            piece_group.add(knight(black=piece.color, square_id=square_index))

# for index, square in enumerate(chess_squares):
#     if index % 2 == 0:
#         piece_group.add(pawn(colour="white", start_pos=square[0].topleft))
#     else:
#         piece_group.add(pawn(colour="black", start_pos=square[0].topleft))
fps = pygame.time.Clock()
while not board.is_game_over() and not quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    window.fill(pygame.color.Color(22,21,18, 255))
    for square in chess_squares:
        pygame.draw.rect(window, square[1], square[0])
    # piece_group.empty()
    # for square_index in board.piece_map():

    #         piece = board.piece_map()[square_index]
    #         name = chess.piece_name(piece.piece_type)
    #         colour = piece.color
    #         if name == "rook":
    #             piece_group.add(rook(black=piece.color, square_id=square_index))
    #         if name == "bishop":

    #             piece_group.add(bishop(black=piece.color, square_id=square_index))

    #         if name == "pawn":          
    #             piece_group.add(pawn(black=piece.color, square_id=square_index))
    #         if name == 'king':
    #             piece_group.add(king(black=piece.color, square_id=square_index))
    #         if name == 'queen':
    #             piece_group.add(queen(black=piece.color, square_id=square_index))
    #         if name == 'knight':
    #             piece_group.add(knight(black=piece.color, square_id=square_index))
    if not animating:
        result = engine.play(board, chess.engine.Limit(.5))
        board.push(result.move)
        
        initial_square = str(result.move)[0:2]
        initial_square_id = chess.parse_square(initial_square)
        final_square = str(result.move)[2:4]
        final_square_id = chess.parse_square(final_square)
        print(final_square_id)
        print(initial_square_id)
        for sprite in piece_group:
            if sprite.square_id == initial_square_id:
                print('gotcha')
                sprite.target_id = final_square_id
                if sprite.__class__.__name__ == "king":
                    if initial_square_id - final_square_id == 2:
                        print('castle detected')
                        for sprite in piece_group:
                            if sprite.square_id == final_square_id + 1: 
                                print('rooky rooky')

                                sprite.target_id = final_square_id
                    elif initial_square_id - final_square_id == -2:
                        print('different castle detected')
                        for sprite in piece_group:
                            if sprite.square_id == final_square_id + 1:
                                print('drooakaf aoerfadf')
                                sprite.target_id = final_square_id - 1

    

        # animating = True
        print(board)
        print("")
        
    piece_group.update()
    piece_group.draw(window)
    pygame.display.update()
    if board.is_game_over():
        time.sleep(10)
    fps.tick(144)

engine.quit()
