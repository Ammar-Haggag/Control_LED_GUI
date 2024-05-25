import tkinter as gui
import time
import RPi.GPIO as GPIO
import threading

LED=21 #number of output pin

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #or GPIO.BOARD
GPIO.setup(21,GPIO.OUT)

x=0 #intial state of led

def LED_Toggle():
    global x

    x^=1 #xor or toggle
    
    GPIO.output(LED,x)
    if x==1 :
        LEDView=gui.Button(main_window,text="   LED   ",command=LED_Toggle,bg="green") #to show state of LED
        LEDView.place(x=170,y=35)
    else :
        LEDView=gui.Button(main_window,text="   LED   ",command=LED_Toggle,bg="white")
        LEDView.place(x=170,y=35)
        

main_window=gui.Tk()

LEDView=gui.Button(main_window,text="   LED   ",command=LED_Toggle,bg="white")
LEDView.place(x=170,y=35)

#for toggle screen // shell

main_window.title("LED toggle")
main_window.geometry("400x200+500+300")
main_window.resizable(False,False)
main_window.configure(background="#300924")

#for toggle button
buttontoggle=gui.Button(main_window,text="      LED Toggle      ",command=LED_Toggle,bg="yellow")
buttontoggle.place(x=140,y=100)

main_window.mainloop()
