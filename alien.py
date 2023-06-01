alien_0 = {"color" : "green" , "points" : 5}
print(alien_0["color"])
print(alien_0["points"])

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0["color"] = "yellow"
print(alien_0)

alien_1 = {'x_position' : 0, 'y_position' : 25, 'speed': 'medium'}
print(f"old position: ({alien_1['x_position']},{alien_1['y_position']})")

alien_1['speed'] = 'fast'

if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_1['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: ({alien_1['x_position']},{alien_1['y_position']})")

del alien_0['color']
print(alien_0)
#print(alien_0['color'])

color_value  = alien_0.get('color', '\nNo color is assigned')
print(color_value)

#Nesting

alien_3 = {'color' : 'green', 'points' : 5}
alien_4 = {'color' : 'yellow', 'points' : 10}
alien_5 = {'color' : 'red', 'points' : 15}

aliens = []

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] == 'yellow'
		alien['speed'] == 'medium'
		alien['points'] == 10
	print(alien)
	elif alien['color'] == 'yellow':
		alien['color'] == 'red'
		alien['speed'] == 'fast'
		alien['points'] == 15

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

