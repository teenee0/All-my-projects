class Figure:
    symbols = ''

    def get_symbols(self):
        return self.symbols


class PawnWhite(Figure):

    def __init__(self):
        self.symbols = 'p'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if i == 6 and field[i - 2][j] == '#' and field[i - 1][j] == '#':
            arr_ret.add((i - 1, j))
            arr_ret.add((i - 2, j))
        elif i == 6 and field[i - 1][j] == '#':
            arr_ret.add((i - 1, j))
        if j > 0 and field[i - 1][j - 1] in list('PRNBQK'):
            arr_ret.add((i - 1, j - 1))
        if j < 7 and field[i - 1][j + 1] in list('PRNBQK'):
            arr_ret.add((i - 1, j + 1))

        if i != 0 and field[i - 1][j] == '#':
            arr_ret.add((i - 1, j))


            
        global last_movies
        if i == 3 and last_movies[-1][0][1] == '7' and last_movies[-1][1][1] == '5' and list('ABCDEFGH').index(last_movies[-1][0][0].upper()) in [j+1, j-1]:
            arr_ret.add((i-1,  list('ABCDEFGH').index(last_movies[-1][0][0].upper()), 'p'))
        return list(arr_ret)


class PawnBlack(Figure):

    def __init__(self):
        self.symbols = 'P'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if i == 1 and field[i + 2][j] == '#' and field[i + 1][j] == '#':
            arr_ret.add((i + 1, j))
            arr_ret.add((i + 2, j))
        elif i == 1 and field[i + 1][j] == '#':
            arr_ret.add((i + 1, j))
        if j > 0 and field[i + 1][j - 1] in list('prnbqk'):
            arr_ret.add((i + 1, j - 1))
        if j < 7 and field[i + 1][j + 1] in list('prnbqk'):
            arr_ret.add((i + 1, j + 1))
        if i != 0 and field[i + 1][j] == '#':
            arr_ret.add((i + 1, j))

        global last_movies
        if i == 4 and last_movies[-1][0][1] == '2' and last_movies[-1][1][1] == '4' and list('ABCDEFGH').index(last_movies[-1][0][0].upper()) in [j+1, j-1]:
            arr_ret.add((i+1,  list('ABCDEFGH').index(last_movies[-1][0][0].upper()), 'P'))

        return list(arr_ret)


class RookWhite(Figure):

    def __init__(self):
        self.symbols = 'r'

    def get_all_movies(self, i_ind, j_ind, field):
        arr_ret = set()

        for i in range(i_ind + 1, 8):
            if field[i][j_ind] == '#':
                arr_ret.add((i, j_ind))
            else:
                if field[i][j_ind] in list('PRHEQK'):
                    arr_ret.add((i, j_ind))
                break

        for i in range(i_ind - 1, -1, -1):
            if field[i][j_ind] == '#':
                arr_ret.add((i, j_ind))
            else:
                if field[i][j_ind] in list('PRHEQK'):
                    arr_ret.add((i, j_ind))
                break

        for j in range(j_ind + 1, 8):
            if field[i_ind][j] == '#':
                arr_ret.add((i_ind, j))
            else:
                if field[i_ind][j] in list('PRHEQK'):
                    arr_ret.add((i_ind, j))
                break

        for j in range(j_ind - 1, -1, -1):
            if field[i_ind][j] == '#':
                arr_ret.add((i_ind, j))
            else:
                if field[i_ind][j] in list('PRHEQK'):
                    arr_ret.add((i_ind, j))
                break

        return list(arr_ret)


class RookBlack(Figure):

    def __init__(self):
        self.symbols = 'R'

    def get_all_movies(self, i_ind, j_ind, field):
        arr_ret = set()

        for i in range(i_ind + 1, 8):
            if field[i][j_ind] == '#':
                arr_ret.add((i, j_ind))
            else:
                if field[i][j_ind] in list('prheqk'):
                    arr_ret.add((i, j_ind))
                break

        for i in range(i_ind - 1, -1, -1):
            if field[i][j_ind] == '#':
                arr_ret.add((i, j_ind))
            else:
                if field[i][j_ind] in list('prheqk'):
                    arr_ret.add((i, j_ind))
                break

        for j in range(j_ind + 1, 8):
            if field[i_ind][j] == '#':
                arr_ret.add((i_ind, j))
            else:
                if field[i_ind][j] in list('prheqk'):
                    arr_ret.add((i_ind, j))
                break

        for j in range(j_ind - 1, -1, -1):
            if field[i_ind][j] == '#':
                arr_ret.add((i_ind, j))
            else:
                if field[i_ind][j] in list('prheqk'):
                    arr_ret.add((i_ind, j))
                break
        return list(arr_ret)


