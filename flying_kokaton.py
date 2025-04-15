import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False) #練習8
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr
        if tmr == 3200: tmr = 0 #練習9
        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_img2,[-x+1600,0]) #練習7
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1
        key_lst = pg.key.get_pressed() #練習9
        h = 0
        v = 0
        if key_lst[pg.K_UP]:
            h = 0
            v = -1
        elif key_lst[pg.K_DOWN]:
            h = 0
            v = +1
        elif key_lst[pg.K_LEFT]:
            h = -2
            v = 0
        elif key_lst[pg.K_RIGHT]:
            h = +1
            v = 0
        elif not key_lst[pg.K_RIGHT]:
            h = -1
            v = 0
        kk_rct.move_ip((h,v))
                
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()