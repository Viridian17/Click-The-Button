import pygame
import random
from random import randint
from tkinter import messagebox
import tkinter as tk 
import time
import sys

import pygame.image
x = 10
y = 10
a = randint(200,1000)
b = randint(100,600)
score=0
highscore=0
class MouseCords:
    def __init__(self,surface,x,y,font,color,pos):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.pos = pos
        self.surface = surface

        self.cord_text = self.font.render("["+str(int(x))+","+str(int(y))+"]",False,self.color)
        self.cord_text_rect = self.cord_text.get_rect(center=(self.pos[0],self.pos[1]))
    def render(self):
        self.surface.blit(self.cord_text,self.cord_text_rect)
    def update(self):
        text=f"[{x:2.0f},{y:2.0f}]"
        self.cord_text = self.font.render(text,False,self.color)
        self.cord_text_rect = self.cord_text.get_rect(center=(self.pos[0],self.pos[1]))
class ScoreCounter:
    def __init__(self,surface,font,color,pos,score):
        self.surface = surface
        self.font=font
        self.color=color
        self.pos=pos
        self.score=score
        self.score_text = self.font.render("Score: "+str(int(score)),False,self.color)
        self.score_text_rect = self.score_text.get_rect(center=(self.pos[0],self.pos[1]))
    def render(self):
        self.surface.blit(self.score_text,self.score_text_rect)
    def update(self):
        text=f"Score: {score:2.0f}"
        self.score_text = self.font.render(text,False,self.color)
        self.score_text_rect = self.score_text.get_rect(center=(self.pos[0],self.pos[1]))
class btn:
    def __init__(self, image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
    def randompos(self):
        self.rect.topleft = (randint(200,1000),randint(100,600))
pygame.font.init()
font = pygame.font.Font(None, 36)
WIDTH = 1366
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False
pressed = False
mousecord = MouseCords(screen,x,y,font,"black",(50,10))
pscore = ScoreCounter(screen,font,"black",[50,50],score)
button = btn("images/btn.png",(a,b))
def message_box(subject, content):  
    root = tk.Tk()  
    root.attributes("-topmost", True)  
    root.withdraw()  
    messagebox.showinfo(subject, content)  
    try:  
        root.destroy()  
    except:  
        pass
file_name = "score.txt"
with open(file_name, "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        if key=="highscore":
            highscore=int(value)
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:  
            done = True
        [ x, y ] = pygame.mouse.get_pos()
        with open(file_name, "w") as file:
            if score>highscore:
                file.write(f"highscore={score}\n")


        if pygame.mouse.get_pressed()[0]:
            if (x < button.rect.left or x > button.rect.right  or y < button.rect.top or y > button.rect.bottom) and pressed == False:
                if score>highscore:
                    message_box("Miss","Your score was: "+str(score)+" points!\n\nNew highscore!")
                if score<=highscore:
                    message_box("Miss","You missed.\n\nYour score was: "+str(score)+" points!\n\nYour highscore is "+str(highscore)+" points!")

                done = True
            elif button.rect.collidepoint([x,y]) and pressed == False:
                score += 1
                pressed = True
                button.randompos()
        if not(pygame.mouse.get_pressed()[0]):
            pressed = False
        screen.fill("white")
        screen.blit(button.image,button.rect)
        """mousecord.render()
        mousecord.update()"""
        pscore.render()
        pscore.update()
        pygame.display.flip()
        