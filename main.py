import pygame, sys

# 초기화
pygame.init()

# 창 이름 설정
pygame.display.set_caption("main")

# 화면크기 설정
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN) # 화면크기 - 풀스크린


# fps
fpsclock = pygame.time.Clock()



# 노래선택
def choice():
    pass


# 메인화면
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
                        choice()
                        return
                    if button == 2:
                        option()
                        return
                    if button == 3:
                        sys.exit()
        
        # 화면 출력
        pygame.display.update()


    
# 옵션화면
def option():
    while True:
        fpsclock.tick(60) # fps 설정 - 60
        
        # 스프라이트 설정
        screen.blit(pygame.image.load("img\option_BG.png"), (0, 0)) # 배경화면 출력
        
        
    
        # 화면 출력
        pygame.display.update()

main()