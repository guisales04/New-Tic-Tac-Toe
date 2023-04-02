from os import system
from random import randint


class Player:
    def __init__(self):
        self._player = 'X'
        self._bot = 'O'
        self._move_list = []
        self._bot_moves = []
        self._player_moves = []

    def movement(self, play: str, velha: dict) -> bool:
        if int(play) > 9:
            return False

        if velha[play] == '':
            self._player_moves.append(int(play))
            self._move_list.append(int(play))
            velha[play] = 'X'
        else:
            return False
        return True

    def validation_move(self, move: int) -> bool:
        if move in self._move_list:
            return False
        return True

    def movement_ia(self, velha: dict) -> None:
        move = randint(1, 9)
        while self.validation_move(move) is False:
            move = randint(1, 9)
        self._bot_moves.append(move)
        self._move_list.append(move)
        velha[str(move)] = 'O'


class Velha(Player):
    def __init__(self):
        super().__init__()
        self.velha = {str(x + 1): '' for x in range(9)}
        self.grid = create_grid()
        self.turno = 'p'
        self.winner = ''

    def update_grid(self) -> None:
        plays = []
        for pos, play in self.velha.items():
            if play != '':
                plays.append(play)
            else:
                plays.append(pos)
        self.grid = f'| {plays[0]} | {plays[1]} | {plays[2]} |\n' \
                    '-------------\n' \
                    f'| {plays[3]} | {plays[4]} | {plays[5]} |\n' \
                    '-------------\n' \
                    f'| {plays[6]} | {plays[7]} | {plays[8]} |\n' \


    def check_win(self) -> tuple:
        players = ((self._player_moves, 'player'), (self._bot_moves, 'bot'))
        wins = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]

        for win in wins:
            for moves in players:
                sets = set(win) & set(moves[0])
                if len(sets) == 3:
                    return (True, moves[1])
        return (False, None)


def create_grid() -> str:
    grid = '| 1 | 2 | 3 |\n' \
           '-------------\n' \
           '| 4 | 5 | 6 |\n' \
           '-------------\n' \
           '| 7 | 8 | 9 |\n' \

    return grid


game = Velha()

while True:
    system('cls')
    print(game.grid)
    if game.turno == 'p':
        play = game.movement(input('Posição da jogada: '), game.velha)
        game.update_grid()
        while play is False:
            system('cls')
            print(game.grid)
            print('\nPosição invalida!')
            play = game.movement(
                input('Posição da jogada: '), game.velha)
            game.update_grid()

    if game.turno == 'ia':
        game.movement_ia(game.velha)
        game.update_grid()

    match game.turno:
        case 'p':
            game.turno = 'ia'
        case 'ia':
            game.turno = 'p'

    win = game.check_win()
    if win[0] is True:
        if win[1] is not None:
            game.winner = win[1]
        break

system('cls')
print(game.grid)
print('VITORIA')
print(f'O {game.winner} venceu!!!!')
