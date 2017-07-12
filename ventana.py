import pygame
import sys 
import pygame.locals
from pygame.constants import *


pygame.init()

mostrar = 1

class interfaz():
    
    def __init__(self):
        
        self.imagen = pygame.image.load("img/fondo1.jpg")
        self.fondo2 = pygame.image.load("img/fondo2.jpg")
        self.fondo3 = pygame.image.load("img/fondo3.jpg")
        self.fondo4 = pygame.image.load("img/fondo4.jpg")
        self.fondo5 = pygame.image.load("img/fondo5.jpg")
        
        self.btnjugar = pygame.image.load("img/botonjugar.png")

        self.regresar = pygame.image.load("img/botonvolver.jpg")
        self.primera_ctividad = pygame.image.load("img/primeractividad.jpg")
        self.segunda_actividad = pygame.image.load("img/segundactividad.jpg")
        self.tercera_actividad = pygame.image.load("img/terceraactividad.png")
        self.cuarta_actividad = pygame.image.load("img/cuartaactividad.png")
        self.quinta_actividad = pygame.image.load("img/quintaactividad.jpg")
        self.sexta_actividad = pygame.image.load("img/sextaatividad.jpg")
        self.final = pygame.image.load("img/final.png")
        
        self.btnsiguiente = pygame.image.load("img/btnsiguiente.jpg")
        self.fondoayuda = pygame.image.load("img/Ayuda.jpg")
        self.botonayuda = pygame.image.load("img/botonayuda.png")
        self.botonregresar = pygame.image.load("img/inicio.png")
        
        
       
 
    def inter_principal(self, superficie, texto):
        
        superficie.blit(self.imagen, (0,0))
       
        
        superficie.blit(self.btnjugar, (510,480))
        superficie.blit(self.botonayuda, (510,571))
   
       

        self.btnjugar = pygame.transform.scale(self.btnjugar,(120,60))
        
        self.botonayuda = pygame.transform.scale(self.botonayuda,(120,60))
      
 
    
    def poscision_elementos_1(self, superficie):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
      
        if (x_mouse > 510 and x_mouse <= 630) and (y_mouse > 482 and y_mouse < 540) :
            mostrar=2
        if (x_mouse > 510 and x_mouse <= 630) and (y_mouse > 571 and y_mouse < 647) :
            mostrar=6
  
        
    def interfaz_dos(self, superficie, texto):
        superficie.blit(self.primera_ctividad,(0,0))
        superficie.blit(self.btnsiguiente,(1000,810))

        self.btnsiguiente =pygame.transform.scale(self.btnsiguiente,(130,50))
  
    def poscision_elementos_2(self, superficie):
        global mostrar

    def interfaz_tres(self, superficie, texto):
        superficie.blit(self.segunda_actividad,(0,0))
        superficie.blit(self.btnsiguiente,(995,810))
       
        
        self.regresar =pygame.transform.scale(self.regresar,(150,80))
        
        
    def poscision_elementos_3(self, superficie):
        global mostrar
       
    def interfaz_cuatro(self, superficie, texto):
        
        superficie.blit(self.tercera_actividad,(0,0))
        superficie.blit(self.btnsiguiente,(995,810))

        
        self.regresar =pygame.transform.scale(self.regresar,(150,80))
        
    def poscision_elementos_4(self, superficie):
        global mostrar
            
        x_mouse, y_mouse = pygame.mouse.get_pos()  
        
        if (x_mouse > 5 and x_mouse <= 140) and (y_mouse > 10 and y_mouse < 60) :
            mostrar=5
      
    def interfaz_cinco(self, superficie, texto):
        
        superficie.blit(self.cuarta_actividad,(0,0))   
        superficie.blit(self.btnsiguiente,(995,810))
         
    def poscision_elementos_5(self, superficie):
        global mostrar 
        x_mouse, y_mouse = pygame.mouse.get_pos() 
        if (x_mouse >  39 and x_mouse <= 173) and (y_mouse > 23 and y_mouse < 52) :
            mostrar = 7  
       
    def interfaz_ayuda(self, superficie, texto):
        
        superficie.blit(self.fondoayuda,(0,0))   
        superficie.blit(self.botonregresar,(510,571))
        self.botonregresar =pygame.transform.scale(self.botonregresar,(100,100))
          
    def poscision_elementos_6(self, superficie):
        global mostrar           
    def interfaz_siete(self, superficie, texto):
       
        superficie.blit(self.quinta_actividad,(0,0))   
        superficie.blit(self.btnsiguiente,(995,810))
    def poscision_elementos_7(self, superficie):
        global mostrar 

    def interfaz_ocho(self, superficie, texto):
        
        superficie.blit(self.sexta_actividad,(0,0))
        superficie.blit(self.btnsiguiente,(995,810))
  
    def poscision_elementos_8(self, superficie):
        global mostrar      
       
    def interfaz_final(self, superficie, texto):
        
        superficie.blit(self.final,(0,0))
        superficie.blit(self.botonregresar,(600,600))
        self.botonregresar =pygame.transform.scale(self.botonregresar,(100,100))
        
    def poscision_elementos_9(self, superficie):
        global mostrar      
       
