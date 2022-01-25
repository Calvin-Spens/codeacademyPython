weight = float(input('How much does your package weigh? '))
ground = 0
ground_premium = 125
drone = 0
cost = 0

if weight <= 2:
    ground = weight * 1.5 + 20
    drone = weight * 4.5
elif weight > 2 and weight <= 6:
    ground = weight * 3 + 20
    drone = weight * 9
elif weight > 6 and weight <= 10:
    ground = weight * 4 + 20
    drone = weight * 12
else:
    ground = weight * 4.75 + 20
    drone = weight * 14.25

ground = float("{:.2f}".format(ground))
drone = float("{:.2f}".format(drone))

print('Your prices are:\nGround: $' + str(ground))
print('Ground Premium: $' + str(ground_premium))
print('Drone: $' + str(drone))
if ground < 125 and ground < drone:
    print('Your best option is to ship using Ground at $' + str(ground))
elif drone < 125 and drone <= ground:
    print('Your best option is to ship using Drone at $' + str(drone))
else:
    print('Your best option is to ship using Ground Premium at $' + str(ground_premium))
