import pygame
import time
from pygame import mixer
import mediapipe as mp
import cv2 as cv2

pygame.init()

screen = pygame.display.set_mode((1280, 1000))

# Initialize
pygame.display.set_caption('better osu!mania')
icon = pygame.image.load('assets/keyboard.png')
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1280, 1000))
pygame.display.set_icon(icon)

# Sound
mixer.music.load('assets/osu.mp3')

# Images
leftR = pygame.image.load('assets/leftR.png')
downR = pygame.image.load('assets/downR.png')
upR = pygame.image.load('assets/upR.png')
rightR = pygame.image.load('assets/rightR.png')

left = pygame.image.load('assets/left.png')
down = pygame.image.load('assets/down.png')
up = pygame.image.load('assets/up.png')
right = pygame.image.load('assets/right.png')

leftD = pygame.image.load('assets/leftD.png')
downD = pygame.image.load('assets/downD.png')
upD = pygame.image.load('assets/upD.png') 
rightD = pygame.image.load('assets/rightD.png')

marvelous = pygame.image.load('assets/marvelous.png')
perfect = pygame.image.load('assets/perfect.png')
great = pygame.image.load('assets/great.png')
miss = pygame.image.load('assets/miss.png')

arrowLX, arrowLY, arrowLX_change  = 577.5, 412.5, 0
arrowDX, arrowDY, arrowDY_change = 577.5, 412.5, 0
arrowUX, arrowUY, arrowUY_change = 577.5, 412.5, 0
arrowRX, arrowRY, arrowRX_change = 577.5, 412.5, 0
judgement, judgement_hp = 0, 0

# Score
score_count = 0
font = pygame.font.Font('freesansbold.ttf', 60)
textX, textY = 1100, 20

# Failed
hp = 100
hp_font = pygame.font.Font('freesansbold.ttf', 48)
failed_font = pygame.font.Font('freesansbold.ttf', 100)
hpX, hpY = 1000, 600

# Functions
def show_score (x, y):
    score = font.render(str(score_count), True, (255,255,255))
    screen.blit(score, (x, y))

def show_hp (x, y):
    health = hp_font.render(str(hp), True, (220,20,60))
    screen.blit(health, (x, y))

def failed():
    global arrowLX, arrowDX, arrowRX, arrowUX
    failed = failed_font.render("FAILED", True, (255,0,0))
    arrowLX = -5000; arrowRX = -5000; arrowUX = 5000; arrowDX = 5000 
    screen.blit(failed, (450, 450))

def receptors():
    screen.blit(leftR, (185, 412.5))
    screen.blit(downR, (577.5, 805))
    screen.blit(upR, (577.5, -20))
    screen.blit(rightR, (970, 412.5))

def arrowL(lX):
    screen.blit(left, (lX, arrowLY))

def arrowR(rX):
    screen.blit(right, (rX, arrowRY))

def arrowU(uY):
    screen.blit(up, (arrowUX, uY))

def arrowD(dY):
    screen.blit(down, (arrowDX, dY))

def check_timingL (arrowX):
    global judgement, score_count, judgement_hp
    if 165 <= arrowX <= 205:
        judgement_hp = 1
        judgement = 1
        score_count += 10
    elif 135 <= arrowX <= 235:
        judgement_hp = 2
        judgement = 2
        score_count += 8
    elif 115 <= arrowX <= 255:
        judgement_hp = 3
        judgement = 3
        score_count += 3
    else:
        judgement_hp = 4
        judgement = 4
        score_count -= 5
    return True

def check_timingR (arrowX):
    global judgement, score_count, judgement_hp
    if 950 <= arrowX <= 1000:
        judgement_hp = 1
        judgement = 1
        score_count += 10
    elif 920 <= arrowX <= 1020:
        judgement_hp = 2
        judgement = 2
        score_count += 8
    elif 900 <= arrowX <= 1040:
        judgement_hp = 3
        judgement = 3
        score_count += 3
    else:
        judgement_hp = 4
        judgement = 4 
        score_count -= 5
    return True

def check_timingU (arrowY):
    global judgement, score_count, judgement_hp
    if -40 <= arrowY <= 0:
        judgement_hp = 1
        judgement = 1
        score_count += 10
    elif -70 <= arrowY <= 30:
        judgement_hp = 2
        judgement = 2
        score_count += 8
    elif -90 <= arrowY <= 50:
        judgement_hp = 3
        judgement = 3
        score_count += 3
    else:
        judgement_hp = 4
        judgement = 4
        score_count -= 5
    return True

def check_timingD (arrowY):
    global judgement, score_count, judgement_hp 
    if 755 <= arrowY <= 855:
        judgement_hp = 1
        judgement = 1
        score_count += 10
    elif 745 <= arrowY <= 865:
        judgement_hp = 2
        judgement = 2
        score_count += 8
    elif 735 <= arrowY <= 875:
        judgement_hp = 3
        judgement = 3
        score_count += 3
    else:
        judgement_hp = 4
        judgement = 4
        score_count -= 5
    return True

def press (time, show):
    global arrowLX, arrowLX_change, arrowLY, arrowRX, arrowRY, arrowRX_change, arrowUX, arrowUY, arrowUY_change, arrowDX, arrowDY, arrowDY_change
    hitsound = mixer.Sound('assets/soft-hitnormal.wav')
    hitsound.set_volume(0.1)
    if time < show:
        hitsound.play()
        if pressL:
            screen.blit(leftD, (185, 412.5))
            arrowLX = 577.5
            arrowLY = 412.5
            # arrowLX_change += -0.01
        if pressR:
            screen.blit(rightD, (970, 412.5))
            arrowRX = 577.5
            arrowRY = 412.5
            # arrowRX_change += 0.01
        if pressU:
            screen.blit(upD, (577.5, -20))
            arrowUX = 577.5
            arrowUY = 412.5
            # arrowUY_change += -0.01
        if pressD:
            screen.blit(downD, (577.5, 805))
            arrowDX = 577.5
            arrowDY = 412.5
            # arrowDY_change += 0.01

