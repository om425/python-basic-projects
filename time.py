import time 
t= (time.strftime("%H:%M:%S"))
h= int(time.strftime("%H"))
print(t)




if (h>=0 and h<12):
  print("Good morning!")
elif(h>=12 and h<17):
  print("Good afternoon!")
elif(h>=17 and h<21):
  print("Good evening!")
elif(h>=21 and h<24):
  print("Good Night!")
