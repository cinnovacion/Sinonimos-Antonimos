import pygame
import sys
import pygame.locals
from pygame.constants import *

class interfaz():
    
    def __init__(self):
        
        self.imagen1 = pygame.image.load("img/boton_1.fw.png")
        self.imagen2 = pygame.image.load("img/boton_2.fw.png")
        self.imagen3 = pygame.image.load("img/boton_3.fw.png") 
        self.fuente_sistema=pygame.font.SysFont("comicsansms",50)
        self.imagen4 = pygame.image.load("img/sabiduria.png")
        self.regresar = pygame.image.load("img/regresar.fw.png")
        
        
         
    def inter_principal(self, superficie, texto):
        
        mi_texto=self.fuente_sistema.render(texto,True,(0,255,0))
        superficie.blit(self.imagen1, (50,0))
        superficie.blit(self.imagen2, (50,200))
        superficie.blit(self.imagen3, (50,500))
        superficie.blit(mi_texto,(300,50))
        
    
    def poscision_elementos_1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 50 and x_mouse <= 276) and (y_mouse > 0 and y_mouse < 78) :
            superficie.fill((255,255,255))
                
        elif (x_mouse > 50 and x_mouse <= 276) and (y_mouse > 200 and y_mouse < 278):
            superficie.fill((0,0,0)) 
                    
        elif (x_mouse > 50 and x_mouse <= 276) and (y_mouse > 500 and y_mouse < 578):
            superficie.fill((57,111,67))
                    
                    #ventana.blit(imagen1, (450,0))
            ocultar = 2
        
    def interfaz_dos(self, superficie, texto):
        mi_texto=self.fuente_sistema.render(texto,True,(0,255,0))
        superficie.blit(self.imagen4, (150,0))
        superficie.blit(self.regresar, (50,0))
        superficie.blit(mi_texto,(300,50))
        
    def poscision_elementos_2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 50 and x_mouse <= 276) and (y_mouse > 0 and y_mouse < 78) :
            superficie.fill((255,255,255))
            ocultar = 1
            
    
 