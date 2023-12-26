import pygame, sys, time
from decimal import * # 부동소수점 제거용

# 초기화
pygame.init()

# 창 이름 설정
pygame.display.set_caption("main")

# 화면크기 설정
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN) # 화면크기 - 풀스크린

# fpsj
maxframe = 60
fps = 60
fpsclock = pygame.time.Clock()

# 메인화면
def main():
    menu = True
    button = 0
    
    # 배경음악
    song_0 = pygame.mixer.Sound("audio\\0.mp3")
    song_1 = pygame.mixer.Sound("audio\\1.mp3")
    song_2 = pygame.mixer.Sound("audio\\2.mp3")
    song_3 = pygame.mixer.Sound("audio\\3.mp3")
    song_0.play(-1)
    
    song_list = ["바들바들 동물콘", "Beethoven virus", "summer", "첫눈"]
    
    background = pygame.image.load(f"img\\background.jpg")
    background = pygame.transform.scale(background, (1920, 748))
    
    font = pygame.font.Font('font\SDSamliphopangcheTTFOutline.ttf', 40)
    font2 = pygame.font.Font('font\Jalnan2TTF.ttf', 80)
    font2_text = font2.render("노래 선택", False, (255, 255, 255))
    
    while menu:
        fpsclock.tick(60) # fps 설정
        
        # 노래제목 설정
        if button == 0:
            choice1 = font.render("", False, (255, 255, 255))
        else:
            choice1 = font.render(song_list[button-1], False, (255, 255, 255))
            
        choice2 = font.render("> "+song_list[button]+" <", False, (255, 255, 255))
        
        if button == 3:
            choice3 = font.render("", False, (255, 255, 255))
        else:
            choice3 = font.render(song_list[button+1], False, (255, 255, 255))
        
        # 썸네일 설정
        thumbnail = pygame.image.load(f"img\{button}.png")
        thumbnail = pygame.transform.scale(thumbnail, (800, 450))
        
        # 이벤트 루프
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # 키다운 이벤트
                if event.key == pygame.K_UP:
                    if not button == 0:
                        button -= 1
                        if button == 0:
                            song_1.stop()
                            song_0.play(-1)
                        elif button == 1:
                            song_2.stop()
                            song_1.play(-1)
                        elif button == 2:
                            song_3.stop()
                            song_2.play(-1)
                elif event.key == pygame.K_DOWN:
                    if not button == 3:
                        button += 1
                        if button == 1:
                            song_0.stop()
                            song_1.play(-1)
                        elif button == 2:
                            song_1.stop()
                            song_2.play(-1)
                        elif button == 3:
                            song_2.stop()
                            song_3.play(-1)
                elif event.key == pygame.K_RETURN:
                    if button == 0:
                        song_0.stop()
                        song_1.stop()
                        song_2.stop()
                        song_3.stop()
                        play(0)
                        return
                    elif button == 1:
                        song_0.stop()
                        song_1.stop()
                        song_2.stop()
                        song_3.stop()
                        play(1)
                        return
                    elif button == 2:
                        song_0.stop()
                        song_1.stop()
                        song_2.stop()
                        song_3.stop()
                        play(2)
                        return
                    elif button == 3:
                        song_0.stop()
                        song_1.stop()
                        song_2.stop()
                        song_3.stop()
                        play(3)
                        return
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 600))
        screen.blit(choice1, (1340-(choice1.get_width() / 2), 350-(choice1.get_height() / 2)))
        screen.blit(choice2, (1340-(choice2.get_width() / 2), 540-(choice2.get_height() / 2)))
        screen.blit(choice3, (1340-(choice3.get_width() / 2), 730-(choice3.get_height() / 2)))
        screen.blit(font2_text, (960-(font2_text.get_width() / 2), 150-(font2.get_height() / 2)))
        
        screen.blit(thumbnail, (550-(thumbnail.get_width() / 2), 540-(thumbnail.get_height() / 2)))
        
        # 화면 출력
        pygame.display.flip()

