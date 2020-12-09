#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,random,Game_Modes,Start_Screen,itertools 
 
Scores = 0
Golds_number = 0

# The background of the game
class Game_Map() :
    def __init__(self,x,y,Background_Image) :
        self.x = x
        self.y = y
        self.Background_Image = Background_Image

    def Map_Move(self):
        if self.x < -(Screen_Width-8) :  
            self.x = 0   
        else:
            self.x -= 8  
        Screen.blit(pygame.image.load(self.Background_Image).convert_alpha(),(self.x, self.y))

# The role of the game
class Game_Role():
    def __init__(self,Role_Image) :  
        self.rect = pygame.Rect(10,Lowest_y,0,0)
        self.Role_Image = Role_Image
        self.Jump_Height = Highest_y
        self.Jump_Start_Position = Lowest_y
        self.Jump_Control = False
        self.Image = (pygame.image.load(self.Role_Image[0]).convert_alpha()\
                      ,pygame.image.load(self.Role_Image[1]).convert_alpha()\
                          ,pygame.image.load(self.Role_Image[2]).convert_alpha()\
                              ,pygame.image.load(self.Role_Image[3]).convert_alpha()\
                                  ,pygame.image.load(self.Role_Image[4]).convert_alpha()\
                                     , pygame.image.load(self.Role_Image[5]).convert_alpha())
        self.rect.size = self.Image[0].get_size()
        self.rect.width -= 50
        self.rect.height -= 50
        self.Jump_Control_Twist = False
        self.jumpValue = 0
    
    def Jump(self):
        Jump_Sound.play()
        self.Jump_Control = True
    
    def Action_Move(self) : 
        if self.Jump_Control == True and self.Jump_Control_Twist == False :
            self.rect.y -= Jump_Speed
            if self.rect.y <= self.Jump_Height :
                self.Jump_Control = False
                self.Jump_Control_Twist = True
        elif self.Jump_Control_Twist == True :
            self.rect.y += (Jump_Speed - 2)
            if self.rect.y >= self.Jump_Start_Position :
                self.Jump_Control_Twist = False
 
            
    def Draw_Role(self,i) :
        # self.Index = next(self.IndexGen)
        if self.Jump_Start_Position <= self.rect.y :
            Screen.blit(self.Image[i],(self.rect.x, self.rect.y))  
        else  :
            Screen.blit(self.Image[5],(self.rect.x, self.rect.y))
            
