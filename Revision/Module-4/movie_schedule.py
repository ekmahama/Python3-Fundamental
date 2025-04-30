current_moives = {
    'The Grinch': '11:00a',
    'Frosty the showman': '3:00pm',
    'Christmas vacation': '5:00pm'
}

print('We are currently showing:')
for key in current_moives:
    print(key)

movie = input('What movies do you like to see the showtime? ')

showtime = current_moives.get(movie)

if not showtime:
    print("Requested movies is not showing")
else:
    print(showtime)
