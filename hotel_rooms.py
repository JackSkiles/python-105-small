# - Make sure you can 
#     - put someone in an unoccpied room
#     - make a room available by setting the occupant name to ''
#     - check if a room number is valid
#     - check if a room is occupied or not


hotel_rooms = {'101': 'Jotaro', '102': 'Joseph', '103': 'kakyoin', '104': 'Avdol', '105': 'Polnereffe', '106': 'Iggy'}
print(hotel_rooms)

hotel_rooms['107'] = 'Hol Horse'
print(hotel_rooms)


hotel_rooms['104'] = ''
print(hotel_rooms)

print(hotel_rooms.get('105', 'Nothing there'))