class HorseWhite(Figure):

    def __init__(self):
        self.symbols = 'n'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = {(i_ind - 2, j_ind - 1), (i_ind - 2, j_ind + 1), (i_ind + 2, j_ind - 1), (i_ind + 2, j_ind + 1),
               (i_ind - 1, j_ind - 2), (i_ind - 1, j_ind + 2), (i_ind + 1, j_ind - 2), (i_ind + 1, j_ind + 2)}
        arr_ret = set()
        for pos in arr:
            i, j = pos
            if 0 <= i <= 7 and 0 <= j <= 7 and field[i][j] not in list('prnbqk'):
                arr_ret.add(pos)

        return list(arr_ret)


class HorseBlack(Figure):

    def __init__(self):
        self.symbols = 'N'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = {(i_ind - 2, j_ind - 1), (i_ind - 2, j_ind + 1), (i_ind + 2, j_ind - 1), (i_ind + 2, j_ind + 1),
               (i_ind - 1, j_ind - 2), (i_ind - 1, j_ind + 2), (i_ind + 1, j_ind - 2), (i_ind + 1, j_ind + 2)}
        arr_ret = set()
        for pos in arr:
            i, j = pos
            if 0 <= i <= 7 and 0 <= j <= 7 and field[i][j] not in list('prnbqk'.upper()):
                arr_ret.add(pos)

        return list(arr_ret)


class ElephantBlack(Figure):

    def __init__(self):
        self.symbols = 'E'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = set()
        j = j_ind + 1
        for i in range(i_ind + 1, 8):
            if j <= 7 and field[i][j] not in list('prnbqk'.upper()):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'):
                    break
                j += 1

            else:
                break

        j = j_ind - 1
        for i in range(i_ind + 1, 8):
            if j >= 0 and field[i][j] not in list('prnbqk'.upper()):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'):
                    break
                j -= 1

            else:
                break

        j = j_ind + 1
        for i in range(i_ind - 1, -1, -1):
            if j <= 7 and field[i][j] not in list('prnbqk'.upper()):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'):
                    break
                j += 1
            else:
                break

        j = j_ind - 1
        for i in range(i_ind - 1, -1, -1):
            if j >= 0 and field[i][j] not in list('prnbqk'.upper()):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'):
                    break
                j -= 1
            else:
                break

        return list(arr)


class ElephantWhite(Figure):

    def __init__(self):
        self.symbols = 'e'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = set()
        j = j_ind + 1
        for i in range(i_ind + 1, 8):
            if j <= 7 and field[i][j] not in list('prnbqk'):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'.upper()):
                    break
                j += 1

            else:
                break

        j = j_ind - 1
        for i in range(i_ind + 1, 8):
            if j >= 0 and field[i][j] not in list('prnbqk'):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'.upper()):
                    break
                j -= 1

            else:
                break

        j = j_ind + 1
        for i in range(i_ind - 1, -1, -1):
            if j <= 7 and field[i][j] not in list('prnbqk'):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'.upper()):
                    break
                j += 1
            else:
                break

        j = j_ind - 1
        for i in range(i_ind - 1, -1, -1):
            if j >= 0 and field[i][j] not in list('prnbqk'):
                arr.add((i, j))
                if field[i][j] in list('prnbqk'.upper()):
                    break
                j -= 1
            else:
                break

        return list(arr)


class KingBlack(Figure):

    def __init__(self):
        self.symbols = 'K'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = {(i_ind, j_ind + 1), (i_ind, j_ind - 1), (i_ind + 1, j_ind + 1), (i_ind - 1, j_ind - 1),
               (i_ind + 1, j_ind - 1), (i_ind - 1, j_ind + 1), (i_ind + 1, j_ind), (i_ind - 1, j_ind)}
        arr_ret = set()
        for pos in arr:
            i, j = pos
            if 0 <= i <= 7 and 0 <= j <= 7 and field[i][j] not in list('prnbqk'.upper()):
                arr_ret.add(pos)

        return list(arr_ret)


class KingWhite(Figure):

    def __init__(self):
        self.symbols = 'k'

    def get_all_movies(self, i_ind, j_ind, field):
        arr = {(i_ind, j_ind + 1), (i_ind, j_ind - 1), (i_ind + 1, j_ind + 1), (i_ind - 1, j_ind - 1),
               (i_ind + 1, j_ind - 1), (i_ind - 1, j_ind + 1), (i_ind + 1, j_ind), (i_ind - 1, j_ind)}
        arr_ret = set()
        for pos in arr:
            i, j = pos
            if 0 <= i <= 7 and 0 <= j <= 7 and field[i][j] not in list('prnbqk'):
                arr_ret.add(pos)

        return list(arr_ret)


class QueenWhite(Figure):

    def __init__(self):
        self.symbols = 'q'

    def get_all_movies(self, i_ind, j_ind, field):
        arr1 = RookWhite().get_all_movies(i_ind, j_ind, field)
        arr2 = ElephantWhite().get_all_movies(i_ind, j_ind, field)
        return arr1 + arr2