condicion=0
condicion2=0
condicion3=0
condicion4=0
condicion5=0
condicion6=0
condicion7=0
condicion8=0
condicion9=0
condicion10=0
condicion11=0
condicion12=0
condicion13=0
condicion14=0
condicion15=0
condicion16=0
condicion17=0
condicion18=0
mostrar2=0

def main():
    global mostrar
    global condicion
    global condicion2
    global condicion3
    global mostrar2
    global condicion4
    global condicion5
    global condicion6 
    global condicion7
    global condicion8
    global condicion9
    global condicion10
    global condicion11
    global condicion12
    global condicion13
    global condicion14
    global condicion15
    global condicion16
    global condicion17
    global condicion18
    siguiente=False
    
   
   
    
    x_mouse, y_mouse=pygame.mouse.get_pos()
 
    ventana = pygame.display.set_mode((1200,900))
    
    prin=interfaz()    
  
    botonmalo = pygame.image.load("img/botonmalo.png")
    botoncorrecto = pygame.image.load("img/botoncorrecto.png")
    btnincorreto = pygame.image.load("img/btnincorrecto.jpg")
    btncorrecto = pygame.image.load("img/btncorrecto.jpg")
    while True:
       
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if(mostrar==1):
                    prin.poscision_elementos_1(ventana)
                   
                if(mostrar==2):
                    prin.poscision_elementos_2(ventana)
 
                if(mostrar==3):
                    prin.poscision_elementos_3(ventana)
                if(mostrar==4):
                    prin.poscision_elementos_4(ventana)
                if(mostrar==5):
                    prin.poscision_elementos_5(ventana)
                if(mostrar==7):
                    prin.poscision_elementos_7(ventana)
                if(mostrar==8):
                    prin.poscision_elementos_8(ventana)
                if(mostrar==9):
                    prin.poscision_elementos_9(ventana)
            elif eventos.type == KEYDOWN:
                
                if eventos.key == K_ESCAPE:
                    
                    sys.exit(0)        
        
        x_mouse, y_mouse=pygame.mouse.get_pos()
        salida=str(x_mouse)+"----"+str(y_mouse)
        fuente_sistema=pygame.font.SysFont("comicsams",50)
        mi_texto=fuente_sistema.render(salida,True,(0,255,0))  
                       
        if(mostrar==1):
            prin.inter_principal(ventana,"Ventana principal")
            ventana.blit(mi_texto,(50,50))
            
            condicion=0
            condicion2=0
            condicion3=0
            condicion4=0
            condicion5=0
            condicion6=0
            condicion7=0
            condicion8=0
            condicion9=0
            condicion10=0
            condicion11=0
            condicion12=0
            condicion13=0
            condicion14=0
            condicion15=0
            condicion16=0
            condicion17=0
            condicion18=0
            mostrar2=0
            
            
            #print (x_mouse, y_mouse)
        elif (mostrar==2):
            prin.interfaz_dos(ventana, "Esta es mi ventana 2")
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            #siguiente = False
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN:
                    #check primero
                   
                    if (x_mouse > 127 and x_mouse <= 218) and (y_mouse > 375 and y_mouse < 460)and condicion==0:
                        condicion=1
                        siguiente=True
                        
                    if (x_mouse > 127 and x_mouse <= 218) and (y_mouse > 554 and y_mouse < 640)and condicion==0:
                        condicion=2
                        siguiente=True
                    if (x_mouse > 127 and x_mouse <= 216) and (y_mouse > 722 and y_mouse < 805)and condicion==0:
                        condicion=3
                        siguiente=True
                    
                     
                    elif (x_mouse >  1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente == True:
                            mostrar = 3
                            siguiente = False
                        else:
                            mostrar = 2
                        
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
                
            if (condicion==1):
                botonmalo =pygame.transform.scale(botonmalo,(88,80))
                ventana.blit(botonmalo,(130,378))
            if (condicion==2):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(88,80))
                ventana.blit(botoncorrecto,(130,558))
               
            if (condicion==3):
                botonmalo =pygame.transform.scale(botonmalo,(88,80))
                ventana.blit(botonmalo,(130,722))
                
        elif(mostrar==3):
            prin.interfaz_tres(ventana, "Esta es mi ventana 3")
            ventana.blit(mi_texto,(50,50))
             
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN:
                    if (x_mouse > 127 and x_mouse <= 218) and (y_mouse > 375 and y_mouse < 460)and condicion2==0:
                        condicion2=1
                        siguiente=True
                        
                    if (x_mouse > 127 and x_mouse <= 218) and (y_mouse > 554 and y_mouse < 640)and condicion2==0:
                        condicion2=2
                        siguiente=True
                        
                    if (x_mouse > 127 and x_mouse <= 216) and (y_mouse > 722 and y_mouse < 805) and condicion2==0 :
                        condicion2 = 3
                        siguiente=True
                        
                    elif (x_mouse >  1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente ==True:
                            mostrar = 4
                            siguiente = False
                        else:
                            mostrar= 3
                        
                        
                    
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
                
            if (condicion2==1):
                botonmalo =pygame.transform.scale(botonmalo,(88,80))
                ventana.blit(botonmalo,(130,378))
            if (condicion2==2):
                botonmalo =pygame.transform.scale(botonmalo,(88,80))
                ventana.blit(botonmalo,(130,558))
            if (condicion2==3):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(88,80))
                ventana.blit(botoncorrecto,(130,722))  
        elif(mostrar==4):
            prin.interfaz_cuatro(ventana, "Esta es mi ventana 4")
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN:
                    if (x_mouse > 863 and x_mouse <= 936) and (y_mouse > 149 and y_mouse < 230)and condicion3==0:
                        condicion3=1
                        
                    if (x_mouse > 972 and x_mouse <= 1043) and (y_mouse > 152 and y_mouse < 232)and condicion3==0:
                        condicion3=2
                        
                    if (x_mouse > 862 and x_mouse <= 936) and (y_mouse > 276 and y_mouse < 355)and condicion4==0:
                        condicion4=1
                        
                    if (x_mouse > 972 and x_mouse <= 1043) and (y_mouse > 274 and y_mouse < 354)and condicion4==0:
                        condicion4=2
                        
                    if (x_mouse > 862 and x_mouse <= 936) and (y_mouse > 389 and y_mouse < 471)and condicion5==0:
                        condicion5=1
                        
                    if (x_mouse > 972 and x_mouse <= 1043) and (y_mouse > 389 and y_mouse < 471)and condicion5==0:
                        condicion5=2
                        
                    if (x_mouse > 862 and x_mouse <= 936) and (y_mouse > 510 and y_mouse < 588)and condicion6==0:
                        condicion6=1
                        
                    if (x_mouse > 972 and x_mouse <= 1043) and (y_mouse > 510 and y_mouse < 588)and condicion6==0:
                        condicion6=2
                        
                    if (x_mouse > 862 and x_mouse <= 936) and (y_mouse > 625 and y_mouse < 705)and condicion7==0:
                        condicion7=1 
                        siguiente=True
                    if (x_mouse > 972 and x_mouse <= 1043) and (y_mouse > 625 and y_mouse < 705)and condicion7==0:
                        condicion7=2     
                        siguiente=True
                    if (x_mouse >  1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente== True:
                            mostrar=5
                            siguiente=False
                        else:
                            mostrar=4
                        
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
                
            if (condicion3==1):
                botonmalo =pygame.transform.scale(botonmalo,(75,85))
                ventana.blit(botonmalo,(863,151))
            if (condicion3==2):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(972,152))
            if (condicion4==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(862,274))
            if (condicion4==2):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(972,274))  
            if (condicion5==1):
                botonmalo =pygame.transform.scale(botonmalo,(75,85))
                ventana.blit(botonmalo,(862,389))    
            if (condicion5==2):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(973,389))
            if (condicion6==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(862,506))  
            if (condicion6==2):
                botonmalo =pygame.transform.scale(botonmalo,(75,85))
                ventana.blit(botonmalo,(972,510)) 
            if (condicion7==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(75,85))
                ventana.blit(botoncorrecto,(862,623))
            if (condicion7==2):
                botonmalo =pygame.transform.scale(botonmalo,(75,85))
                ventana.blit(botonmalo,(973,624))    
        elif(mostrar==5):
            prin.interfaz_cinco(ventana, "Esta es mi ventana ") 
            ventana.blit(mi_texto,(50,50))
            
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN:
                    if (x_mouse > 856 and x_mouse <= 927) and (y_mouse > 163 and y_mouse < 241)and condicion8==0:
                        condicion8=1
                        
                        
                    if (x_mouse > 962 and x_mouse <= 1036) and (y_mouse > 163 and y_mouse < 241)and condicion8==0:
                        condicion8=2
                       
                        
                    if (x_mouse > 856 and x_mouse <= 927) and (y_mouse > 276 and y_mouse < 355)and condicion9==0:
                        condicion9=1
                        
                        
                    if (x_mouse > 962 and x_mouse <= 1036) and (y_mouse > 276 and y_mouse < 355)and condicion9==0:
                        condicion9=2
                       
                        
                    if (x_mouse > 856 and x_mouse <= 927) and (y_mouse > 396 and y_mouse < 474)and condicion10==0:
                        condicion10=1
                        
                        
                    if (x_mouse > 962 and x_mouse <= 1036) and (y_mouse > 396 and y_mouse < 474)and condicion10==0:
                        condicion10=2
                        siguiente=True
                        
                    if (x_mouse > 856 and x_mouse <= 927) and (y_mouse > 512 and y_mouse < 591)and condicion11==0:
                        condicion11=1
                        
                         
                    if (x_mouse > 962 and x_mouse <= 1036) and (y_mouse > 512 and y_mouse < 591)and condicion11==0:
                        condicion11=2
                        
                        
                    if (x_mouse > 856 and x_mouse <= 927) and (y_mouse > 625 and y_mouse < 705)and condicion12==0:
                        condicion12=1
                        siguiente=True 
                        
                    if (x_mouse > 962 and x_mouse <= 1036) and (y_mouse > 625 and y_mouse < 705)and condicion12==0:
                        condicion12=2
                        siguiente=True     
                    
                    if (x_mouse >  1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente == True:
                            mostrar = 7
                            siguiente=False
                        else:
                            mostrar=5    
                        
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
        
            if (condicion8==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(73,82))
                ventana.blit(botoncorrecto,(857,160))
            if (condicion8==2):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(962,160))
            if (condicion9==1):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(856,275))
            if (condicion9==2):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(73,82))
                ventana.blit(botoncorrecto,(962,276))  
            if (condicion10==1):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(856,396))    
            if (condicion10==2):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(962,396))
            if (condicion11==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(73,82))
                ventana.blit(botoncorrecto,(856,512))  
            if (condicion11==2):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(962,512)) 
            if (condicion12==1):
                botoncorrecto =pygame.transform.scale(botoncorrecto,(73,82))
                ventana.blit(botoncorrecto,(856,625))
            if (condicion12==2):
                botonmalo =pygame.transform.scale(botonmalo,(73,82))
                ventana.blit(botonmalo,(962,625))  
            
        
        
        elif(mostrar==6):
            prin.interfaz_ayuda(ventana, "Esta es mi ventana ayuda ") 
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN: 
        
                    if (x_mouse > 536 and x_mouse <= 658) and (y_mouse > 572 and y_mouse < 720) :
                        mostrar=1 
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
            
                 
            
        elif(mostrar==7):
            prin.interfaz_siete(ventana, "Esta es mi sexta ventana ") 
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN: 
                    
                    if (x_mouse > 612 and x_mouse <= 780) and (y_mouse > 148 and y_mouse < 195)and condicion13==0:
                        condicion13=1 
                        
                        
                    elif (x_mouse > 612 and x_mouse <= 780) and (y_mouse > 254 and y_mouse < 301)and condicion13==0:
                        condicion13=2
                         
                        
                    if (x_mouse > 612 and x_mouse <= 780) and (y_mouse > 379 and y_mouse < 428)and condicion14==0:
                        condicion14=1
                       
                        
                    elif (x_mouse > 612 and x_mouse <= 786) and (y_mouse > 485 and y_mouse < 534)and condicion14==0:
                        condicion14=2
                          
                            
                    if (x_mouse > 615 and x_mouse <= 786) and (y_mouse > 599 and y_mouse < 647)and condicion15==0:
                        condicion15=1
                        siguiente=True  
                           
                    elif (x_mouse > 615 and x_mouse <= 786) and (y_mouse > 706 and y_mouse < 741)and condicion15==0:
                        condicion15=2
                        siguiente=True   
                         
                    if (x_mouse > 1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente == True:
                            mostrar=8
                            siguiente=False
                        else:
                            mostrar = 7    
                        
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
            if (condicion13==1):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(890,201))  
            if (condicion13==2):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(890,201))  
                
            if (condicion14==1):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(894,433))  
            if (condicion14==2):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(894,433)) 
            if (condicion15==1):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(894,652))
            if (condicion15==2):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(894,652))
         
         
        elif(mostrar==8):
            prin.interfaz_ocho(ventana, "Esta es mi septima ventana ") 
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN: 
                    
                    if (x_mouse > 628 and x_mouse <= 798) and (y_mouse > 154 and y_mouse < 202)and condicion16==0:
                        condicion16=1 
                       
                        
                    elif (x_mouse > 628 and x_mouse <= 798) and (y_mouse > 261 and y_mouse < 309)and condicion16==0:
                        condicion16=2
                        
                        
                    if (x_mouse > 620 and x_mouse <= 788) and (y_mouse > 385 and y_mouse < 434)and condicion17==0:
                        condicion17=1 
                       
                        
                    elif (x_mouse > 628 and x_mouse <= 788) and (y_mouse > 492 and y_mouse < 540)and condicion17==0:
                        condicion17=2 
                        
                           
                    if (x_mouse > 620 and x_mouse <= 789) and (y_mouse > 606 and y_mouse < 653)and condicion18==0:
                        condicion18=1 
                        siguiente=True
                        
                    elif (x_mouse > 620 and x_mouse <= 784) and (y_mouse > 712 and y_mouse < 743)and condicion18==0:
                        condicion18=2 
                        siguiente=True
                          
                    if (x_mouse > 1000 and x_mouse <= 1129) and (y_mouse > 810 and y_mouse < 860) :
                        if siguiente== True:
                            mostrar=9
                            siguiente=False   
                        else:
                            mostrar=8                         
                        
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        sys.exit(0)
            if (condicion16==1):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(907,208))            
            if (condicion16==2):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(906,208))  
            if (condicion17==1):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(897,440))    
            if (condicion17==2):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(897,440))  
            if (condicion18==1):
                btnincorrecto =pygame.transform.scale(btnincorreto,(170,50))
                ventana.blit(btnincorrecto,(898,659))  
            if (condicion18==2):
                btncorrecto =pygame.transform.scale(btncorrecto,(170,50))
                ventana.blit(btncorrecto,(898,659))                 
        elif(mostrar==9):
            prin.interfaz_final(ventana, "Esta es mi ventana final ") 
            ventana.blit(mi_texto,(50,50))
            x_mouse, y_mouse = pygame.mouse.get_pos()
            for eventos in pygame.event.get():
            
                if eventos.type == QUIT:
                    sys.exit(0)
                
                elif eventos.type == MOUSEBUTTONDOWN: 
                    
                    if (x_mouse > 598 and x_mouse <= 698) and (y_mouse > 647 and y_mouse < 702) :
                        mostrar = 1
        pygame.display.update()
                    
                    
if __name__ == '__main__':

    main()