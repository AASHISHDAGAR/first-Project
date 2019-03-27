from random import randint
rnd_number = randint(1, 100)

choose_number = [0]
game_over = False

while not game_over:
    choose_number = [0]
    attempt = 0
    player_choose = input('Guess the BTW 1 and 100')
    choose_number.append(player_choose)

    if player_choose == rnd_number:
        print('Congratulations you won the game !!')
        game_over = True
        game_play = False
    if attempt < 1:
        if abs(rnd_number - player_choose) <= 10:
            print('Warm')
        elif abs(rnd_number - player_choose) > 10:
            print('Cold')

    while game_play:
        if abs(rnd_number - choose_number[- 1] < abs(rnd_number -
                                                     choose_number[-2])):
            print('Warmer')
        elif abs(rnd_number - choose_number[- 1] < abs(rnd_number -
                                                       choose_number[-2])):
            print('Colder')
    continue



