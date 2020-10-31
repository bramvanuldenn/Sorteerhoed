import classes
import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("SORTEERHOED")
font = pygame.font.Font("data\dum1.ttf", 10)
start_surface = pygame.display.set_mode((1000, 700))
background = pygame.Surface((1000, 700))
backgroundimage = pygame.image.load("data\startdonker.png")
backgroundlicht = pygame.image.load("data\startlicht.png")
background.blit(backgroundimage, (0,0))
papierrol = pygame.image.load("data\papierrol.png")
papierrol = pygame.transform.scale(papierrol, (800, 150))
# manager handled events, gui updates, refreshes etc
manager = pygame_gui.UIManager((1000, 700), "theme.json")

# we cappen de framerate van de GUI om de resources die we nodig hebben te beperken.
# ook gebruiken veel elementen timers, dus is het handig!
clock = pygame.time.Clock()
is_running = True
s = classes.Systeem()
s.scramble_antwoorden()
s.scramble_vragen()
vragendict = iter(s.vragen)
afnemer = classes.Afnemer('placeholder')
huidige_volgorde = {}

pygame.mixer.init()
pygame.mixer.music.load("data/seashanty2.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0)

vraag1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 100), (700, 100)),
                                        text="Welkom! Vul je naam in en druk op de deur om te beginnen.",
                                        manager = manager,
                                        object_id='vraag1')

victory_banner = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 300), (700, 100)),
                                        text="",
                                        manager = manager)

victory_banner.hide()

textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 300), (400, 100)),
                                        manager=manager)

a = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='a')
a.hide()

b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 300), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='b')

b.hide()

c = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='c')
c.hide()

d = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 400), (700, 50)),
                                             text='aya',
                                             manager=manager,
                                             object_id='d')
d.hide()

volumeslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 570), (300, 30)),
                                                      manager=manager,
                                                      start_value=10,
                                                      value_range=(0,100))

doorbutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 100), (300, 600)),
                                             text='',
                                             manager=manager,
                                             object_id='deur')





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

def showResultaat(time_delta):
    a.hide()
    b.hide()
    c.hide()
    d.hide()
    vraag1.set_text("ewaja broer hier is je resultaat")
    vraag1.update(time_delta)
    for i in afnemer.scoredict:
        if afnemer.scoredict[i] == max(afnemer.scoredict.values()):
            victory_banner.set_text(f"wow {afnemer.naam} wat een zieke toets heb je gemaakt jij bent echt eentje voor {i}")
            victory_banner.show()
            victory_banner.update(time_delta)
    afnemer.schrijf_resultaat()



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
                if event.ui_element == doorbutton and textbox.text != "":
                    afnemer.naam = textbox.text
                    textbox.hide()
                    doorbutton.hide()
                    a.show()
                    b.show()
                    c.show()
                    d.show()
                    backgroundimage = pygame.image.load("data/vraag_scherm.jpg")
                    try:
                        vraag = next(vragendict)
                        huidige_volgorde = updateVragen(time_delta, vraag)
                        vraag1.set_text(vraag)
                        vraag1.update(time_delta)
                    except StopIteration:
                        vraag1.set_text("geen vragen meer sorry lol")
                        vraag1.update(time_delta)
                if event.ui_element == doorbutton and textbox.text == "":
                    vraag1.set_text("Vergeet geen naam in te vullen!")


                #on button update
                if event.ui_object_id in antwoord_buttons:
                    afnemer.addto(huidige_volgorde[event.ui_object_id])
                    print(afnemer.naam, "-", afnemer.scoredict)
                    try:
                        vraag = next(vragendict)
                        huidige_volgorde = updateVragen(time_delta, vraag)
                        vraag1.set_text(vraag)
                        vraag1.update(time_delta)
                    except StopIteration:
                        showResultaat(time_delta)
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                pygame.mixer.music.set_volume(volumeslider.current_value / 100)
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                if event.ui_element == doorbutton:
                    background.blit(backgroundlicht, (0,0))
            if event.user_type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                if event.ui_element == doorbutton:
                    background.blit(backgroundimage, (0,0))
        if event.type == pygame.QUIT:
            is_running = False


        manager.process_events(event)
    manager.update(time_delta)
    start_surface.blit(background, (0, 0))
    start_surface.blit(papierrol, (108, 72.5))
    manager.draw_ui(start_surface)


    pygame.display.update()