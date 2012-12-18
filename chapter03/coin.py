import random
Num = int(input("enter number of coin flips:"))
coin = 0
h = 0
t = 0
while coin < Num:
   coin = coin + 1
   rand = random.randint(0,2)
   if rand == 1:
     h = h + 1
   else:
    t = t + 1
print (h, "heads",t, "tails")
