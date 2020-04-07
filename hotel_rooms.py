# - Make sure you can 
#     - put someone in an unoccpied room
#     - make a room available by setting the occupant name to ''
#     - check if a room number is valid
#     - check if a room is occupied or not
hotel_rooms = {'101': 'Jotaro', '102': 'Joseph', '103': 'kakyoin', '104': 'Avdol', '105': 'Polnereffe', '106': 'Iggy'}
main_menu = '''\n
1. Put someone in an unoccupied room
2. Make a room available
3. check if room number is valid
4. check if room is occupied
'''
while True:
    hotel_rooms = {'101': 'Jotaro', '102': 'Joseph', '103': 'kakyoin', '104': 'Avdol', '105': 'Polnereffe', '106': 'Iggy'}
    print(main_menu)
    choose_room = input('Please enter what you would like to do: ')
    if choose_room == '1':
        new_room = input('Please enter new room number you would like to create: ')
        new_occupant = input('Please enter new occupant of room: ')
        hotel_rooms[new_room] = new_occupant
        print(hotel_rooms)
    elif choose_room == '2':
        hotel_rooms['107'] = 'Hol Horse'
        print(hotel_rooms)


    hotel_rooms['104'] = ''
    print(hotel_rooms)

    print(hotel_rooms.get('105', 'Nothing there'))