def judge (time, show):
    global hp, judgement_hp
    if time < show:
        if judgement == 1:
            screen.blit(marvelous, (500, 464))
        if judgement == 2:
            screen.blit(perfect, (500, 464))
        if judgement == 3:
            screen.blit(great, (500, 464))
        if judgement == 4:
            screen.blit(miss, (500, 464))    

def check_hp():
    global hp, judgement_hp
    if hp == 0:
        return failed()
    if judgement_hp == 1:
        hp = hp+5 if hp+5 < 100 else 100
    if judgement_hp == 2:
        hp = hp+2 if hp+2 < 100 else 100
    if judgement_hp == 3:
        hp = hp+1 if hp+1 < 100 else 100
    if judgement_hp == 4:
        hp = hp-20 if hp-20 > 0 else 0
    judgement_hp = 0

def hand_in_left(x, y):
    if 10 <= x <= 110 and 150 <= y <= 250:
        return True

def hand_in_right(x, y):
    if 525 <= x <= 625 and 150 <= y <= 250:
        return True

def hand_in_up(x, y):
    if 275 <= x <= 375 and 0 <= y <= 100:
        return True

def hand_in_down(x, y):
    if 275 <= x <= 375 and 375 <= y <= 475:
        return True

# Game
running = True
pressL, pressR, pressU, pressD = False, False, False, False
show_judgement, show_press, show_arrowL, show_arrowR, show_arrowU, show_arrowD = 0, 0, 0, 0, 0, 0
start_time = time.time()
while running:
    screen.blit(background, (0,0))
    elapsed_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                show_press = elapsed_time + 250
                pressL = True
                print("pressed left arrow at: ", arrowLX)
                if check_timingL(arrowLX):
                    show_judgement = elapsed_time + 500

            if event.key == pygame.K_RIGHT:
                show_press = elapsed_time + 250
                pressR = True
                print("pressed right arrow at: ", arrowRX)
                if check_timingR(arrowRX):
                    show_judgement = elapsed_time + 500

            if event.key == pygame.K_UP:
                show_press = elapsed_time + 250
                pressU = True
                print("pressed up arrow at: ", arrowUY)
                if check_timingU(arrowUY):
                    show_judgement = elapsed_time + 500

            if event.key == pygame.K_DOWN:
                show_press = elapsed_time + 250
                pressD = True
                print("pressed down arrow at: ", arrowDY)
                if check_timingD(arrowDY):
                    show_judgement = elapsed_time + 500

            if event.key == pygame.K_w:
                arrowUY_change = -2.5

            if event.key == pygame.K_a:
                arrowLX_change = -2.5

            if event.key == pygame.K_s:
                arrowDY_change = 2.5

            if event.key == pygame.K_d:
                arrowRX_change = 2.5

            # Music
            if event.key == pygame.K_p:
                mixer.music.play(0, 100)
                pygame.mixer.music.set_volume(0.3)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressL = False
            if event.key == pygame.K_RIGHT:
                pressR = False
            if event.key == pygame.K_UP:
                pressU = False
            if event.key == pygame.K_DOWN:
                pressD = False

            if event.key == pygame.K_w:
                arrowUY_change = 0
                arrowUY = 412.5
            if event.key == pygame.K_a:
                arrowLX_change = 0
                arrowLX = 577.5
            if event.key == pygame.K_s:
                arrowDY_change = 0
                arrowDY = 412.5
            if event.key == pygame.K_d:
                arrowRX_change = 0
                arrowRX = 577.5

            if event.key == pygame.K_p:
                pygame.mixer.music.pause()

    receptors()

    arrowLX += arrowLX_change
    arrowL(arrowLX)

    arrowRX += arrowRX_change
    arrowR(arrowRX)

    arrowUY += arrowUY_change
    arrowU(arrowUY)

    arrowDY += arrowDY_change
    arrowD(arrowDY)

    press(elapsed_time, show_press)
    judge(elapsed_time, show_judgement)
    check_hp()

    show_score(textX, textY)
    show_hp(hpX, hpY)

    pygame.display.update()

# Detection
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
prevTime = 0

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        lmList = []

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        cv2.rectangle(image, (110, 250), (10, 150), (0, 255, 0), 5)
        cv2.rectangle(image, (375, 100), (275, 0), (0, 255, 0), 5)
        cv2.rectangle(image, (625, 250), (525, 150), (0, 255, 0), 5)
        cv2.rectangle(image, (375, 475), (275, 375), (0, 255, 0), 5)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                # print(lmList)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                x = lmList[8][1]
                y = lmList[8][2]
                if hand_in_left(x, y):
                    pressL = True
                    # print("left")
                if hand_in_right(x, y):
                    pressR = True
                    # print("right")
                if hand_in_up(x, y):
                    pressU = True
                    # print("up")
                if hand_in_down(x, y):
                    pressD = True
                    # print("down")

        cv2.imshow('Movement Detection', image)
        if cv2.waitKey(5) & 0xFF == 27:
            cap.release()
            cv2.destroyAllWindows()
            break