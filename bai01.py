import RPi.GPIO as gpio
from time import sleep
import multiprocessing as mp

gpio.setwarnings(False)
pin14 = 14
pin15 = 14
queue = mp.Queue()

def blink_led(delay): 
    queue.put('blink_led')            
    print('blink_led')
    while True:
        gpio.output(pin14, gpio.HIGH)
        sleep(delay)
        gpio.output(pin14, gpio.LOW)
        sleep(delay)
# blink_led()
def blink_led_pwm(max_step):
    queue.put('blink_led_pwm')         
    print('blink_led_pwm')
    pi_pwm = gpio.PWM(pin15,1000)	
    pi_pwm.start(0)
    while True:
        for duty in range(0,max_step,1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.01)
#blink_led_pwm()
if __name__ == '__main__':
    # mp.set_start_method('spawn')  
    gpio.setmode(gpio.BCM)   
    gpio.setup(pin14, gpio.OUT)    

    gpio.setmode(gpio.BCM)   
    gpio.setup(pin15, gpio.OUT)      

    process_blink_led = mp.Process(target=blink_led, args=(0.2, ))
    process_blink_led_pwm = mp.Process(target=blink_led_pwm, args=(101, ))
    process_blink_led.start()
    process_blink_led_pwm.start()



