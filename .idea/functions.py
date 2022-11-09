# Игра крестики-нолики.

EMPTY = ' '

def instructions():
    '''Выводит инструкции для игрока на экран!'''
    print('''
    Добро пожаловать в игру кречстики-нолики! 
    
    По правилам игры вам необходимо выбрать, какими символами 
    
    будете играть, затем жеребьевка на право первого хода.
    
    Игровое поле выглядит так:
    
         |    |     
    ----------------
         |    |    
    ----------------
         |    |            
    
    ''')


def question():
    '''Определение, какими символами будет играть пользователь.
    Возвращает выбранный символ.'''
    print('Какими символами Вы будете играть, "x" или "0" ?')
    human = ' '
    comp = ' '
    while human not in ('x', '0'):
        human = input('\nВведите "x" или "0": ').lower()
        if human == 'x':
            comp = '0'
            print('\nХорошо, Вы играете "x"')
        elif human == '0':
            comp = 'x'
            print('\nХорошо, Вы играете "0"')
    return human, comp


def who():
    '''Кто начинает первым игру??'''
    answer = None
    while answer not in ('y', 'n'):
        answer = input('\nХотите ли вы сыграть первым (y/n): ').lower()
    return answer


def acquaintance():
    '''Печать игровой зоны '''
    print("\n----Ознакомьтесь с возможными ходами----")
    print('''   
      0  |  1  |  2   
    ----------------
      3  |  4  |  5   
    ----------------
      6  |  7  |  8         
    ''')


def area():
    '''Создаем новую игральную область.
    Возвращает пустой список'''
    board = [(lambda i: EMPTY)(i) for i in range(9)]
    return board


def display(board):
    '''Печать игровой зоны '''
    print(f"\n\t  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("\t----------------")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("\t----------------")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}  ")


def available(board):
    '''Проверка наличия свободных ходов
    Выводит список свободных ходов'''
    free_area = []
    for i in range(9):
        if board[i] == EMPTY:
            free_area.append(i)
    return free_area


def win(board):
    '''Определяем выйгрышные комбинации и
    возвращает победителя'''
    tie = 'Ничья'
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
    for i in combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
        elif EMPTY not in board:
            return board
    return 0


def player(board, human):
    '''Ход игрока. Возвращает ответ.'''
    move = available(board)
    answer = None
    while answer not in move:
        answer = input('\nВыбери поле из интервала (0-8): ')
        try:
            answer = int(answer)
        except (ValueError, IndexError):
            print('Это не число вообще')
            continue
        if answer > 8 or answer < 0:
            print('Диапазон не соблюдается!')
        elif answer not in move:
            print('Это место уже занято!')
    return answer


def computer(board, human, comp):
    '''Ход компьютера.'''
    board = board[:]
    comp_choice = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for move in available(board):
        board[move] = comp
        if win(board) == comp:
            print(f'\n{move} - выбор компьютера!')
            return move
        board[move] = EMPTY
    for move in available(board):
        board[move] = human
        if win(board) == human:
            print(f'\n{move} - выбор компьютера!')
            return move
        board[move] = EMPTY
    for move in comp_choice:
        if move in available(board):
            print(f'\n{move} - выбор компьютера!')
            return move


def end(winner, comp, human):
    if winner == comp:
        print('\nКомпьютер победил!')
    elif winner == human:
        print('\nЧеловек победил!')
    else:
        print('\nНичья!')


def another():
    tell = input('Хотите сыграть еще раз? Напишите y/n: ')
    if tell.lower() == 'y':
        main()
    elif tell.lower() == 'n':
        print('Хорошего дня!')
    else:
        input('Нажмите enter, чтобы выйти!')





