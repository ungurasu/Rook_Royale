import pygame
from pygame.locals import *


class Piece(pygame.sprite.Sprite):
    def __init__(self, init_y, init_x, init_off_y, init_off_x, init_tile_size, bw, name):
        self.bw = bw
        self.x = init_x
        self.y = init_y
        self.tile_size = init_tile_size
        self.off_x = init_off_x
        self.off_y = init_off_y
        self.move = 0
        self.movedtwo = 0
        self.name = name
        self.possible_moves = list()

        super(Piece, self).__init__()
        if bw == 0:
            self.surf = pygame.image.load("images/white_"+name+".png")
        else:
            self.surf = pygame.image.load("images/black_"+name+".png")

        transparent = self.surf.get_at((0, 0))
        self.surf.set_colorkey(transparent)
        self.surf = pygame.transform.scale(self.surf, (self.tile_size, self.tile_size))
        self.rect = self.surf.get_rect()
        self.rect[0] = self.off_x+self.tile_size*(init_x-1)
        self.rect[1] = self.off_y+self.tile_size*(init_y-1)

    def move_sprite(self, move_y, move_x):
        self.x = move_x
        self.y = move_y
        self.rect[0] = self.off_x+self.tile_size*(self.x-1)
        self.rect[1] = self.off_y+self.tile_size*(self.y-1)


class Tile(pygame.sprite.Sprite):
    def __init__(self, y, x, off_y, off_x, tile_size, bw):
        self.bw = bw
        super(Tile, self).__init__()
        if bw == 0:
            self.surf = pygame.image.load("images/white_tile.png")
        else:
            self.surf = pygame.image.load("images/black_tile.png")
        self.surf = pygame.transform.scale(self.surf, (tile_size, tile_size))
        self.rect = self.surf.get_rect()
        self.rect[0] = off_x+tile_size*(x-1)
        self.rect[1] = off_y+tile_size*(y-1)


