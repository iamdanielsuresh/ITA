battery = 45

for i in range(0,battery):
    battery -= 1
    print("Battery : {}%".format(battery))
    
print( "Battery died, phone switching off")