# 인게임
def play(song_num):
    global perfect, great, good, miss, rate, combo, rate_text_size, combo_text_size, rate_text_color, note_num, max_combo
    
    rate = "READY"
    
    load = True
    ingame = False
    
    f = open(f"Charts/{song_num}.txt", "r")
    line_count = 0
    note_start_time = 0
    bpm = 0
    data_list = []
    rate_data = [0, 0, 0, 0]
    clock = pygame.time.Clock()
    maxframe = 60
    
    # 점수설정
    note_num = 0 # 노트의 개수  (점수구할때 사용)
    if song_num == 0:
        note_num = 70
    elif song_num == 1:
        note_num = 289
    elif song_num == 2:
        note_num = 148
    elif song_num == 3:
        note_num = 149
    
    combo = 0
    max_combo = 0
    perfect = 0
    great = 0
    good = 0
    miss = 0

    # 노트설정
    speed = 2.8
    keys = [0, 0, 0, 0]
    keyset = [0, 0, 0, 0]
    n_d = []
    n_f = []
    n_j = []
    n_k = []
    
    # 배경설정
    background = pygame.image.load(f"img\{song_num}.png")
    background = pygame.transform.scale(background, (1920, 1080))
    background.set_alpha(64)
    
    gst = time.time()
    Time = time.time() - gst
    
    # 노래설정
    song = pygame.mixer.Sound(f"audio/{song_num}.mp3")
    song.set_volume(0.3)
    song_play = 0
    
    rate_text_size = 10
    combo_text_size = 20
    rate_text_color = (255, 255, 255)
    
    # 노트 생성
    def sum_note(n_spot, note_sum_time):
        nst = note_sum_time - Time + 2
        if n_spot == 1: # d
            n_d.append([0, nst])
        if n_spot == 2: # f
            n_f.append([0, nst])
        if n_spot == 3: # j
            n_j.append([0, nst])
        if n_spot == 4: # k
            n_k.append([0, nst])
            
    # 노트 판정
    def rating(tiledata):
        global perfect, great, good, miss , rate, combo, rate_text_size, combo_text_size, rate_text_color, note_num, max_combo
        test = 0
        
        if len(tiledata) >= 1 and tiledata[0][0] >= 650:
            
            if test == 1:
                if tiledata[0][0] >= 800: # 테스트용
                    tiledata.remove(tiledata[0])
            else:
                if 770 <= tiledata[0][0] + 7.5 <= 840: # perfect
                    tiledata.remove(tiledata[0])
                    perfect += 1
                    rate = 'perfect'
                    rate_text_size = 10
                    combo += 1
                    combo_text_size = 20
                    rate_text_color = (153,50,204)
                elif 740 <= tiledata[0][0] + 7.5 <= 870: # great
                    tiledata.remove(tiledata[0])
                    great += 1
                    rate = 'great'
                    rate_text_size = 10
                    combo += 1
                    combo_text_size = 20
                    rate_text_color = (102, 255, 255)
                elif 710 <= tiledata[0][0] + 7.5 <= 900: # good
                    tiledata.remove(tiledata[0])
                    good += 1
                    rate = 'good'
                    rate_text_size = 10
                    combo += 1
                    combo_text_size = 20
                    rate_text_color = (255, 255, 0)
                else: # miss
                    tiledata.remove(tiledata[0])
                    miss += 1
                    rate = 'miss'
                    rate_text_size = 10
                    if combo > max_combo:
                        max_combo = combo
                    combo = 0
                    combo_text_size = 50
                    rate_text_color = (102, 102, 102)
            
        else:
            return ''

    while load: # 노트 소환
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
        line = f.readline()
        
        line_count += 1
        
        if line_count == 1:
            note_start_time = line[11:]
            note_start_time = float(Decimal(str(note_start_time)))
        elif line_count == 2:
            song_start_time = line[11:]
            song_start_time = float(Decimal(str(song_start_time)))
        elif line_count == 3:
            bpm = line[11:]
            bpm = float(Decimal(str(bpm)))
        elif line == 'end':
            gst = time.time()
            load = False
            ingame = True
        else:
            data_list.append(list(map(str, line.split('|'))))
            data_list[0][1] = int(data_list[0][1])
            
            # 두개의 노트가 동시에 내려오는 경우도 있어 elif를 사용하지 않음.
            if "1" in data_list[0][0]:
                sum_note(1, Time - note_start_time + 2)
            if "2" in data_list[0][0]:
                sum_note(2, Time - note_start_time + 2)
            if "3" in data_list[0][0]:
                sum_note(3, Time - note_start_time + 2)
            if "4" in data_list[0][0]:
                sum_note(4, Time - note_start_time + 2)
            
            note_start_time -= 240 / bpm / data_list[0][1]  - (240 / bpm / data_list[0][1]) / 98 * (12 / data_list[0][1])
            del data_list[0]
            
        clock.tick(maxframe * 8)
    
    while ingame:
        test = 0
        if test == 1:
            rating(n_d)
            rating(n_f)
            rating(n_j)
            rating(n_k)
        
        fpsclock.tick(60) # fps 설정
        Time = float(Decimal(str(time.time() - gst)))
        
        # 노래가 끝나고 결과창 이동
        if song_num == 0:
            if Time >= 36:
                result(perfect, great, good, miss, max_combo)
                sys.exit()
        elif song_num == 1:
            if Time >= 101:
                result(perfect, great, good, miss, max_combo)
                sys.exit()
        elif song_num == 2:
            if Time >= 64:
                result(perfect, great, good, miss, max_combo)
                sys.exit()
        elif song_num == 3:
            if Time >= 71:
                result(perfect, great, good, miss, max_combo)
                sys.exit()
        
        
        SST = 0 # SST : 딜레이 제거용 노래 소환시간 변수
        if song_play == 0 and song_start_time < Time:
            song.play()
            SST = Time - (song_start_time) 
            song_play += 1
        
        keys[0] += (keyset[0] - keys[0]) / (2 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (2 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (2 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (2 * (maxframe / fps))
        
        # rate_data
        if len(n_d) > 0:
            rate_data[0] = n_d[0][1]
        if len(n_f) > 0:
            rate_data[1] = n_f[0][1]
        if len(n_j) > 0:
            rate_data[2] = n_j[0][1]
        if len(n_k) > 0:
            rate_data[3] = n_k[0][1]    
        
        
        # 이벤트 루프
        for event in pygame.event.get():
            
            # 키다운 이벤트
            if event.type == pygame.KEYDOWN:
                
                # 게임종료(개발용)
                if event.key == pygame.K_KP0:
                    sys.exit()
                    
                # 리듬게임 키
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    rating(n_d)
                if event.key == pygame.K_f:
                    keyset[1] = 1
                    rating(n_f)
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    rating(n_j)
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    rating(n_k)
                    
                    
            # 키업 이벤트
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0
        
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
        # 양쪽선
        pygame.draw.line(screen, (255, 255, 255), [660, 0], [660, 1080], 6)
        pygame.draw.line(screen, (255, 255, 255), [1260, 0], [1260, 1080], 6)
        
        pygame.draw.line(screen, (255, 255, 255), [809.5, 0], [809.5, 1080], 1)
        pygame.draw.line(screen, (255, 255, 255), [960, 0], [960, 1080], 1)
        pygame.draw.line(screen, (255, 255, 255), [1110.5, 0], [1110.5, 1080], 1)
        
        
        # 판정선
        pygame.draw.line(screen, (255, 255, 255), [659, 800], [1261, 800], 3)
        pygame.draw.line(screen, (255, 255, 255), [659, 810], [1261, 810], 3)
        
        
        if rate_text_size < 30:
            rate_text_size += 2
        if combo_text_size < 60:
            combo_text_size += 5
        elif combo_text_size > 60:
            combo_text_size = 60
        
        rate_font = pygame.font.Font('font\DNFBitBitv2.ttf', rate_text_size)
        rate_text = rate_font.render(str(rate), False, rate_text_color)
        combo_font = pygame.font.Font('font\DNFBitBitv2.ttf', combo_text_size)
        combo_text = combo_font.render(str(combo), False, (255, 255, 255))
        
        
        # 판정 결과 출력
        screen.blit(rate_text, (960 - rate_text.get_width() / 2, 670))
        
        
        # 콤보 텍스트 출력
        screen.blit(combo_text, (960 - combo_text.get_width() / 2, 200))
        
        
        # 노트출력
        for i in n_k:
            i[0] = ((1080 / 24) * 17) + (Time + SST - i[1]) * 350 * speed * (1080 / 900)
            if i[0] < 900:
                pygame.draw.rect(screen, (255, 255, 255), [1109.5, i[0], 150.5, 15])
            else:
                n_k.remove(i)
                rate = 'miss'
                miss += 1
                if combo > max_combo:
                    max_combo = combo
                combo = 0
                combo_text_size = 50
                rate_text_color = (102, 102, 102)
        for i in n_j:
            i[0] = ((1080 / 24) * 17) + (Time + SST - i[1]) * 350 * speed * (1080 / 900)
            if i[0] < 900:
                pygame.draw.rect(screen, (255, 255, 255), [959.5, i[0], 150.5, 15]) 
            else:
                n_j.remove(i)
                rate = 'miss'
                miss += 1
                if combo > max_combo:
                    max_combo = combo
                combo = 0
                combo_text_size = 50
                rate_text_color = (102, 102, 102)
        for i in n_f:
            i[0] = ((1080 / 24) * 17) + (Time + SST - i[1]) * 350 * speed * (1080 / 900)
            if i[0] < 900:
                pygame.draw.rect(screen, (255, 255, 255), [809.5, i[0], 150.5, 15])
            else:
                n_f.remove(i)
                rate = 'miss'
                miss += 1
                if combo > max_combo:
                    max_combo = combo
                combo = 0
                combo_text_size = 50
                rate_text_color = (102, 102, 102)
        for i in n_d:
            i[0] = ((1080 / 24) * 17) + (Time + SST - i[1]) * 350 * speed * (1080 / 900)
            if i[0] < 900:
                pygame.draw.rect(screen, (255, 255, 255), [659, i[0], 150.5, 15])
            else:
                n_d.remove(i)
                rate = 'miss'
                miss += 1
                if combo > max_combo:
                    max_combo = combo
                combo = 0
                combo_text_size = 500
                rate_text_color = (102, 102, 102)
        
        
        # 화면 출력
        pygame.display.flip()
        
        clock.tick(maxframe)

def result(perfect, great, good, miss, max_combo):
    note_num = perfect + great + good + miss
    score = (1000000 / note_num * perfect) + (1000000 / note_num / 5 * 4 * great) + (1000000 / note_num / 5 * 3 * good)
    
    aaa = True
    
    while aaa:
        
        # 등급 정하기
        a = 0
        if score == 1000000:
            a = 'S+'
        elif score >= 900000:
            a = 'S'
        elif score >= 700000:
            a = 'A'
        elif score >= 500000:
            a = 'B'
        else:
            a = 'C'
        
        font = pygame.font.Font('font\OKMANFONT.ttf', 170)
        text = font.render(a, False, (255,255,255))
        
        font1 = pygame.font.Font('font\Pretendard-Bold.ttf', 80)
        text1 = font1.render(f'SCORE : {round(score)}', False, (255, 255, 255))
        text7 = font1.render('RESULT', False, (255, 255, 255))
        
        font2 = pygame.font.Font('font\SDSamliphopangcheTTFOutline.ttf', 50)
        text2 = font2.render(f'PERFECT : {perfect}', False, (153,50,204) )
        text3 = font2.render(f'GREAT : {great}', False, (102, 255, 255))
        text4 = font2.render(f'GOOD : {good}', False, (255, 255, 0))
        text5 = font2.render(f'MISS : {miss}', False, (102, 102, 102))
        text6 = font2.render(f'MAX COMBO : {max_combo}', False, (255, 255, 255))
        
        font3 = pygame.font.Font('font\Pretendard-Bold.ttf', 25)
        text8 = font3.render('- 스페이스바를 눌러 선택화면으로 이동 -', False, (255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    main()
                    sys.exit()
        
        screen.fill((0, 0, 0))
        
        circle = pygame.image.load(f"img\circle.jpg")
        circle = pygame.transform.scale(circle, (1350, 900))
        screen.blit(circle, (550 - (circle.get_width() / 2), 560 - (circle.get_height() / 2)))
        #pygame.draw.circle(screen, (255, 255, 255), (550, 540), 300, 10)
        
        screen.blit(text, (595 - (text.get_width() / 2), 560 - (text.get_height() / 2)))
        
        screen.blit(text1, (1070, 350 - (text1.get_height() / 2)))
        
        screen.blit(text2, (1070, 470 - (text2.get_height() / 2)))
        screen.blit(text3, (1070, 550 - (text3.get_height() / 2)))
        screen.blit(text4, (1070, 630 - (text4.get_height() / 2)))
        screen.blit(text5, (1070, 710 - (text5.get_height() / 2)))
        screen.blit(text6, (1070, 790 - (text5.get_height() / 2)))
        
        screen.blit(text7, (960 - (text7.get_width() / 2), 140 - (text7.get_height() / 2)))
        screen.blit(text8, (960 - (text8.get_width() / 2), 1050 - (text8.get_height() / 2)))
            
        # 화면 출력
        pygame.display.flip()
    
main()
