import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import datetime
from threading import Thread
lcd = LCD.Adafruit_CharLCDPlate()
lcd.clear()
GPIO.setup(26, GPIO.OUT)
timecount= 0


    
def main():
    global timecount
    usercode = [0, 0, 0, 0, 0, 0]
    numactive = 0
    buttons = ( (LCD.SELECT, 'Select'),
                (LCD.LEFT,   'Left'  ),
                (LCD.UP,     'Up'    ),
                (LCD.DOWN,   'Down'  ),
                (LCD.RIGHT,  'Right' ) )
    lcd.set_color(1.0, 0.0, 0.0)
    lcdmsg0(usercode)
    while True:
        # Loop through each button and check if it is pressed.
        if timecount >= 120:
            timedisplayer()
            timecount = 0
            usercode = [0, 0, 0, 0, 0, 0]
            numactive = 0
            lcd.clear()
            lcdmsg0(usercode)
        for button in buttons:
            if lcd.is_pressed(button[0]):
                timecount = 0
                if button[1] == 'Left':
                    if numactive == 0:
                        numactive = 5
                        time.sleep(0.2)
                    else:
                        numactive -= 1
                        time.sleep(0.2)
                elif button[1] == 'Right':
                    if numactive == 5:
                        numactive = 0
                        time.sleep(0.2)
                    else:
                        numactive += 1
                        time.sleep(0.2)
                elif button[1] == 'Up':
                    if usercode[numactive] == 9:
                        usercode[numactive] = 0
                        lcd.clear()
                        lcdmsg0(usercode)
                        time.sleep(0.2)
                    else:
                        usercode[numactive] += 1
                        lcd.clear()
                        lcdmsg0(usercode)
                        time.sleep(0.2)
                elif button[1] == 'Down':
                    if usercode[numactive] == 0:
                        usercode[numactive] = 9
                        lcd.clear()
                        lcdmsg0(usercode)
                        time.sleep(0.2)
                    else:
                        usercode[numactive] -= 1
                        lcd.clear()
                        lcdmsg0(usercode)
                        time.sleep(0.2)
                elif button[1] == 'Select':
                    f = open('/home/pi/safe/code.txt')
                    f1 = f.read()
                    f.close()
                    if f1 == str(usercode[0]) + str(usercode[1]) + str(usercode[2]) + str(usercode[3]) + str(usercode[4]) + str(usercode[5]):
                        lcd.set_color(0.0, 1.0, 0.0)
                        GPIO.output(26, True)
                        lcd.clear()
                        lcd.message('code correct')
                        time.sleep(0.8)
                        lcd.clear()
                        lcd.message('Left: quit\nSel: change code')
                        x = 1
                        while x == 1:
                            for button in buttons:
                                if lcd.is_pressed(button[0]):
                                    if button[1] == 'Left':
                                        x = 0
                                    if button[1] == 'Select':
    #################################################################################
                                        x = 1
                                        numactive = 0
                                        usercode = [0, 0, 0, 0, 0, 0]
                                        lcd.clear()
                                        lcdmsg0(usercode)
                                        time.sleep(0.2)
                                        k = 1
                                        while k == 1:
                                            for button in buttons:
                                                if lcd.is_pressed(button[0]):
                                                    if button[1] == 'Left':
                                                        if numactive == 0:
                                                            numactive = 5
                                                            time.sleep(0.2)
                                                        else:
                                                            numactive -= 1
                                                            time.sleep(0.2)
                                                    elif button[1] == 'Right':
                                                        if numactive == 5:
                                                            numactive = 0
                                                            time.sleep(0.2)
                                                        else:
                                                            numactive += 1
                                                            time.sleep(0.2)
                                                    elif button[1] == 'Up':
                                                        if usercode[numactive] == 9:
                                                            usercode[numactive] = 0
                                                            lcd.clear()
                                                            lcdmsg0(usercode)
                                                            time.sleep(0.2)
                                                        else:
                                                            usercode[numactive] += 1
                                                            lcd.clear()
                                                            lcdmsg0(usercode)
                                                            time.sleep(0.2)
                                                    elif button[1] == 'Down':
                                                        if usercode[numactive] == 0:
                                                            usercode[numactive] = 9
                                                            lcd.clear()
                                                            lcdmsg0(usercode)
                                                            time.sleep(0.2)
                                                        else:
                                                            usercode[numactive] -= 1
                                                            lcd.clear()
                                                            lcdmsg0(usercode)
                                                            time.sleep(0.2)
                                                    elif button[1] == 'Select':
                                                        f = open('/home/pi/safe/code.txt', 'w')
                                                        f.write(str(usercode[0]) + str(usercode[1]) + str(usercode[2]) + str(usercode[3]) + str(usercode[4]) + str(usercode[5]))
                                                        f.close()
                                                        lcd.clear()
                                                        lcd.message('Left: quit\nSel: change code')
                                                        k = 0
                                                        time.sleep(0.2)
                                                               
#############################################################################################                                        

                        lcd.set_color(1.0, 0.0, 0.0)
                        GPIO.output(26, False)
                        p = 1
                    else:
                        lcd.clear()
                        lcd.message('code incorrect')
                        time.sleep(0.8)
                        p = 0
                    timecount = 0
                    lcd.clear()
                    usercode = [0, 0, 0, 0, 0, 0]
                    numactive = 0
                    lcdmsg0(usercode)
                    if p == 1:
                        time.sleep(0.2)
                    
    
def lcdmsg0(value):
    lcd.message(str(value[0]) + str(value[1]) + str(value[2]) + str(value[3]) + str(value[4]) + str(value[5]))

def timecounter():
    global timecount
    while True:
        time.sleep(1)
        timecount += 1
        
def timedisplayer():
    timechache = 0
    buttons = ( (LCD.SELECT, 'Select'),
                (LCD.LEFT,   'Left'  ),
                (LCD.UP,     'Up'    ),
                (LCD.DOWN,   'Down'  ),
                (LCD.RIGHT,  'Right' ) )
    x = 1
    while x == 1:
        if timechache != datetime.datetime.now().strftime("%Y-%m-%d %H:%M"):
            lcd.clear()
            lcd.message(datetime.datetime.now().strftime("%Y-%m-%d\n%H:%M"))
            timechache = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        for button in buttons:
            if lcd.is_pressed(button[0]):
                x = 0
                time.sleep(0.2)
    

Thread(target=main).start()
Thread(target=timecounter).start()
                    
