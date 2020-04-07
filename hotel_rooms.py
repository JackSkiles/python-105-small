import json

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
jotaro = {
'name': 'Jotaro', 
'phone number': 4232235840, 
'has prepaid': True
}

# with open('bffs.json', 'r') as f2:
#      jotaro = json.load(f2)


joseph = {
'name': 'joseph', 
'phone number': 22000, 
'has prepaid?': False
}

kakyoin = {
'name': 'Kakyoin', 
'phone number': 40203, 
'has prepaid': True
}

avdol = {
'name': 'avdol',
'phone number': 20012,
'has prepaid': True
}

Polnereffe = {
'name': 'Polnereffe',
'phone number': 42011,
'has prepaid': False
}

# #print(hotel_rooms)
# print(jotaro)
# hotel_rooms['101'] = jotaro
def name_checker(occupant_name):
     if occupant_name == 'jotaro':
        return jotaro
     elif occupant_name == 'kakyoin':
         return kakyoin
     elif occupant_name == 'avdol':
         return avdol
     elif occupant_name == 'joseph':
         return joseph
     elif occupant_name == 'polnereffe':
         return Polnereffe
     else:
         pass


def room_vacancy(room_check):
    if hotel_rooms[room_check] == '':
        return(f'{room_check} is vacant')
    else:
        return hotel_rooms.get(room_check, 'That is not a valid room entry.')
 
def new_occupant_name(new_occupant, room_number):
    hotel_rooms[room_number] = new_occupant

def remove_occupant(checkout):
    hotel_rooms[checkout] = ''



while True:

    print(main_menu)

    choose_room = input('Please enter what you would like to do: ')

    if choose_room == '1':
        check_hotel_room2 = input('Please enter room you would like to check if occupied: ')
        print(room_vacancy(check_hotel_room2))

    elif choose_room == '2':
        print(f'These are the available rooms: {hotel_rooms}')

        enter_room_number = input('Please input room number you would like to fill: ')
        enter_new_occupant = input('Who would you like to make the new occupant?')
        enter_new_occupant = name_checker(enter_new_occupant)
        print(new_occupant_name(enter_new_occupant, enter_room_number))
        print(f'new room list: {hotel_rooms}')

    elif choose_room == '3':
        check_hotel_room = input('Please choose room number you would like to check out: ')
        print(f'{hotel_rooms[check_hotel_room]} is checking out.')
        remove_occupant(check_hotel_room)
   
print('Thank you for checking hotel rooms!')