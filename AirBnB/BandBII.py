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
    Cmd_list = read_cmd_file()
    for index in range(len(Cmd_list)):
        current_Cmd = Cmd_list[index]
        print(current_Cmd)
        Cmd_action = current_Cmd.action.lower()
        if Cmd_action == 'nb':
            new_room = NB_command(current_Cmd.text[0])
            BnB.append(new_room)
        elif Cmd_action == 'lb':
            available_rooms = LB_command(BnB)
            available_rooms_str = room_num_str(available_rooms)
            file_str = "{}\n{}".format(file_str, available_rooms_str)
        elif Cmd_action == 'pl':
            line = PL_command(current_Cmd)
            file_str = "{}\n{}".format(file_str, line)
        elif Cmd_action == '**':
            skip_command()
        elif Cmd_action == 'db':
            if any(Room.room_num== current_Cmd.text[0] for Room in BnB):
                BnB = DB_command(current_Cmd.text[0], BnB)
            else:
                file_str = "{}\nSorry, can't delete room {}; it is not in service now".format(
                        file_str, current_Cmd.text[0])
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
    for index in range(len(RL)):
        current = RL[index]
        room_str = "{}\n{}".format(room_str, current.room_num)
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

##test = [Room('405', True), Room('302', True), Room('505', True)]
##
##test1 = DB_command('302', test)
##
##print(test1)

Bed_n_Breakfast()

