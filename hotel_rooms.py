import json

file_name = 'bffs.json'

new_room = {}
hotel_rooms = {'101': {},
 '102': {}, 
 '103': {}, 
 '104': {}, 
 '105': {}, 
 '106': {}
}

# with open(file_name, 'w') as save_file:
#     json.dump(hotel_rooms, save_file)

main_menu = '''\n
1. check room vacancy
2. check in customer
3. check out customer
'''
# with open('bffs.json', 'r') as f2:
#      jotaro = json.load(f2)



def room_vacancy(room_check):
    if hotel_rooms[room_check] == {}:
        return(f'room {room_check} is vacant')
    else:
        return hotel_rooms.get(room_check, 'That is not a valid room entry.')
 

def new_occupant_name():
    name = input('Please enter new occupants name: ')
    phone_number = input('Please enter phone number: ')
    prepaid = input('Has the customer prepaid? True or False: ')
    if prepaid == 'True':
        prepaid = True
    elif prepaid == 'False':
        prepaid = False
    new_occupant = {
    'name': name,
    'phone number': phone_number,
    'has prepaid': prepaid
    }
    return new_occupant


def check_in(room_num):
    name = new_occupant_name()
    hotel_rooms[room_num] = name



def remove_occupant(checkout):
    if hotel_rooms[checkout]['has prepaid'] == True:
       hotel_rooms[checkout] = {}
       return hotel_rooms[checkout]
    elif hotel_rooms[checkout]['has prepaid'] == False:
       return print('you cant leave you havent paid yet')




while True:

    print(main_menu)

    choose_room = input('Please enter what you would like to do: ')

    if choose_room == '1':
        check_hotel_room2 = input('Please enter room you would like to check if occupied: ')
        print(room_vacancy(check_hotel_room2))

    elif choose_room == '2':
        print(f'These are the available rooms: {hotel_rooms}')
        new_room_fill = input('Please enter room you would like to fill')
        check_in(new_room_fill)

    elif choose_room == '3':
        check_hotel_room = input('Please choose room number you would like to check out: ')
        print(f'{hotel_rooms[check_hotel_room]} is checking out.')
        remove_occupant(check_hotel_room)
        
        
   
print('Thank you for checking hotel rooms!')