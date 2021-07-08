# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Пивной алкаш', color="#c8ffc8")

image bg maze = "maze/base0.png"

image left3 = "maze/left3.png"
image left2 = "maze/left2.png"
image left1 = "maze/left1.png"

image right3 = "maze/right3.png"
image right2 = "maze/right2.png"
image right1 = "maze/right1.png"

image front1 = "maze/front1.png"
image front2 = "maze/front2.png"

image enemy1 = "kiwi.png"
image enemy2 = "Mike.png"
image enemy3 = "Stas.png"
image enemy4 = "Ric.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    #start hp, mana
    $ hp = 30
    $ mana = 10

    $ weapon = 0

    #start pos and dir
    $ x = 6
    $ y = 3
    $ dir = 0

    #level
    $ a = [ [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 3, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 2, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 2, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 3, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    $ renpy.movie_cutscene("Intro1.mpg")
    $ renpy.movie_cutscene("Intro2.mpg")
    $ renpy.movie_cutscene("Intro3.mpg")
    $ renpy.movie_cutscene("Intro4.mpg")
    $ renpy.movie_cutscene("Intro5.mpg")

    #game loop
    while hp > 0:
        call render_maze from _call_render_maze

        $ t = False
        if dir == 0 and a[x][y+1] != 1:
            $ t = True
        elif dir == 1 and a[x+1][y] != 1:
            $ t = True
        elif dir == 2 and a[x][y-1] != 1:
            $ t = True
        elif dir == 3 and a[x-1][y] != 1:
            $ t = True

        $ enemy = renpy.random.randint(1, 10)

        if t == True:
            menu:
                "x:[x], y:[y]\nhp:[hp]"
                "вперёд":
                    $ renpy.movie_cutscene("forward.mpg")
                    if dir == 0:
                        $ y += 1
                    elif dir == 1:
                        $ x += 1
                    elif dir == 2:
                        $ y -= 1
                    elif dir == 3:
                        $ x -= 1

                    if a[x][y] == 2:
                        $ enemy = 0
                    if a[x][y] == 3:
                        $ enemy = -1

                    call render_maze from _call_render_maze_1
                    #check for fight
                    if enemy <= 2:
                        #fight
                        $ ehp = 0
                        $ enemyname = ""
                        if enemy == 1:
                            show enemy1
                            $ ehp = 4
                            $ enemyname = "ТакБлэт"
                        elif enemy == 2:
                            show enemy2
                            $ ehp = 6
                            $ enemyname = "Майк Вазовски"
                        elif enemy == 0:
                            show enemy3
                            $ ehp = 8
                            $ enemyname = "Стас Барецкий"
                        elif enemy == -1:
                            show enemy4
                            $ ehp = 12
                            $ enemyname = "Рикардо Милос"
                        while ehp > 0:
                            if hp <= 0:
                                jump penis
                            menu:
                                "you: [hp]hp, [mana]mana\n[enemyname]: [ehp]hp"
                                "атаковать":
                                    $ att = 0
                                    if weapon == 0:
                                        $ renpy.movie_cutscene("weapon1.mpg")
                                        $ att = 1
                                    if weapon == 1:
                                        $ renpy.movie_cutscene("weapon2.mpg")
                                        $ att = 2
                                    if weapon == 2:
                                        $ renpy.movie_cutscene("weapon3.mpg")
                                        $ att = 3

                                    $ hp -= 1
                                    $ ehp -= att
                                    "Вы ударили [enemyname] на [att] урон"
                                    if ehp <= 0:
                                        "Вы убили [enemyname]"
                                        $ a[x][y] = 0
                                        if weapon < 2:
                                            $ weapon += 1
                                        if enemy == -1:
                                            jump win
                                "уклониться":
                                    "Вы уклонились от удара [enemyname]"
                                "способность":
                                    "Вы использовали вашу способность, но ничего не произошло"
                                "сбежать":
                                    $ ehp = 0
                                    "Вы съебались от [enemyname]"
                        label penis:
                            if hp <= 0:
                                "Вы умерли от [enemyname]"
                                if enemy == 1:
                                    $ renpy.movie_cutscene("DieKiwi.mpg")
                                elif enemy == 2:
                                    $ renpy.movie_cutscene("DieMike.mpg")
                                elif enemy == 0 or enemy == -1:
                                    $ renpy.movie_cutscene("DieStas.mpg")
                                $ renpy.movie_cutscene("died.mpg")
                        hide enemy1
                        hide enemy2
                        hide enemy3
                        hide enemy4

                #rotate player
                "налево":
                    $ renpy.movie_cutscene("left.mpg")
                    if dir == 0:
                        $ dir = 3
                    else:
                        $ dir -= 1
                "направо":
                    $ renpy.movie_cutscene("right.mpg")
                    if dir == 3:
                        $ dir = 0
                    else:
                        $ dir += 1
            call render_maze from _call_render_maze_2
        else:
            menu:
                "x:[x], y:[y]\nhp:[hp]"
                #rotate player
                "налево":
                    $ renpy.movie_cutscene("left.mpg")
                    if dir == 0:
                        $ dir = 3
                    else:
                        $ dir -= 1
                "направо":
                    $ renpy.movie_cutscene("right.mpg")
                    if dir == 3:
                        $ dir = 0
                    else:
                        $ dir += 1
            call render_maze from _call_render_maze_3
    return
    label win:
        $ renpy.movie_cutscene("win.mpg")






    # e "Вы готовы?"
    #
    # $ renpy.movie_cutscene("a.mpg")
    #
    # menu:
    #     "Как на это реагировать?"
    #
    #     "Ругаться":
    #         $ renpy.movie_cutscene("b.mpg")
    #     "Запустить ракету":
    #         $ renpy.movie_cutscene("oa4_launch.webm")
    #
    # $ renpy.movie_cutscene("chromotest.mpg")
    #
    # $ i = 0
    #
    # while i < 3:
    #     e "хуй"
    #     $ i += 1
    #
    # e "конец истории"

    return


label render_maze:
    show bg maze
    hide left1
    hide left2
    hide left3
    hide right1
    hide right2
    hide right3
    hide front1
    hide front2

    if dir == 0:
        #left
        if y <= 6 and a[x-1][y+2] == 1:
            show left3
        if a[x-1][y+1] == 1:
            show left2
        if a[x-1][y] == 1:
            show left1
        #right
        if y <= 6 and a[x+1][y+2] == 1:
            show right3
        if a[x+1][y+1] == 1:
            show right2
        if a[x+1][y] == 1:
            show right1
        #front
        if y <= 6 and a[x][y+2] == 1:
            show front2
        if a[x][y+1] == 1:
            show front1
    elif dir == 1:
        #left
        if x <= 13 and a[x+2][y+1] == 1:
            show left3
        if a[x+1][y+1] == 1:
            show left2
        if a[x][y+1] == 1:
            show left1
        #right
        if x <= 13 and a[x+2][y-1] == 1:
            show right3
        if a[x+1][y-1] == 1:
            show right2
        if a[x][y-1] == 1:
            show right1
        #front
        if x <= 13 and a[x+2][y] == 1:
            show front2
        if a[x+1][y] == 1:
            show front1
    elif dir == 2:
        #left
        if y >= 2 and a[x+1][y-2] == 1:
            show left3
        if a[x+1][y-1] == 1:
            show left2
        if a[x+1][y] == 1:
            show left1
        #right
        if y >= 2 and a[x-1][y-2] == 1:
            show right3
        if a[x-1][y-1] == 1:
            show right2
        if a[x-1][y] == 1:
            show right1
        #front
        if y >= 2 and a[x][y-2] == 1:
            show front2
        if a[x][y-1] == 1:
            show front1
    elif dir == 3:
        #left
        if x <= 13 and a[x-2][y-1] == 1:
            show left3
        if a[x-1][y-1] == 1:
            show left2
        if a[x][y-1] == 1:
            show left1
        #right
        if x <= 13 and a[x-2][y+1] == 1:
            show right3
        if a[x-1][y+1] == 1:
            show right2
        if a[x][y+1] == 1:
            show right1
        #front
        if x <= 13 and a[x-2][y] == 1:
            show front2
        if a[x-1][y] == 1:
            show front1
    return
