import json
# - Make sure you can 
#     - put someone in an unoccpied room
#     - make a room available by setting the occupant name to ''
#     - check if a room number is valid
#     - check if a room is occupied or not
file_name = 'bffs.json'


hotel_rooms = {'101': '',
 '102': '', 
 '103': '', 
 '104': '', 
 '105': '', 
 '106': {
        'name': 'Iggy',
        'phone number': 000,
        'has prepaid': False}
}

# with open(file_name, 'w') as save_file:
#     json.dump(hotel_rooms, save_file)

main_menu = '''\n
1. check room vacancy
2. Make a room available
3. check if room number is valid
4. check if room is occupied
'''
# jotaro = {
# 'name': 'Jotaro', 
# 'phone number': 4232235840, 
# 'has prepaid': True
# }

# with open('bffs.json', 'r') as f2:
#      jotaro = json.load(f2)


# joseph = {
# 'name': 'joseph', 
# 'phone number': 22000, 
# 'has prepaid?': False
# }

# kakyoin = {
# 'name': 'Kakyoin', 
# 'phone number': 40203, 
# 'has prepaid': True
# }

# avdol = {
# 'name': 'avdol',
# 'phone number': 20012,
# 'has prepaid': True
# }

# Polnereffe = {
# 'name': 'Polnereffe',
# 'phone number': 42011,
# 'has prepaid': False
# }

# #print(hotel_rooms)
# print(jotaro)
# hotel_rooms['101'] = jotaro


def room_vacancy(room_check):
    #for room_check in hotel_rooms.keys():
    if hotel_rooms[room_check] == '':
        return(f'{room_check} is vacant')
    else:
        return hotel_rooms.get(room_check, 'That is not a valid room entry.')
 



while True:
#    hotel_rooms = {'101': 'Jotaro', '102': 'Joseph', '103': 'kakyoin', '104': 'Avdol', '105': 'Polnereffe', '106': 'Iggy'}
    print(main_menu)

    choose_room = input('Please enter what you would like to do: ')

    if choose_room == '1':
        check_hotel_room2 = input('Please enter room you would like to check if occupied: ')
        print(room_vacancy(check_hotel_room2))
#         new_room = input('Please enter new room number you would like to create: ')
#         new_occupant = input('Please enter new occupant of room: ')
#         hotel_rooms[new_room] = new_occupant
#         print(hotel_rooms)
#     elif choose_room == '2':
#         change_room = input('Please enter room you would like to empty: ')
#         hotel_rooms[change_room] = ''
#         print(hotel_rooms)
#     elif choose_room == '3':
#         check_hotel_room = input('Please choose room number you would like to check: ')
#         print(hotel_rooms.get(check_hotel_room, 'Room is empty'))
    # elif choose_room == '2':
    #     check_hotel_room2 = input('Please enter room you would like to check if occupied: ')
    #     print(hotel_rooms.get(check_hotel_room2, 'room is empty'))
        #if hotel_rooms[check_hotel_room2]
#     else:
#         break

#     # hotel_rooms['104'] = ''
#     # print(hotel_rooms)

#     # print(hotel_rooms.get('105', 'Nothing there'))
# print('Thank you for checking hotel rooms!')