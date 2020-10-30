import classes
import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("SORTEERHOED")
font = pygame.font.Font("data\dum1.ttf", 10)
start_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
backgroundimage = pygame.image.load("data\papyrus.png")
background.blit(backgroundimage, (0,0))
# manager handled events, gui updates, refreshes etc
manager = pygame_gui.UIManager((800, 600), "theme.json")
start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (100, 50)),
                                             text='Start',
                                             manager=manager
                                            )

# we cappen de framerate van de GUI om de resources die we nodig hebben te beperken.
# ook gebruiken veel elementen timers, dus is het handig!
clock = pygame.time.Clock()
is_running = True
s = classes.Systeem()
s.scramble_antwoorden()
s.scramble_vragen()
vragendict = iter(s.vragen)
tempAfnemer = classes.Afnemer('bram')
huidige_volgorde = {}

vraag1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 100), (700, 100)),
                                        text="Welkom! Druk op start om te beginnen.",
                                        manager = manager)

a = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 250), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='a')
a.hide()

b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 300), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='b')

b.hide()

c = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 350), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='c')
c.hide()

d = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 400), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='d')
d.hide()
def updateVragen(time_delta, vraag):
    nieuwe_antwoorden = iter(s.vragen[vraag].values())
    keys_volgorde = list(s.vragen[vraag].keys())
    nieuwe_volgorde = {'a':keys_volgorde[0],
                       'b':keys_volgorde[1],
                       'c':keys_volgorde[2],
                       'd':keys_volgorde[3]
                       }
    a.set_text(next(nieuwe_antwoorden))
    b.set_text(next(nieuwe_antwoorden))
    c.set_text(next(nieuwe_antwoorden))
    d.set_text(next(nieuwe_antwoorden))
    a.update(time_delta)
    b.update(time_delta)
    c.update(time_delta)
    d.update(time_delta)
    return nieuwe_volgorde
while is_running:
    # hier slaan we die timer waar ik het net over had op.
    # deze delta is eigenlijk hoe lang ons programma er over doet om door deze loop te lopen.
    # omdat we de clock.tick de value 60 geven is onze FPS nu gecapt op 60 fps.
    time_delta = clock.tick(60) / 1000.0
    antwoord_buttons = 'abcd'
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #on start
                if event.ui_element == start:
                    start.hide()
                    a.show()
                    b.show()
                    c.show()
                    d.show()
                    try:
                        vraag = next(vragendict)
                        huidige_volgorde = updateVragen(time_delta, vraag)
                        vraag1.set_text(vraag)
                        vraag1.update(time_delta)
                    except StopIteration:
                        vraag1.set_text("geen vragen meer sorry lol")
                        vraag1.update(time_delta)

                #on button update
                if event.ui_object_id in antwoord_buttons:
                    tempAfnemer.addto(huidige_volgorde[event.ui_object_id])
                    print(tempAfnemer.scoredict)
                    try:
                        vraag = next(vragendict)
                        huidige_volgorde = updateVragen(time_delta, vraag)
                        vraag1.set_text(vraag)
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
