##infile = open('BBcommands.txt', 'r')
##outfile = open('BBresults.txt', 'w')

import collections
from datetime import datetime

Room = collections.namedtuple('Room', 'room_num available reservations')
Reservation = collections.namedtuple('Reservation', 'confirmation arv_date dep_date name')
Cmd = collections.namedtuple('Cmd', 'action text')




def Bed_n_Breakfast():
    """Execute BBcommands.txt file"""
    BnB = []
    RL = []
    file_str = ''
    cmd_list = read_cmd_file()
    for index in range(len(cmd_list)):
        current_cmd = cmd_list[index]
##        print(current_Cmd)
        cmd_action = current_cmd.action.lower()
        cmd_text = current_cmd.text
        if cmd_action == 'nb':
            new_room = NB_command(cmd_text[0])
            BnB.append(new_room)
        elif cmd_action == 'lb':
            available_rooms = room_num_str(LB_command(BnB))
##            available_rooms_str = room_num_str(available_rooms)
##            file_str.join(file_str, available_rooms_str)
            file_str.join(available_rooms)
        elif cmd_action == 'pl':
            line = PL_command(current_cmd)
            file_str = "{}\n{}".format(file_str, line)
        elif cmd_action == '**':
            skip_command()
        elif cmd_action == 'db':
            if any(Room.room_num == current_cmd.text[0] for Room in BnB):
                BnB = DB_command(current_cmd.text[0], BnB)
            else:
                file_str = "{}\nSorry, can't delete room {}; it is not in service now".format(
                        file_str, current_cmd.text[0])
        elif Cmd_action == 'rr':
            if any(Room.room_num == current_cmd.text[0] for Room in BnB):
                for i in range(len(BnB)):
                    current_room = BnB[i]
                    if current_cmd.text[0] == current_room.room_num:
                        current_room = Room(current_room.room_num, True,
                                            RR_command(current_room.room_num, current_cmd.text[1],
                                                       current_cmd.text[2],
                                                       str(current_cmd.text[3] + current_cmd.text[4])))
                BnB[i] = current_room
            else:
                file_str = "{}\nSorry, can't reserve room {}; it is not in service now".format(
                        file_str, current_Cmd.text[0])
    print(file_str)
    print(BnB)
    outfile = open('BBresults.txt', 'w')
    outfile.write(file_str)
    outfile.close


def read_cmd_file():
    """Read file, and return list of Commands"""
    infile = open('BBcommands.txt', 'r')
    Cmd_list = []
    for line in infile:
        current = line.split()
        cmd = Cmd(current[0], current[1:])
        Cmd_list.append(cmd)
    infile.close
    return Cmd_list
        



def room_num_str(RL: list):
    """Return list of Room, as string of room numbers"""
    room_str = 'Number of bedrooms in service: {} \n------------------------------------'.format(
        len(RL))
    for index in range(len(RL)):
        current = RL[index]
        room_str = "{}\n{}".format(room_str, current.room_num)
    return room_str


def NB_command(room_num):
    """Add a new bedroom based on number to list of rooms"""
    new_room = Room(room_num, True, [])
    return new_room


def LB_command(RL:list):
    """Returns list of available rooms"""
    available_rooms = []
    for index in range(len(RL)):
        current = RL[index]
        if current.available:
            available_rooms.append(current)
    return available_rooms

def PL_command(Cmd: Cmd):
    """Take text in Cmd, and return as str"""
    line = ''
    current = Cmd.text
    for text in current:
        line = line + text + ' '
    return line

def skip_command():
    """skip command"""
    return ''

def DB_command(del_room, RL: list):
    """Return room based on number from list of rooms"""
    print(len(RL))
    for i in range(len(RL)):
        current_room = RL[i]
        if current_room.room_num == del_room:
            RL.remove(current_room)
            break
    return RL    

def RR_command(rev_room, arrival: 'mm/dd/yyyy', departure: 'mm/dd/yyyy', name: 'last, first'):
    arrival_date = convert_date(arrival)
    departure_date = convert_date(departure)
    if len(RL) == 0:
        confirm = 0
    else:
        confirm = RL[-1].confirmation + 1
    new_reservation = Reservation(confirm, arrival_date, departure_date, name)
    RL.append(new_reservation)
    return new_reservation


def convert_date(date: 'mm/dd/yyyy'):
    """Return date object from str"""
    date_obj = datetime.strptime(date, '%m/%d/%Y').date()
    return date_obj


##reserve1 = RR_command('405', '01/20/2020', '01/25/2020', 'Nguyen, Thang')
##reserve2 = RR_command('406', '01/20/2020', '01/25/2020', 'Nguyen, Thang')
##reserve3 = RR_command('407', '01/20/2020', '01/25/2020', 'Nguyen, Thang')
##print(RL)

Bed_n_Breakfast()

