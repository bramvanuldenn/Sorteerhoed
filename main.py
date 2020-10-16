import classes
import pygame
import pygame_gui


pygame.init()
pygame.display.set_caption("SORTEERHOED")
font = pygame.font.Font("data\dum1.ttf", 10)
start_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# manager handled events, gui updates, refreshes etc
manager = pygame_gui.UIManager((800, 600), "theme.json")
start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (100, 50)),
                                             text='Start',
                                             manager=manager
                                            )

otherstart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 300), (100, 50)),
                                             text='Other Start',
                                             manager=manager)

ok = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 350), (100, 50)),
                                             text='Ok',
                                             manager=manager)

# we cappen de framerate van de GUI om de resources die we nodig hebben te beperken.
# ook gebruiken veel elementen timers, dus is het handig!
clock = pygame.time.Clock()
is_running = True
s = classes.Systeem()
s.scramble_antwoorden()
s.scramble_vragen()
vragendict = iter(s.vragen)
vraag1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 100), (700, 100)),
                                        text=next(vragendict),
                                        manager = manager)

while is_running:
    # hier slaan we die timer waar ik het net over had op.
    # deze delta is eigenlijk hoe lang ons programma er over doet om door deze loop te lopen.
    # omdat we de clock.tick de value 60 geven is onze FPS nu gecapt op 60 fps.
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start:
                    start.hide()
                    otherstart.show()
                if event.ui_element == otherstart:
                    otherstart.hide()
                    start.show()
                if event.ui_element == ok:
                    try:
                        vraag1.set_text(next(vragendict))
                        vraag1.update(time_delta)
                    except StopIteration:
                        vraag1.set_text("geen vragen meer sorry lol")
                        vraag1.update(time_delta)
        if event.type == pygame.QUIT:
            is_running = False


        manager.process_events(event)
    manager.update(time_delta)
    start_surface.blit(background, (0, 0))
    manager.draw_ui(start_surface)


    pygame.display.update()







#s = classes.Systeem()
#inputNaam = str(input("Wat is je naam? "))
#afnemer = classes.Afnemer(inputNaam)
#print(afnemer.scoredict)
#for i in s.vragen:
#    print(i)
#    print(s.vragen[i])
#    a = {
#        "a": 0,
#        "b": 1,
#        "c": 2,
#        "d": 3
#    }
#    inputAntwoord = str(input()).lower()
#    iterdict = iter(s.vragen[i])
#
#    if inputAntwoord in "abcd":
#        val = a[inputAntwoord]
#        print(val)
#        for i in range(0, val):
#            next(iterdict)
#        a = (next(iterdict))
#        print(a)
#        afnemer.addto(a)
#        print(afnemer.scoredict)
#afnemer.schrijf_resultaat()
