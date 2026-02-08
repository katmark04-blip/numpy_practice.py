import time
import random

#for x in range(0,4):
   # print (x)
  #  time.sleep(2)
  #  print (".......happy new year......")
inputtime =int(input("enter time in seconds..."))
for num in range(inputtime,0,-1):
  seconds = num %60
  minutes = int(num /60) % 60
  hour = int(num/3600)
  print(f"{hour:02} : {minutes:02} : {seconds:02}")
  time.sleep(1)    