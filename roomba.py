# Python script for roomba serial interface
# This script is meant to be run in interactive mode:
#   python -i roomba.py
import serial
import sys
import time

port = "/dev/ttyUSB0"
s = serial.Serial(port, 115200)
print "Starting interface"
s.write(bytearray([128])) 
print "Roomba ready"

def send(bs):
  s.write(bytearray(bs))

def safeMode():
  send([131])
  time.sleep(0.1)

def clean():
  print "Start cleaning"
  send([135])

def playNote():
  safeMode()
  print "Playing a note"
  send([140, 0, 1, 62, 32])
  time.sleep(0.1)
  send([141, 0])

def noLED():
  safeMode()
  send([139, 0, 0, 0])

def allLED():
  safeMode()
  print "Lighting all LEDs"
  send([139, 15, 0, 255])

def setDayTime(day, hour, minute):
  print "Setting day/time:", day, hour, ":", minute
  send([168, day, hour, minute]) 

def scheduleEveryDay(hour, minute):
  print "Scheduling every day at", hour, ":", minute
  send([167, 127, hour, minute, hour, minute, hour, minute,
        hour, minute, hour, minute, hour, minute, hour, minute])
  print "Note: schedule only active in passive mode"

def exit():
  print "Exiting interface"
  send([173])
  sys.exit()
