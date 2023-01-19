from time import sleep
from gpiozero import Motor
import RPi.GPIO as GPIO
import pygame

pygame.init()
screen = pygame.display.set_mode((50,50))
# pines
BTN_PAUSA = 22
ENCODER = 18
# Pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PAUSA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ENCODER, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

mylcd = I2C_LCD_driver.lcd()
motor = Motor(forward=20, backward=16)
mylcd.lcd_display_string("Bienvenido", 1, 2)
menu = 1
vueltas = 0
sentido = 1
velocidad = 0
flag = False

#Funcion del motor
def arrancar(velocidad, sentido, vueltas_1):
    global vueltas
    global flag
    print('entre')
    print(vueltas, vueltas_1)
    while vueltas != vueltas_1:
        if flag == False:
            mylcd.lcd_display_string("Numero de vuelta",1,)
            mylcd.lcd_display_string(" "+(str(vueltas_1 - vueltas) +" "),2,6)
            if sentido == 1:
                if velocidad == 10 or velocidad == 20:
                    motor.forward(0.3)
                    sleep(0.25)
                motor.forward(velocidad/100)
            if sentido == 2:
                if velocidad == 10 or velocidad == 20:
                    motor.backward(0.3)
                    sleep(0.25)
                motor.backward(velocidad/100)
        elif flag == True:
            motor.backward(0)
            motor.forward(0)
            mylcd.lcd_display_string("***** STOP *****", 1, 0)
            for i in range (0,20,1) :
                mylcd.lcd_display_string((str(20-i)+" s "), 2, 6)
                sleep(1)
            flag = False
    motor.backward(0)
    motor.forward(0)
#Funcion de boton de pausa    
def pausa(pausa):
    global flag
    flag=True
GPIO.add_event_detect(BTN_PAUSA, GPIO.RISING, callback=pausa,bouncetime=200)

#Funcion del Encoder   
def contar(sensor):
    global vueltas
    vueltas += 1
GPIO.add_event_detect(ENCODER, GPIO.RISING, callback=contar,bouncetime=200)

#Funcion del menu principal
def upmenu():
    global sentido, velocidad, vueltas
    if menu == 1:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("PWM            *", 1, 0)
        mylcd.lcd_display_string("Sentido giro    ", 2, 0)
    if menu == 2:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("PWM             ", 1, 0)
        mylcd.lcd_display_string("Sentido giro   *", 2, 0)
    if menu == 3:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("#Vueltas       *", 1, 0)
        mylcd.lcd_display_string("PWM             ", 2, 0)
    if menu == 4:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("#Vueltas        ", 1, 0)
        mylcd.lcd_display_string("PWM            *", 2, 0)
    if menu == 5:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Sentido giro   *", 1, 0)
        mylcd.lcd_display_string("#Vueltas        ", 2, 0)
    if menu == 6:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Sentido giro    ", 1, 0)
        mylcd.lcd_display_string("#Vueltas       *", 2, 0)
    print(sentido, vueltas, velocidad)

# Funcion para PWM
def PWM():
    global velocidad
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Ingrese el %:", 1, 1)
    a = int(input('Escribe un valor numérico: '))
    try:
        if a % 10 == 0:
            result = str(a)
            velocidad = a
            mylcd.lcd_display_string(result+"%", 2, 3)
        else:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("SYNTAX ERROR", 1, 2)
    except ValueError:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("SYNTAX ERROR", 1, 2)
    sleep(2)
        
# Funcion para sentido de giro
def NS():
    global sentido
    mylcd.lcd_clear()
    mylcd.lcd_display_string ("1.Derecha         ",1,0)
    mylcd.lcd_display_string ("2.Izquierda        ",2,0)
    opcion=int(input("Que giro desea:"))
    if opcion==1:
        print("derecha")
        mylcd.lcd_display_string ("1.Derecha      *",1,0)
        sentido=1
    if opcion==2:
        print("izquierda")
        mylcd.lcd_display_string ("2.Izquierda    *",2,0)
        sentido=2
    sleep(2)

# Funcion #vueltas
def Vuelta():
    global vueltas, sentido, velocidad
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Ingrese el #:", 1, 1)
    v = int(input('Escribe el numero de vueltas '))
    conta = 0
    vueltas = conta
    arrancar(velocidad, sentido, v)
    sleep(2)

# Funcion para la accion
def action():
    if menu == 1 or menu == 4:
        PWM()
    if menu == 2 or menu == 5:
        NS()
    if menu == 3 or menu == 6:
        Vuelta()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up1")
                menu-=1
                upmenu()
                sleep(0.1)
            if event.key == pygame.K_DOWN:
                print("down1")
                menu+=1
                upmenu()
                sleep(0.1)
            if menu<1 :
                menu=6
                upmenu()
            if menu>6 :
                menu=1
                upmenu()
            if event.key == pygame.K_RETURN:
                action()
                upmenu()
                sleep(0.1)