class QueenBlack(Figure):

    def __init__(self):
        self.symbols = 'Q'

    def get_all_movies(self, i_ind, j_ind, field):
        arr1 = RookBlack().get_all_movies(i_ind, j_ind, field)
        arr2 = ElephantBlack().get_all_movies(i_ind, j_ind, field)
        return arr1 + arr2


def input_to_move(player, field):
    while True:
        # ввели позицию фигуры
        while True:
            try:
                a, b = input('Введите позицию вашей фигуры (A 2): ').split()
                ind_i_from = abs(int(b) - 8)
                ind_j_from = list('ABCDEFGH').index(a.upper())
                hod = a, b
                if field[ind_i_from][ind_j_from] in list('prnbqk') and player == 'white':
                    break
                elif field[ind_i_from][ind_j_from] in list('prnbqk'.upper()) and player == 'black':
                    break
                else:
                    print('Это не ваша фигура')
            except:
                pass
        # вводим позицию хода
        try:
            a, b = input('Введите позицию вашего хода (A 4): ').split()
            ind_i_to = abs(int(b) - 8)
            ind_j_to = list('ABCDEFGH').index(a.upper())

            figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': HorseWhite,
                           'N': HorseBlack,
                           'b': ElephantWhite, 'B': ElephantBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                           'q': QueenWhite}
            # check_mat(player, field, figure_dict)
            movies = figure_dict[field[ind_i_from][ind_j_from]]().get_all_movies(ind_i_from, ind_j_from, field)
            # print(movies)
            global last_movies
            if (ind_i_to, ind_j_to) in movies:
                field[ind_i_to][ind_j_to] = field[ind_i_from][ind_j_from]
                field[ind_i_from][ind_j_from] = '#'

                last_movies.append([''.join(hod), f'{a}{b}'])
                break
            elif (ind_i_to, ind_j_to, 'p') in movies:
                field[ind_i_to][ind_j_to] = field[ind_i_from][ind_j_from]
                field[ind_i_from][ind_j_from] = '#'
                field[ind_i_to+1][ind_j_to] = '#'
                last_movies.append([''.join(hod), f'{a}{b}, p'])
                break
            elif (ind_i_to, ind_j_to, 'P') in movies:
                field[ind_i_to][ind_j_to] = field[ind_i_from][ind_j_from]
                field[ind_i_from][ind_j_from] = '#'
                field[ind_i_to-1][ind_j_to] = '#'
                last_movies.append([''.join(hod), f'{a}{b}', 'P'])
                break
            else:
                print('Такой ход невозможен')
        except:
            pass


class Field:
    def __init__(self):
        self.field = []
        for i in range(8):
            self.field.append(['#'] * 8)
        self.field[0] = list('RNBQKBNR')
        self.field[1] = list('PPPPPPPP')
        # self.field[2] = list('########')
        self.field[-2] = list('pppppppp')
        self.field[-1] = list('RNBQKBNR'.lower())
        # self.field[4][3] = 'E'
        # self.field[2][3] = 'k'

    def check_mat(self):
        figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': HorseWhite,
                       'N': HorseBlack,
                       'b': ElephantWhite, 'B': ElephantBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                       'q': QueenWhite}
        for i in range(8):
            for j in range(8):
                if self.field[i][j] in list('prnbqk'):
                    movies = figure_dict[self.field[i][j]]().get_all_movies(i, j, self.field)
                    for pos in movies:
                        if self.field[pos[0]][pos[1]] == 'K':
                            return '\nШАХ ЧЕРНЫМ'
                elif self.field[i][j] in list('prnbqk'.upper()):
                    movies = figure_dict[self.field[i][j]]().get_all_movies(i, j, self.field)
                    for pos in movies:
                        if self.field[pos[0]][pos[1]] == 'k':
                            return '\nШАХ БЕЛЫМ'

        return ''

    def __repr__(self):
        str_ret = '   A B C D E F G H\n'
        for i in range(8):
            str_ret += str(8 - i) + '  ' + ' '.join(self.field[i]) + '  ' + str(8 - i) + '\n'
        str_ret += '   A B C D E F G H\n' + self.check_mat()
        return str_ret

last_movies = []

def Chess():
    f = Field()
    player = 'white'
    while True:

        print(f)
        print(player, 'move')
        input_to_move(player, f.field)
        # print(last_movies)
        if 'k' not in ''.join([''.join(f.field[i]) for i in range(8)]):
            print(f)
            print('BLACK WIN')
            break

        if 'K' not in ''.join([''.join(f.field[i]) for i in range(8)]):
            print(f)
            print('WHITE WIN')
            break

        if player == 'white':
            player = 'black'
        else:
            player = 'white'

    print('END')


if __name__ == '__main__':
    Chess()
