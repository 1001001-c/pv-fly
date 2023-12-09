import pygame
import sys
import random

import threading

runway_img = pygame.image.load('./images/飞机跑道.png')

# 定义信号量
semaphore = threading.Semaphore(1)


def draw_text(screen, text, position, font_size=36):
    # 创建Font对象
    font = pygame.font.Font(None, font_size)
    # 渲染文本
    text_surface = font.render(text, True, (0, 0, 0))
    # 绘制文本
    screen.blit(text_surface, position)


def land(screen, start_x, end_x, end_y, speed, plane_id):
    # P操作
    semaphore.acquire()

    # 设置窗口大小
    width, height = 925, 400

    # 载入飞机和跑道的图片
    plane_img = pygame.image.load('./images/飞机1.png')
    # 获取飞机的尺寸
    plane_size = plane_img.get_rect().size
    plane_width = plane_size[0]
    plane_height = plane_size[1]

    # 飞机的初始位置和速度
    start_y = 0
    plane_speed = 5
    plane_x = start_x
    plane_y = start_y
    running = True
    while running and (plane_x < end_x or plane_y < end_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((135, 206, 235))  # 填充为天蓝色背景
        screen.blit(runway_img, (0, screen.get_height() - runway_img.get_height()))  # 绘制跑道，底部对齐
        screen.blit(plane_img, (plane_x, plane_y))  # 绘制飞机
        draw_text(screen, f"Flight {plane_id} landing", (plane_x + 20, plane_y - 30))  # 在飞机上方显示编号

        pygame.display.flip()  # 更新屏幕显示
        if plane_y < end_y and plane_x < end_x:
            plane_y += 0.5 * speed
            plane_x += speed
            # 否则，只进行水平移动
        else:
            if plane_x < end_x:
                plane_x += speed
        pygame.time.Clock().tick(30)  # 控制帧率
    # V操作，
    semaphore.release()


def take_off(screen, start_x, end_x, end_y, speed, plane_id):
    # P操作
    semaphore.acquire()

    # 设置窗口大小
    width, height = 925, 400

    # 载入飞机和跑道的图片
    plane_img = pygame.image.load('./images/飞机4.png')
    # 获取飞机的尺寸
    plane_size = plane_img.get_rect().size
    plane_width = plane_size[0]
    plane_height = plane_size[1]

    # 飞机的初始位置和速度
    start_y = height - 100 + 10
    plane_speed = 5
    plane_x = start_x
    plane_y = start_y
    running = True
    while running and (plane_x > end_x or plane_y > end_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((135, 206, 235))  # 填充为天蓝色背景
        screen.blit(runway_img, (0, screen.get_height() - runway_img.get_height()))  # 绘制跑道，底部对齐
        screen.blit(plane_img, (plane_x, plane_y))  # 绘制飞机
        draw_text(screen, f"Flight {plane_id} taking off", (plane_x + 20, plane_y - 30))  # 在飞机上方显示编号

        pygame.display.flip()  # 更新屏幕显示
        # 如果飞机没有到达指定的end_y高度，则继续向上移动
        if plane_x > 700:
            plane_x -= speed
        elif plane_y > end_y and plane_x > end_x:
            plane_y -= 0.5 * speed
            plane_x -= speed
        # 否则，只进行水平移动
        else:
            if plane_x > end_x:
                plane_x -= speed
        pygame.time.Clock().tick(30)  # 控制帧率
    semaphore.release()


def create_plane_threads():
    pygame.init()

    # 设置窗口大小
    width, height = 925, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('飞机跑道动画')

    # 载入飞机和跑道的图片
    plane_img = pygame.image.load('./images/飞机1.png')
    # 获取飞机的尺寸
    plane_size = plane_img.get_rect().size
    plane_width = plane_size[0]
    plane_height = plane_size[1]

    # 飞机的初始位置和速度
    plane_speed = 5

    # 创建飞机线程
    plane_threads = []
    landing_thread = threading.Thread(target=land, args=(screen,
                                                         -plane_width, width, 400 - plane_height, plane_speed, "CA123"))
    taking_off_thread = threading.Thread(target=take_off, args=(screen,
                                                                width - plane_width, -plane_width, 0, plane_speed,
                                                                "CA456"))
    landing_thread2 = threading.Thread(target=land, args=(screen,
                                                          -plane_width, width, 400 - plane_height, plane_speed,
                                                          "CA789"))
    taking_off_thread2 = threading.Thread(target=take_off, args=(screen,
                                                                 width - plane_width, -plane_width, 0, plane_speed,
                                                                 "CA012"))
    plane_threads.extend([landing_thread, taking_off_thread, landing_thread2, taking_off_thread2])
    # 启动飞机线程
    for thread in plane_threads:
        thread.start()

    # 等待所有飞机线程结束
    for thread in plane_threads:
        thread.join()


if __name__ == "__main__":
    # 进行多次起飞和降落
    for _ in range(10):
        create_plane_threads()
    # 退出pygame
    pygame.quit()
    sys.exit()
