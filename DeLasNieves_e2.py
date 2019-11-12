line = input("Enter sustained winds: ")
x = int(line)

if x >= 220:
	print("Super Typhoon")
elif x >= 118:
	print("Typhoon")
elif x >= 89:
	print("Severe Tropical Storm")
elif x >= 62:
	print("Tropical Storm")
else:
	print ("Tropical Depression")



