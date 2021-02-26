##infile = open('BBcommands.txt', 'r')
##outfile = open('BBresults.txt', 'w')

import collections
from datetime import datetime
from time import strftime

Cmd = collections.namedtuple('Cmd', 'action text')
Room = collections.namedtuple('Room', 'room_num available reservation')
Reservation = collections.namedtuple('Reservation', 'confirmation room_num arv_date dep_date name')

def Bed_n_Breakfast():
    """Execute BBcommands.txt file"""
    BnB = []
    file_str = ''
    res_list = []
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
            result = DB_command(text[0], BnB)                #Structure similar to RR command would have been better here
            if type(result) == list:
                BnB = result
            else:
                file_str = "{}\n{}".format(file_str, result)
        elif action == 'rr':
            if check_room(text[0], BnB):
                reserve = new_reservation(text, res_list, BnB)
                file_str = "{}\n{}".format(file_str, res_str(reserve))
                res_list.append(reserve)
            elif not check_room(text[0], BnB):
                file_str = "{}\n{}".format(file_str, not_res_str(text[0]))
        elif action == 'lr':
            file_str = "{}\n{}".format(file_str, LR_command(res_list))
        elif action == 'dr':
            confirmation_number = int(text[0])
            if check_reservation(confirmation_number, res_list):
                res_list = DR_command(confirmation_number, res_list)
            elif not check_reservation(confirmation_number, res_list):
                file_str = "{}\n{}".format(file_str, del_res_str(text[0]))
    print(res_list)
    print(file_str)
    outfile = open('BBresults.txt', 'w')
    outfile.write(file_str)
    outfile.close


#Stage I


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


def room_num_str(room_list: list):
    """Return list of Room, as string of room numbers"""
    room_str = 'Number of bedrooms in service: {} \n------------------------------------'.format(
        len(room_list))
    for room in room_list:
        room_str = "{}\n{}".format(room_str, room.room_num)
    return room_str


def NB_command(room_num):
    """Add a new bedroom based on number to list of rooms"""
    new_room = Room(room_num, True, "")
    return new_room


def LB_command(room_list:list):
    """Returns list of available rooms"""
    available_rooms = []
    for index in range(len(room_list)):
        current = room_list[index]
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


##Stage II


def DB_command(del_room, room_list: list):
    """Return room based on number from list of rooms"""
    if check_room(del_room, room_list):
        for room in room_list:
            print(room)
            if room.room_num == del_room:
                room_list.remove(room)
                break
        return room_list
    else:
        file_str = "Sorry, can't delete room {}; it is not in service now".format(del_room)
        return file_str   

def check_room(room, room_list):
    """Check if room exist in list of rooms"""
    return any(Room.room_num == room for Room in room_list)


##Stage III

###Reservation Functions###

def new_reservation(text: list, res_list, BnB):
    """Return a Reservation or error msg based on Cmd.text"""
    request_room = text[0]
    arrival = text[1]
    departure = text[2]
    name = text[4] + ', ' + text[3]
    reservation = create_reservation(request_room, arrival, departure, name, res_list)
    return reservation


def create_reservation(rev_room, arrival: 'mm/dd/yyyy', departure: 'mm/dd/yyyy',
                       name: 'last, first', res_list):
    """Return a Reservation"""
    arrival_date = convert_date(arrival)
    departure_date = convert_date(departure)
    confirm = confirm_number(res_list)
    reservation = Reservation(confirm, rev_room, arrival_date, departure_date, name)
    return reservation


def res_str(r: Reservation):
    """Return reservation string from Reservation"""
    res_str = "Reserving room {} for {} -- Confirmation #{}\n\t(arriving {}, departing {})".format(
        r.room_num, r.name, r.confirmation, r.arv_date, r.dep_date)
    return res_str


def not_res_str(room_num):
    """Return error string with room number"""
    not_res_str = "Sorry; can't reserve room {}; room not in service".format(room_num)
    return not_res_str


def confirm_number(res_list):
    """Return 0 or the last confirmation number in list of reservation"""
    if len(res_list) == 0:
        confirm = 1
    else:
        confirm = res_list[-1].confirmation + 1
    return confirm


def convert_date(date: 'mm/dd/yyyy'):
    """Return date object from str"""
    date_obj = datetime.strptime(date, '%m/%d/%Y').date()
    return date_obj



###LR List Reservations###


def LR_command(rl: "List of Reservations"):
    header = "Number of reservations: {}\nNo. Rm. Arrive      Depart     Guest\n------------------------------------------------".format(len(rl))
    body = ''
    for r in rl:
        arv = r.arv_date.strftime('%m/%d/%Y')
        dep = r.dep_date.strftime('%m/%d/%Y')
        reserve_str = "\n{:3} {:3} {} {}  {}".format(r.confirmation, r.room_num, arv, dep, r.name)
        body = body + reserve_str 
    return (header + body)


###DR Delete Reservation##

def check_reservation(confirmation_num: int, rl: "List of Reservations"):
    """Return boolean if confirmation number is in list of reservation"""
##    for reservation in rl:
##        if reservation.confirmation == confirmation_num:
##            return True
    return any(reservation.confirmation == confirmation_num for reservation in rl)

def DR_command(confirmation_num: int, rl:"List of Reservations"):
    """Remove reservation with matching confirmation number from list of Reservations, returns list"""
    for reservation in rl:
        if reservation.confirmation == confirmation_num:
            rl.remove(reservation)
    return rl

def del_res_str(confirmation_num):
    """Return error msg str for deleting reservation not listed"""
    del_str = "Sorry, can't cancel reservation; no confirmation number {}".format(confirmation_num)
    return del_str
    
test1 = [Reservation(confirmation=1, room_num='303', arv_date=1, dep_date=2, name='Hilton, Conrad'),
         Reservation(confirmation=2, room_num='303', arv_date=3, dep_date=4, name='Ritz, Cesar'),
         Reservation(confirmation=3, room_num='301', arv_date=5, dep_date=6, name='Helmsley, Leona')]
assert check_reservation(1, test1)

test2 = DR_command(1, test1)
assert len(test2) == 2
##print(test2)

Bed_n_Breakfast()