# The barriers of the game
class Barriers() :
    def __init__(self,Barriers_Images) :   
        self.rect = pygame.Rect(800,0,0,0)  
        self.Barriers_Images = Barriers_Images
        Random_Number =  random.randint(0,3)
        if Random_Number == 0 :         
            self.Image = (pygame.image.load(self.Barriers_Images[0][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[0][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[0][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[0][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[0][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = (pygame.image.load(self.Barriers_Images[1][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[1][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[1][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[1][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[1][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 2 :
            self.Image = (pygame.image.load(self.Barriers_Images[2][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[2][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[2][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[2][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[2][4]).convert_alpha())
            self.rect.y = Highest_y 
        elif Random_Number == 3 :
            self.Image = (pygame.image.load(self.Barriers_Images[3][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[3][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[3][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[3][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[3][4]).convert_alpha())
            self.rect.y = Highest_y 
        self.rect.size = self.Image[0].get_size()
        self.rect.width -= 80
        self.rect.height -= 80
        self.Barriers_Index = itertools.cycle([0,1,2,3,4])
        self.Score = 1
 
    def Move(self) :
        self.rect.x -= 8
        
    def Draw_Barriers(self) :
        Index = next(self.Barriers_Index)
        Screen.blit(self.Image[Index], (self.rect.x, self.rect.y))
        
    def getScore(self):
        Temporary_Score = self.Score
        if Temporary_Score == 1 :
            Get_Score.play()
        self.Score = 0
        return Temporary_Score
    
class Golds():
    def __init__(self,Golds_Images) :   
        self.rect = pygame.Rect(750,0,0,0)  
        self.Golds_Images = Golds_Images
        self.active = True  
        Random_Number =  random.randint(0,1)
        if Random_Number == 0 :         
            self.Image = pygame.image.load(self.Golds_Images).convert_alpha()
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = pygame.image.load(self.Golds_Images).convert_alpha()
            self.rect.y = Highest_y + 10
        self.rect.size = self.Image.get_size()
        self.Score = 1   
        
    def Draw_Golds(self) :
        if pygame.sprite.collide_rect(Role,self) :
            Screen.blit(pygame.image.load("Images/Barriers/Nothing_1.png").convert_alpha(), (self.rect.x, self.rect.y))
        else :
            Screen.blit(self.Image, (self.rect.x, self.rect.y))
    
    def Move(self) :
        self.rect.x -= 8
    
    def getScore(self):
        Temporary_Score = self.Score
        self.Score = 0
        return Temporary_Score

def Game_Main(P_Screen_Width,P_Screen_Height,P_Highest_y,P_Lowest_y,P_Background,P_Background_Sound,P_Barriers_Images):
    global  Screen_Width,Screen_Height,Jump_Speed,Highest_y,Lowest_y,Jump_Sound,\
        Game_Run_Sound,Get_Score,Screen,Background_Images,Scores,Golds_number,Role
    Screen_Width = P_Screen_Width
    Screen_Height = P_Screen_Height
    Jump_Speed = 8  
    Highest_y = P_Highest_y
    Lowest_y = P_Lowest_y    
    # Local variables
    Fps = 30
    Distance = 0
    Gold_Lists = []
    Barriers_Time = 0 
    Barriers_List = []
    Golds_Time = 0
    Role_Image_Time = -1
    # Initialising pygame
    pygame.init()
    pygame.mixer.init() 
    # The sounds of the game
    Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
    Game_Run_Sound = pygame.mixer.Sound(P_Background_Sound)
    Get_Score = pygame.mixer.Sound("Sounds/Get_Score.wav")
    Dead_Bgm = pygame.mixer.Sound("Sounds/Dead.mp3")
    Gold_sound = pygame.mixer.music.load("Sounds/gold_ggg.mp3")
    # The images of the game
    Role_Image_Action = ["Images/Roles/Role_Run_1.png","Images/Roles/Role_Run_2.png","Images/Roles/Role_Run_3.png"\
                         ,"Images/Roles/Role_Run_4.png","Images/Roles/Role_Run_5.png","Images/Roles/Role_Jump.png"]
    Golds_Images = "Images/Barriers/Gold_1.png" 
    Barriers_Images = P_Barriers_Images
    
    Background = P_Background
    Game_Over_Image = pygame.image.load("Images/Game_Over.png").convert_alpha()
    Game_Over_Width = Game_Over_Image.get_width()
    Game_Over_Height = Game_Over_Image.get_height()
    Return_Button = Start_Screen.Button("Play Again", (255,255,255), Screen_Width/2 , Lowest_y)
    # Creat the display with Screen_Width and Screen_Height
    Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
    # Set the title of the game
    pygame.display.set_caption("CWG's Game")   
    Role = Game_Role(Role_Image_Action)
    Fps_Flash = pygame.time.Clock()
    Bg = Game_Map(0,0,Background)  
    Game_Run_Sound.play(-1,0)
    Game_Over = False  

    while True : 
        if Game_Over == False :
            
            Distance += 1
            Role_Image_Time += 1
            Bg.Map_Move()
            Role.Action_Move()  
            if Role_Image_Time == 0 :
                Role.Draw_Role(0)
            elif Role_Image_Time == 1 :
                Role.Draw_Role(1)
            elif Role_Image_Time == 2 :
                Role.Draw_Role(2)
            elif Role_Image_Time == 3 :
                Role.Draw_Role(3)
            elif Role_Image_Time == 4 :
                Role.Draw_Role(4)
                Role_Image_Time = -1         
            #########################################        
            if Golds_Time >= 800 :
                r=random.randint(0,100)
                if r <= 10 :
                    Gold = Golds(Golds_Images) 
                    Gold_Lists += [Gold]
                    Golds_Time = 0
            for i in range(len(Gold_Lists)) :
                Gold_Lists[i].Move()            
                Gold_Lists[i].Draw_Golds()               
                if pygame.sprite.collide_rect(Role,Gold_Lists[i]) :
                    Get_Score.play()
                    Golds_number += Gold_Lists[i].getScore()
                    Start_Screen.Show(Screen,"Gold +1",0,0)
                    
            if Barriers_Time >= 1000 :
                r=random.randint(0,100)
                if r <= 40 :
                    Barrier = Barriers(Barriers_Images)
                    Barriers_List += [Barrier]
                    Barriers_Time = 0        
            #########################################
            
            for i in range(len(Barriers_List)) :
                Barriers_List[i].Move() 
                Barriers_List[i].Draw_Barriers()              
                if pygame.sprite.collide_circle(Role,Barriers_List[i]) :
                    Game_Over = True
                    Game_Run_Sound.stop()
                    Dead_Bgm.play()
                    Scores =  Scores + Golds_number * 5
                    Start_Screen.Show(Screen,f"You ran {Distance} meters and got {Golds_number} Golds ,{Scores} scores!",0,0)
                    Screen.blit(Game_Over_Image,((Screen_Width/2-Game_Over_Width/2),(Screen_Height/2-Game_Over_Height/2)))
                    pygame.draw.rect(Screen, (0,0,0),[Screen_Width/2, Lowest_y, 130, 40])
                    Return_Button.display()
                    break
                elif (Barriers_List[i].rect.x + Barriers_List[i].rect.size[0]) < Role.rect.x :
                        Scores += Barriers_List[i].getScore()    
        #########################################                
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()# for the rest of the people with windows or Linux
                os._exit(0) # for Mac users.
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                    Role.Jump()                   
        ######################################
        if pygame.mouse.get_pressed()[0]:            
            if Return_Button.check_click(pygame.mouse.get_pos()):
                Game_Run_Sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()                
                os._exit(0)    
        Barriers_Time += 20
        Golds_Time += 30            
        pygame.display.flip()      
        Fps_Flash.tick(Fps)
        
