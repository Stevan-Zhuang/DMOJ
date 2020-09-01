speed_limit = int(input())
speed = int(input())
speed_above = speed - speed_limit

if speed_above > 0:
  if speed_above >= 31: price = "500"
  elif speed_above >= 21: price = "270"
  elif speed_above >= 1: price = "100"
  print("You are speeding and your fine is $" + price + ".")
else:
  print("Congratulations, you are within the speed limit!")
