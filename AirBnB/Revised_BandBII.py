##infile = open('BBcommands.txt', 'r')
##outfile = open('BBresults.txt', 'w')

import collections

Room = collections.namedtuple('Room', 'room_num available')
Cmd = collections.namedtuple('Cmd', 'action text')

BnB = []


def Bed_n_Breakfast():
    """Execute BBcommands.txt file"""
    BnB = []
    file_str = ''
    RL = []
    cmd_list = read_cmd_file()
    for cmd in cmd_list:
        action = cmd.action.lower()
        text = cmd.text
        if action == 'nb':
            new_room = NB_command(text[0])
            BnB.append(new_room)
        elif action == 'lb':
            available_rooms = room_num_str(LB_command(BnB))
            file_str = "{}\n{}".format(file_str, available_rooms)
        elif action == 'pl':
            line = PL_command(cmd)
            file_str = "{}\n{}".format(file_str, line)
        elif action == '**':
            skip_command()
        elif action == 'db':
            result = DB_command(text[0],BnB)
            if type(result) == list:
                BnB = result
            else:
                file_str = "{}\n{}".format(file_str, result)
    print(file_str)
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
    for room in RL:
        room_str = "{}\n{}".format(room_str, room.room_num)
    return room_str


def NB_command(room_num):
    """Add a new bedroom based on number to list of rooms"""
    new_room = Room(room_num, True)
    return new_room


def LB_command(RL:list):
    """Returns list of available rooms"""
    available_rooms = []
    for index in range(len(RL)):
        current = RL[index]
        if current.available:
            available_rooms.append(current)
    return available_rooms

def PL_command(cmd: Cmd):
    """Take text in Cmd, and return as str"""
    line = " ".join(cmd.text)
    return line

def skip_command():
    """skip command"""
    return ''

def DB_command(del_room, RL: list):
    """Return room based on number from list of rooms"""
    if check_room(del_room, RL):
        for room in RL:
            print(room)
            if room.room_num == del_room:
                RL.remove(room)
                break
        return RL
    else:
        file_str = "Sorry, can't delete room {}; it is not in service now".format(del_room)
        return file_str   

def check_room(room, RL):
    return any(Room.room_num == room for Room in RL)


Bed_n_Breakfast()

