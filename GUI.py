import pygame
import functions
import db
import time


def create_button(screen, size_and_coords, text=''):
    txt = pygame.font.Font('fonts\\UniSans.ttf', 48)
    txt_out = txt.render(text, True, (245, 98, 98))
    screen.blit(txt_out, (size_and_coords[0], size_and_coords[1]))


def game_cycle():
    run = True
    pygame.init()

    # настройка экрана
    size = 1600, 900
    screen = pygame.display.set_mode(size)

    bg_start = pygame.image.load('Images\\bg_start.jpg')
    bg_start = pygame.transform.smoothscale(bg_start, screen.get_size())
    screen.blit(bg_start, (0, 0))
    pygame.display.flip()


    for i in range(0, 1600, 16):
        pygame.draw.line(screen, (22, 36, 49), (i, 0), (i, 900), 16)
        time.sleep(0.03)
        pygame.display.flip()



    bg = pygame.image.load('Images\\background.jpg')
    bg = pygame.transform.smoothscale(bg, screen.get_size())
    screen.blit(bg, (0, 0))

    setings_but = False

    create_button(
        screen,
        (1346 - 189, 55, 189, 60),
        'настройки'
    )

    create_button(
        screen,
        (250 - 176, 835 - 21, 189, 60),
        'контакты'
    )

    create_button(
        screen,
        (1346 - 189, 835 - 21, 189, 60),
        'инструкция'
    )

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if 1346 - 189 < pygame.mouse.get_pos()[0] < 1346 + 100 and \
                        55 < pygame.mouse.get_pos()[1] < 55 + 48:
                    setings_but = True

                    pygame.draw.rect(
                        screen,
                        (165, 249, 98),
                        (250 - 176, 55, 1024, 576)
                    )

                    create_button(
                        screen,
                        (250 - 156, 75, 271 * 2, 30),
                        'добавить программу в бд'
                    )

                if 90 < pygame.mouse.get_pos()[0] < 750 and \
                        85 < pygame.mouse.get_pos()[1] < 130 and \
                        setings_but:
                    db.add_element(functions.get_name(), functions.get_URL())

                if 250 - 176 < pygame.mouse.get_pos()[0] < 250 + 176 and \
                        835 - 21 < pygame.mouse.get_pos()[1] < 835 + 21:
                    setings_but = False

                    pygame.draw.rect(
                        screen,
                        (165, 249, 98),
                        (250 - 176, 55, 1024, 576)
                    )

                    txt = pygame.font.Font(
                        'fonts\\UniSans.ttf',
                        35
                    )
                    txt_email = pygame.font.Font(
                        'fonts\\Roboto-BlackItalic.ttf',
                        35
                    )

                    text = 'по поводу сотрудничества или'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 55)
                    )

                    text = 'идей по улучшению пишите на почту'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 95)
                    )

                    text = 'dan4ik-gp@yandex.ru'
                    txt_out = txt_email.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 135)
                    )

                if 1346 - 189 < pygame.mouse.get_pos()[0] < 1346 + 100 and \
                        835 - 21 < pygame.mouse.get_pos()[1] < 835 + 21:
                    setings_but = False

                    pygame.draw.rect(
                        screen,
                        (165, 249, 98),
                        (250 - 176, 55, 1024, 576)
                    )

                    txt = pygame.font.Font(
                        'fonts\\UniSans.ttf',
                        35
                    )

                    text = 'для работы программы требуется микрофон'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 55)
                    )

                    text = 'необходимо сказать слово Алекс и назвать команду'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 95)
                    )

                    text = 'на данный момент существует 4 функции:'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98))
                    screen.blit(
                        txt_out,
                        (250 - 176, 135)
                    )

                    text = 'запуск и закрытие приложения (необходимо '
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 175)
                    )

                    text = 'добавить в список приложений в настройках)'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 210)
                    )

                    text = 'выключение компьютера и изменение громкости'
                    txt_out = txt.render(
                        text,
                        True,
                        (245, 98, 98)
                    )
                    screen.blit(
                        txt_out,
                        (250 - 176, 245)
                    )

        pygame.display.flip()

    pygame.quit()


game_cycle()