class Board:
    def __init__(self, init_off_y, init_off_x, init_tile_size, init_game_screen):
        self.off_y = init_off_y
        self.off_x = init_off_x
        self.tile_size = init_tile_size
        self.game_screen = init_game_screen
        self.player = 0
        self.selected_piece = "none"
        self.selected_y = 0
        self.selected_x = 0

        self.tiles = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.pieces = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.pieces[1][1] = Piece(1, 1, self.off_y, self.off_x, self.tile_size, 0, "rook")
        self.pieces[1][2] = Piece(1, 2, self.off_y, self.off_x, self.tile_size, 0, "horse")
        self.pieces[1][3] = Piece(1, 3, self.off_y, self.off_x, self.tile_size, 0, "bishop")
        self.pieces[1][4] = Piece(1, 4, self.off_y, self.off_x, self.tile_size, 0, "king")
        self.pieces[1][5] = Piece(1, 5, self.off_y, self.off_x, self.tile_size, 0, "queen")
        self.pieces[1][6] = Piece(1, 6, self.off_y, self.off_x, self.tile_size, 0, "bishop")
        self.pieces[1][7] = Piece(1, 7, self.off_y, self.off_x, self.tile_size, 0, "horse")
        self.pieces[1][8] = Piece(1, 8, self.off_y, self.off_x, self.tile_size, 0, "rook")
        for x in range(1, 9):
            self.pieces[2][x] = Piece(2, x, self.off_y, self.off_x, self.tile_size, 0, "pawn")

        self.pieces[8][1] = Piece(8, 1, self.off_y, self.off_x, self.tile_size, 1, "rook")
        self.pieces[8][2] = Piece(8, 2, self.off_y, self.off_x, self.tile_size, 1, "horse")
        self.pieces[8][3] = Piece(8, 3, self.off_y, self.off_x, self.tile_size, 1, "bishop")
        self.pieces[8][4] = Piece(8, 4, self.off_y, self.off_x, self.tile_size, 1, "king")
        self.pieces[8][5] = Piece(8, 5, self.off_y, self.off_x, self.tile_size, 1, "queen")
        self.pieces[8][6] = Piece(8, 6, self.off_y, self.off_x, self.tile_size, 1, "bishop")
        self.pieces[8][7] = Piece(8, 7, self.off_y, self.off_x, self.tile_size, 1, "horse")
        self.pieces[8][8] = Piece(8, 8, self.off_y, self.off_x, self.tile_size, 1, "rook")
        for x in range(1, 9):
            self.pieces[7][x] = Piece(7, x, self.off_y, self.off_x, self.tile_size, 1, "pawn")

        for y in range(1, 9):
            for x in range(1, 9):
                self.tiles[y][x] = Tile(y, x, self.off_y, self.off_x, self.tile_size, (x+y) % 2)

        try:
            self.font = pygame.font.Font("minecraftia.ttf", 16)
        except:
            self.font = pygame.font.Font(pygame.font.get_default_font(), 16)

    def blit_tiles(self):
        for y in range(1, 9):
            for x in range(1, 9):
                self.game_screen.blit(self.tiles[y][x].surf, self.tiles[y][x].rect)

    def blit_pieces(self):
        for y in range(1, 9):
            for x in range(1, 9):
                if self.pieces[y][x]:
                    self.game_screen.blit(self.pieces[y][x].surf, self.pieces[y][x].rect)

    def blit_text(self):
        if not self.player:
            img_player_surf = self.font.render("White's turn.", True, (0, 0, 0))
        else:
            img_player_surf = self.font.render("Black's turn.", True, (0, 0, 0))
        img_player_rect = img_player_surf.get_rect()
        img_player_rect[0] = self.off_x + self.tile_size*9
        img_player_rect[1] = self.off_y

        if self.selected_piece == "none":
            img_selected_piece_surf = self.font.render("No piece selected!", True, (0, 0, 0))
        else:
            img_selected_piece_surf = self.font.render("Selected {} at {}{}".format(self.selected_piece, chr(97+self.selected_x-1), self.selected_y), True, (0, 0, 0))
        img_selected_piece_rect = img_selected_piece_surf.get_rect()
        img_selected_piece_rect[0] = self.off_x + self.tile_size*9
        img_selected_piece_rect[1] = self.off_y + self.tile_size/2

        img_selected_piece_icon_surf = 0
        if self.selected_piece != "none":
            img_selected_piece_icon_surf = pygame.image.load("images/{}.png".format(self.selected_piece))
            img_selected_piece_icon_surf = pygame.transform.scale(img_selected_piece_icon_surf, (self.tile_size, self.tile_size))
            img_selected_piece_icon_surf.set_colorkey((255, 255, 255))
            img_selected_piece_icon_rect = img_selected_piece_icon_surf.get_rect()
            img_selected_piece_icon_rect[0] = self.off_x + self.tile_size*9
            img_selected_piece_icon_rect[1] = self.off_y + self.tile_size

        img_vertical_coords_surf = list()
        img_vertical_coords_rect = list()
        for i in range(0, 8):
            img_vertical_coords_surf.append(self.font.render("{}".format(i+1), True, (0, 0, 0)))
            img_vertical_coords_rect.append(img_vertical_coords_surf[i].get_rect())
            img_vertical_coords_rect[i][0] = self.off_x/2
            img_vertical_coords_rect[i][1] = self.off_y*1.35 + self.tile_size*i

        img_horizontal_coords_surf = list()
        img_horizontal_coords_rect = list()
        for i in range(0, 8):
            img_horizontal_coords_surf.append(self.font.render("{}".format(chr(97+i)), True, (0, 0, 0)))
            img_horizontal_coords_rect.append(img_horizontal_coords_surf[i].get_rect())
            img_horizontal_coords_rect[i][0] = self.off_x*1.45 + self.tile_size*i
            img_horizontal_coords_rect[i][1] = self.off_y+ self.tile_size * 8

        self.game_screen.blit(img_player_surf, img_player_rect)
        self.game_screen.blit(img_selected_piece_surf, img_selected_piece_rect)
        if img_selected_piece_icon_surf:
            self.game_screen.blit(img_selected_piece_icon_surf, img_selected_piece_icon_rect)
        for i in range(0, 8):
            self.game_screen.blit(img_vertical_coords_surf[i], img_vertical_coords_rect[i])
        for i in range(0, 8):
            self.game_screen.blit(img_horizontal_coords_surf[i], img_horizontal_coords_rect[i])

    def blit_board(self):
        self.blit_tiles()
        self.blit_pieces()
        self.blit_text()

    def click_on_board_coords(self, y, x):
        if y < self.off_y or x < self.off_x or y > self.off_y+8*self.tile_size or x > self.off_x+8*self.tile_size:
            return 0
        else:
            return [int((y-self.off_y)/self.tile_size+1), int((x-self.off_x)/self.tile_size+1)]

    def within_board(self, coords):
        if 1 <= coords[0] and coords[0] <= 8 and 1 <= coords[1] and coords[1] <= 8:
            return True
        else:
            return False

    def eat_piece(self, y, x):
        if self.pieces[y][x]:
            print("ate bw {} {} at {}{}".format(self.pieces[y][x].bw, self.pieces[y][x].name, chr(97+x-1), y))
            self.pieces[y][x] = 0

    def generate_piece_possible_moves(self, y, x):
        if self.selected_piece != "none":
            self.pieces[y][x].possible_moves = list()
            if self.pieces[y][x].name == "pawn":
                if not self.pieces[y][x].bw:
                    if self.within_board((y+1, x)) and not self.pieces[y+1][x]:
                        self.pieces[y][x].possible_moves.append((y+1, x))
                    if self.within_board((y+2, x)) and self.pieces[y][x].move == 0 and not self.pieces[y+2][x]:
                        self.pieces[y][x].possible_moves.append((y+2, x))
                    if self.within_board((y+1, x-1)) and ((self.pieces[y+1][x-1] and self.pieces[y+1][x-1].bw != self.pieces[y][x].bw) or (self.pieces[y][x-1] and self.pieces[y][x-1].bw != self.pieces[y][x].bw and self.pieces[y][x-1].move == 1 and self.pieces[y][x-1].movedtwo and self.pieces[y][x-1].name == "pawn")):
                        self.pieces[y][x].possible_moves.append((y+1, x-1))
                    if self.within_board((y+1, x+1)) and ((self.pieces[y+1][x+1] and self.pieces[y+1][x+1].bw != self.pieces[y][x].bw) or (self.pieces[y][x+1] and self.pieces[y][x+1].bw != self.pieces[y][x].bw and self.pieces[y][x+1].move == 1 and self.pieces[y][x+1].movedtwo and self.pieces[y][x+1].name == "pawn")):
                        self.pieces[y][x].possible_moves.append((y+1, x+1))
                else:
                    if self.within_board((y-1, x)) and not self.pieces[y-1][x]:
                        self.pieces[y][x].possible_moves.append((y-1, x))
                    if self.within_board((y-2, x)) and self.pieces[y][x].move == 0 and not self.pieces[y-2][x]:
                        self.pieces[y][x].possible_moves.append((y-2, x))
                    if self.within_board((y-1, x-1)) and ((self.pieces[y-1][x-1] and self.pieces[y-1][x-1].bw != self.pieces[y][x].bw) or (self.pieces[y][x-1] and self.pieces[y][x-1].bw != self.pieces[y][x].bw and self.pieces[y][x-1].move == 1 and self.pieces[y][x-1].movedtwo and self.pieces[y][x-1].name == "pawn")):
                        self.pieces[y][x].possible_moves.append((y-1, x-1))
                    if self.within_board((y-1, x+1)) and ((self.pieces[y-1][x+1] and self.pieces[y-1][x+1].bw != self.pieces[y][x].bw) or (self.pieces[y][x+1] and self.pieces[y][x+1].bw != self.pieces[y][x].bw and self.pieces[y][x+1].move == 1 and self.pieces[y][x+1].movedtwo and self.pieces[y][x+1].name == "pawn")):
                        self.pieces[y][x].possible_moves.append((y-1, x+1))
            elif self.pieces[y][x].name == "horse":
                if self.within_board((y-2, x-1)) and (not self.pieces[y-2][x-1] or (self.pieces[y-2][x-1] and self.pieces[y-2][x-1].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y-2, x-1))
                if self.within_board((y-2, x+1)) and (not self.pieces[y-2][x+1] or (self.pieces[y-2][x+1] and self.pieces[y-2][x+1].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y-2, x+1))
                if self.within_board((y+2, x-1)) and (not self.pieces[y+2][x-1] or (self.pieces[y+2][x-1] and self.pieces[y+2][x-1].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y+2, x-1))
                if self.within_board((y+2, x+1)) and (not self.pieces[y+2][x+1] or (self.pieces[y+2][x+1] and self.pieces[y+2][x+1].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y+2, x+1))
                if self.within_board((y-1, x-2)) and (not self.pieces[y-1][x-2] or (self.pieces[y-1][x-2] and self.pieces[y-1][x-2].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y-1, x-2))
                if self.within_board((y-1, x+2)) and (not self.pieces[y-1][x+2] or (self.pieces[y-1][x+2] and self.pieces[y-1][x+2].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y-1, x+2))
                if self.within_board((y+1, x-2)) and (not self.pieces[y+1][x-2] or (self.pieces[y+1][x-2] and self.pieces[y+1][x-2].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y+1, x-2))
                if self.within_board((y+1, x+2)) and (not self.pieces[y+1][x+2] or (self.pieces[y+1][x+2] and self.pieces[y+1][x+2].bw != self.pieces[y][x].bw)):
                    self.pieces[y][x].possible_moves.append((y+1, x+2))
            print(self.pieces[y][x].possible_moves)

    def attempt_move(self, y, x):
        print("y: {} x: {} selected_y: {} selected_x: {}".format(y, x, self.selected_y, self.selected_x))
        if self.pieces[self.selected_y][self.selected_x].possible_moves.count((y, x)):
            self.pieces[self.selected_y][self.selected_x].move += 1
            if self.pieces[self.selected_y][self.selected_x].name == "pawn":
                if y == self.selected_y + 2:
                    self.pieces[self.selected_y][self.selected_x].movedtwo = 1
                if x == self.selected_x+1 and self.pieces[self.selected_y][self.selected_x+1] and self.pieces[self.selected_y][self.selected_x+1].name == "pawn" and self.pieces[self.selected_y][self.selected_x+1].bw != self.pieces[self.selected_y][self.selected_x].bw and self.pieces[self.selected_y][self.selected_x+1].move == 1 and self.pieces[self.selected_y][self.selected_x+1].movedtwo:
                    self.eat_piece(self.selected_y, self.selected_x+1)
                if x == self.selected_x-1 and self.pieces[self.selected_y][self.selected_x-1] and self.pieces[self.selected_y][self.selected_x-1].name == "pawn" and self.pieces[self.selected_y][self.selected_x-1].bw != self.pieces[self.selected_y][self.selected_x].bw and self.pieces[self.selected_y][self.selected_x-1].move == 1 and self.pieces[self.selected_y][self.selected_x-1].movedtwo:
                    self.eat_piece(self.selected_y, self.selected_x-1)
            if self.pieces[y][x]:
                self.eat_piece(y, x)
            self.pieces[self.selected_y][self.selected_x].move_sprite(y, x)
            self.pieces[y][x] = self.pieces[self.selected_y][self.selected_x]
            self.pieces[self.selected_y][self.selected_x] = 0

            #remove wasted en passant privilege
            for iy in range(1, 9):
                for ix in range(1, 9):
                    if self.pieces[iy][ix] and self.pieces[iy][ix].bw != self.player:
                        self.pieces[iy][ix].movedtwo = 0

            self.player = not self.player
            self.selected_piece = "none"
        else:
            print("bad move!")

    def attempt_select(self, y, x):
        if self.within_board((y,x)) and self.pieces[y][x] and self.pieces[y][x].bw == self.player:
            print("selected valid piece y {} x {} bw {} name {}".format(y, x, self.player, self.pieces[y][x].name))
            if not self.player:
                self.selected_piece = "white_" + self.pieces[y][x].name
            else:
                self.selected_piece = "black_" + self.pieces[y][x].name
            self.selected_y = y
            self.selected_x = x
            self.generate_piece_possible_moves(y, x)
        else:
            self.selected_piece = "none"
            print("nothing or bad select at y:{} x:{}".format(y, x))

    def click_event(self):
        mouse = [pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0]]

        if self.click_on_board_coords(mouse[0], mouse[1]):
            coords = self.click_on_board_coords(mouse[0], mouse[1])
            if self.selected_piece == "none":
                self.attempt_select(coords[0], coords[1])
            else:
                self.attempt_move(coords[0], coords[1])
        else:
            self.selected_piece = "none"

    def unclick_event(self):
        self.selected_piece = "none"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("white_rook.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


pygame.init()

pygame.display.set_caption('Rook Royale')
icon = pygame.image.load("images/white_king.png")
icon.set_colorkey((255, 255, 255))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

board = Board(50, 50, 50, screen)
clicked = 0
unclicked = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    if pygame.mouse.get_pressed(3)[0] and not clicked:
        #print("click on screen {} on board {}".format(pygame.mouse.get_pos(),board.click_on_board_coords(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])))
        board.click_event()
        clicked = 1
    elif not pygame.mouse.get_pressed(3)[0] and clicked:
        clicked = 0

    if pygame.mouse.get_pressed(3)[2] and not unclicked:
        board.unclick_event()
        unclicked = 1
    elif not pygame.mouse.get_pressed(3)[2] and unclicked:
        unclicked = 0

    board.blit_board()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
