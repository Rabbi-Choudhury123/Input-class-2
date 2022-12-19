celsius = float(input("please enter the temperature in celsias: "))
farenheit = (celsius * 1.8) + 32

print(celsius,farenheit)

temp = farenheit


if (temp >= 104):
  print("Its hot")
elif (temp <= 50):
  print("Its cold")
else:
  print("The temperature is nice")
  
