import pygame, sys, time
from decimal import * # 부동소수점 제거용

# 초기화
pygame.init()

# 창 이름 설정
pygame.display.set_caption("main")

# 화면크기 설정
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN) # 화면크기 - 풀스크린

# fps
maxframe = 60
fps = 60
fpsclock = pygame.time.Clock()


# 노래선택(인게임 구현후 구현예정)
def choice():
    pass

def check():
    pass

# 인게임
def play():
    global score, perfect, great, good, miss
    
    load = True
    
    f = open("Charts/1.txt", "r")
    note_start_time = 0
    bpm = 180.0
    data_list = []
    
    # 점수설정
    score = 0
    perfect = 0
    great = 0
    good = 0
    miss = 0

    # 노트설정
    speed = 8
    keys = [0, 0, 0, 0]
    keyset = [0, 0, 0, 0]
    n_d = []
    n_f = []
    n_j = []
    n_k = []
    gst = time.time()
    Time = time.time() - gst
    
    # 노트 생성
    def sum_note(n_spot, note_sum_time):
        if n_spot == 1: # d
            n_d.append([-15, note_sum_time])
        if n_spot == 2: # f
            n_f.append([-15, note_sum_time])
        if n_spot == 3: # j
            n_j.append([-15, note_sum_time])
        if n_spot == 4: # k
            n_k.append([-15, note_sum_time])
            
    # 노트 판정
    def rating(tiledata):
        global perfect, great, good, miss
        if len(tiledata) >= 1 and tiledata[0][0] >= 650:
            if 790 <= tiledata[0][0] + 7.5 <= 820: # perfect
                tiledata.remove(tiledata[0])
                perfect += 1
            elif 770 <= tiledata[0][0] + 7.5 <= 840: # great
                tiledata.remove(tiledata[0])
                great += 1
            elif 740 <= tiledata[0][0] + 7.5 <= 870: # good
                tiledata.remove(tiledata[0])
                good += 1
            else: # miss
                tiledata.remove(tiledata[0])
                miss += 1

    while load: # 노트 소환
        pygame.display.flip()
        
        line = f.readline()
        
        if line == 'end':
            load = False
            ingame = True
        else:
            data_list.append(list(map(int, line.split('|'))))
            sum_note(data_list[0][0], note_start_time)
            note_start_time += 240 / bpm / data_list[0][1] - (240 / bpm / data_list[0][1]) / 98 * (12 / data_list[0][1])
            del data_list[0]
    
    while ingame:
        fpsclock.tick(60) # fps 설정
        
        
        keys[0] += (keyset[0] - keys[0]) / (2 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (2 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (2 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (2 * (maxframe / fps))

        
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0
                    
                    
        screen.fill((0, 0, 0))
        
        # 양쪽선
        pygame.draw.line(screen, (255, 255, 255), [660, 0], [660, 1080], 6)
        pygame.draw.line(screen, (255, 255, 255), [1260, 0], [1260, 1080], 6)
            
        # 판정선
        pygame.draw.line(screen, (255, 255, 255), [659, 800], [1261, 800], 1)
        pygame.draw.line(screen, (255, 255, 255), [659, 810], [1261, 810], 1)
        
        # 노트출력
        for i in n_d:
            i[0] += speed # 속도만큼 y좌표를 변경해서 노트가 내려간다.
            if i[0] < 960:
                pygame.draw.rect(screen, (255, 255, 255), [659, i[0], 150.5, 15])
            else:
                n_d.remove(i)
        for i in n_f:
            i[0] += speed
            if i[0] < 960:
                pygame.draw.rect(screen, (255, 255, 255), [809.5, i[0], 150.5, 15])
            else:
                n_f.remove(i)
        for i in n_j:
            i[0] += speed
            if i[0] < 960:
                pygame.draw.rect(screen, (255, 255, 255), [959.5, i[0], 150.5, 15]) 
            else:
                n_j.remove(i)
        for i in n_k:
            i[0] += speed
            if i[0] < 960:
                pygame.draw.rect(screen, (255, 255, 255), [1109.5, i[0], 150.5, 15])
            else:
                n_k.remove(i)
        
        # 화면 출력
        pygame.display.flip()




# 메인화면(UI, 배경화면 미확정)
running = True
def main():
    game_paused = False
    button = 1
    
    # 배경음악
    main_audio = pygame.mixer.Sound("audio\main_AUDIO.mp3") # 12Mornings
    main_audio.play(-1)
    
    while True:
        
        # 자투리 설정
        fpsclock.tick(60) # fps 설정
        font = pygame.font.SysFont('malgungothicsemilight', 80)
        
        
        # 배경화면
        screen.blit(pygame.image.load("img\main_BG.png"), (0, 0))
        
        
        # START 버튼
        if button == 1:
            text_start = font.render('START', True, (255, 255, 0))
        else:
            text_start = font.render('START', True, (255, 255, 255))
            
        text_start_size = text_start.get_rect().size # START 텍스트의 rect의 size 가져오기
        text_start_width = text_start_size[0] # 가로 사이즈
        text_start_height = text_start_size[1] # 세로 사이즈
        screen.blit(text_start, (960 - (text_start_width / 2), 650 - (text_start_height / 2)))
        
        # OPTION 버튼
        if button == 2:
            text_option = font.render('OPTION', True, (255, 255, 0))
        else:
            text_option = font.render('OPTION', True, (255, 255, 255))
            
        text_option_size = text_option.get_rect().size # OPTION 텍스트의 rect의 size 가져오기
        text_option_width = text_option_size[0] # 가로 사이즈
        text_option_height = text_option_size[1] # 세로 사이즈
        screen.blit(text_option, (960 - (text_option_width / 2), 800 - (text_option_height / 2)))
        
        # QUIT 버튼
        if button == 3:
            text_quit = font.render('QUIT', True, (255, 255, 0))
        else:
            text_quit = font.render('QUIT', True, (255, 255, 255))
            
        text_quit_size = text_quit.get_rect().size # OPTION 텍스트의 rect의 size 가져오기
        text_quit_width = text_quit_size[0] # 가로 사이즈
        text_quit_height = text_quit_size[1] # 세로 사이즈
        screen.blit(text_quit, (960 - (text_quit_width / 2), 950 - (text_quit_height / 2)))
        
        
        # 이벤트 루프
        for event in pygame.event.get():
            
            
            # 키다운 이벤트
            if event.type == pygame.KEYDOWN:
                
                # 위쪽 화살표를 눌렀을 때
                if event.key == pygame.K_UP:
                    if not button == 1:
                        button -= 1
                
                # 아래쪽 화살표를 눌렀을 때
                elif event.key == pygame.K_DOWN:
                    if not button == 3:
                        button += 1

                # 엔터키를 눌렀을 때
                elif event.key == pygame.K_RETURN:
                    if button == 1:
                        main_audio.stop()
                        choice()
                        return
                    if button == 2:
                        # main_audio.stop()
                        option()
                        return
                    if button == 3:
                        sys.exit()
        
        # 화면 출력
        pygame.display.update()



# 옵션화면(UI, 배경화면 미확정)
def option():
    while True:
        fpsclock.tick(60) # fps 설정 - 60
        
        # 스프라이트 설정
        screen.blit(pygame.image.load("img\option_BG.png"), (0, 0)) # 배경화면 출력
        
        
    
        # 화면 출력
        pygame.display.update()

play()