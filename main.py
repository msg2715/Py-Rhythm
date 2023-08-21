import pygame, sys

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



# 인게임 데모
def play():
    
    # 채보파일 읽고 데이터 저장
    f = open("Charts\m.txt", "r")
    n_type, n_spot, note_sum_time = f.readline().split(',')
    
    # 노트설정
    note_y = 0
    note_sum_time = 0
    speed = 2
    keys = [0, 0, 0, 0]
    keyset = [0, 0, 0, 0]
    
    # 노트
    n_d = []
    n_f = []
    n_j = []
    n_k = []
    
    # 노트 생성
    def sum_note():
        if n_spot == "d":
            n_d.append([note_y])
        if n_spot == "f":
            n_f.append([note_y])
        if n_spot == "j":
            n_j.append([note_y])
        if n_spot == "k":
            n_k.append([note_y])
    
    while True:
        fpsclock.tick(60) # fps 설정
        
        keys[0] += (keyset[0] - keys[0]) / (2 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (2 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (2 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (2 * (maxframe / fps))
        
        # 노트생성
        note = None
        
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
                if event.key == pygame.K_f:
                    keyset[1] = 1
                if event.key == pygame.K_j:
                    keyset[2] = 1
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    
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
        
        for tile_data in n_d:
            pass    
        
        # 양쪽선
        pygame.draw.line(screen, (255, 255, 255), [660, 0], [660, 1080], 6)
        pygame.draw.line(screen, (255, 255, 255), [1260, 0], [1260, 1080], 6)
            
        # 판정선
        pygame.draw.line(screen, (255, 255, 255), [659, 800], [1261, 800], 1)
        pygame.draw.line(screen, (255, 255, 255), [659, 810], [1261, 810], 1)
        
        # 화면 출력
        pygame.display.update()



# 메인화면(UI, 배경화면 미확정)
running = True
def main():
    game_paused = False
    button = 1
    
    # 배경음악
    main_audio = pygame.mixer.Sound("audio\main_AUDIO.mp3")
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
                        print(button)
                
                # 아래쪽 화살표를 눌렀을 때
                elif event.key == pygame.K_DOWN:
                    if not button == 3:
                        button += 1
                        print(button)

                # 엔터키를 눌렀을 때
                elif event.key == pygame.K_RETURN:
                    if button == 1:
                        main_audio.stop()
                        choice()
                        return
                    if button == 2:
                        main_audio.stop()
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