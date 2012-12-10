import random

# cookie = random.randstr('good','bab','evil','poor','smell')

cookie = random.randint(1, 5)

if cookie == 1:
  print("Your fortune for today is well")

elif cookie == 2:
  print("Your fortune for today is uncertain")

elif cookie == 3:
  print("Your fortune for today is deadbeat")

elif cookie == 4:
  print("Your fortune for today is healthy")

elif cookie == 5:
  print("Your fortune for today is superduper hapiness")

input("\n\nPress the enter key to exit.")

