import pygame
import sys

def draw_text(screen, text, position, font_size=36):
    # 创建Font对象
    font = pygame.font.Font(None, font_size)
    # 渲染文本
    text_surface = font.render(text, True, (0, 0, 0))
    # 绘制文本
    screen.blit(text_surface, position)
def land(screen, plane_img, start_x, start_y, end_x, speed, plane_id):
    plane_x = start_x
    plane_y = start_y
    running = True
    while running and plane_x < end_x:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # 填充背景色
        screen.blit(runway_img, (0, 90))  # 绘制跑道
        screen.blit(plane_img, (plane_x, plane_y))  # 绘制飞机
        draw_text(screen, f"land Flight {plane_id}", (plane_x + 20, plane_y - 30))  # 在飞机上方显示编号

        pygame.display.flip()  # 更新屏幕显示
        plane_x += speed  # 更新飞机位置
        pygame.time.Clock().tick(30)  # 控制帧率

def take_off(screen, plane_img, start_x, start_y, end_x, speed, plane_id):
    plane_x = start_x
    plane_y = start_y
    running = True
    while running and plane_x > end_x:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # 填充背景色
        screen.blit(runway_img, (0, 90))  # 绘制跑道
        screen.blit(plane_img, (plane_x, plane_y))  # 绘制飞机
        draw_text(screen, f"land Flight {plane_id}", (plane_x + 20, plane_y - 30))  # 在飞机上方显示编号
        pygame.display.flip()  # 更新屏幕显示
        plane_x -= speed  # 更新飞机位置
        pygame.time.Clock().tick(30)  # 控制帧率

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 925, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('飞机跑道动画')

# 载入飞机和跑道的图片
plane_img = pygame.image.load('./images/飞机1.png')
runway_img = pygame.image.load('./images/飞机跑道.png')

# 获取飞机的尺寸
plane_size = plane_img.get_rect().size
plane_width = plane_size[0]
plane_height = plane_size[1]

# 飞机的初始位置和速度
start_y = 90
plane_speed = 5

# 执行降落和起飞动作
land(screen, plane_img, -plane_width, start_y, width, plane_speed, "CA123")
take_off(screen, plane_img, width - plane_width, start_y, -plane_width, plane_speed, "CA123")

# 退出pygame
pygame.quit()
sys.exit()
