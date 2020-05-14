#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame

BLACK = (0, 0, 0)
pad_width = 1024
pad_height = 600


# In[2]:


def back(x, y):
    global gamepad, background
    gamepad.blit(background, (x, y))


# In[3]:


def horses(x, y):
    global gamepad, horse
    gamepad.blit(horse, (x, y))


# In[4]:


def darkness(x, y):
    global gamepad, dark
    gamepad.blit(dark, (x, y))


# In[5]:


def runGame():
    global gamepad, horse, clock, background, dark
    x = -1300
    y = -650
    y_change = 0
    x_change = 0
    pygame.mixer.music.load("Dracula_theme.mp3")
    pygame.mixer.music.play(-1)
    
    
    cnt = True
    while cnt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cnt = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change =- 7
                elif event.key == pygame.K_UP:
                    y_change = 7
                elif event.key == pygame.K_LEFT:
                    x_change = 7
                elif event.key == pygame.K_RIGHT:
                    x_change =- 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    y_change = 0
                    x_change = 0
        y += y_change
        x += x_change        
        
        gamepad.fill(BLACK)
        back(x, y)
        horses(400, 90)
        darkness(-525, -700)
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    quit()


# In[6]:


def initGame():
    global gamepad, horse, clock, background, dark
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Who am I? (feat. Dracula) _ Made by MBTMI')
    horse = pygame.image.load('horse.png')
    background = pygame.image.load('map.jpg')
    dark = pygame.image.load('dark.png')
    clock = pygame.time.Clock()
    runGame()


# In[1]:


import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# In[ ]:


initGame()

