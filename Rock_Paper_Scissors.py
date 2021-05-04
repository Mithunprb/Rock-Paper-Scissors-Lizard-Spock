import random
e, pos, lost, win, tie = input("Choose rock paper siccors or r,p,s:"), ["r", "p", "s", "rock", "paper", "siccors"],lambda: print("you lost")if e.lower() in pos else print("you lost"), lambda: print("you win")if e.lower(
  ) in pos else print("you win"), lambda: print("TIE!")if e.lower() in pos else print("TIE!")
func = random.choice([lost, win, tie])
func()