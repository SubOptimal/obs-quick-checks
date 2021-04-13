#!/usr/bin/python3

'''
A simple test script to verify the function of the ultrasonic sensors.
'''

import RPi.GPIO as GPIO
import time

TRIG_PIN = 15
ECHO_PIN = 14

try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TRIG_PIN, GPIO.OUT)
  GPIO.setup(ECHO_PIN, GPIO.IN)

  echo_start = 0
  echo_end = 0

  while True:
      GPIO.output(TRIG_PIN, GPIO.LOW)
      time.sleep(0.5)

      GPIO.output(TRIG_PIN, GPIO.HIGH)
      time.sleep(0.00002)
      GPIO.output(TRIG_PIN, GPIO.LOW)

      while GPIO.input(ECHO_PIN) == GPIO.LOW:
          echo_start = time.time_ns()

      while GPIO.input(ECHO_PIN) == GPIO.HIGH:
          echo_end = time.time_ns()

      echo_duration = echo_end - echo_start

      distance = (echo_duration / 2) * 0.00003436

      if 21 <= distance < 800:
          print('distance: %.2f cm' % distance)
      else:
          print('*')
except KeyboardInterrupt:
    GPIO.cleanup()
