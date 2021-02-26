

import collections
import datetime
##from calendar import date
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
    confirm = 0
    cmd_list = read_cmd_file()
    for cmd in cmd_list:
        action = cmd.action.lower()
        text = cmd.text
        if action == 'nb':
            room_num = text[0]
            if not check_room(room_num, BnB):
                new_room = new_bedroom(room_num)
                BnB.append(new_room)
            else:
                file_str = "{}\n{}".format(file_str, new_bedroom_error_str(room_num))
        elif action == 'lb':
            available_rooms = room_num_str(list_bedrooms(BnB))
            file_str = "{}\n{}".format(file_str, available_rooms)
        elif action == 'pl':
            line = print_line(cmd)
            file_str = "{}\n{}".format(file_str, line)
        elif action == '**':
            skip_command()
        elif action == 'db':
            room_num = int(text[0])
            if check_room(room_num, BnB):
                BnB = delete_room(room_num, BnB)
                file_str = "{}\n{}".format(file_str, remove_reservation_str(room_num, res_list)) 
                res_list = remove_reservation(room_num, res_list)
            else:
                del_str = del_fail_str(room_num)
                file_str = "{}{}".format(file_str, del_str) 
        elif action == 'rr':
            room_num = text[0]
            arv_date = convert_date(text[1])
            dep_date = convert_date(text[2])
            if check_logic(BnB, text, res_list):
                confirm = confirm + 1
                print(confirm)
                reserve = new_reservation(text, res_list, BnB, confirm)
                file_str = "{}\n{}".format(file_str, res_str(reserve))
                res_list.append(reserve)
            elif not check_room(room_num, BnB):
                file_str = "{}\n{}".format(file_str, not_res_str(room_num))
            elif res_date_check(arv_date, dep_date):
                file_str = "{}\n{}".format(file_str, res_date_error_str(room_num, arv_date, dep_date))
            elif  same_date_check(arv_date, dep_date):
                file_str = "{}\n{}".format(file_str, same_date_error_str(room_num, arv_date, dep_date))
            elif not res_room_unavailable_check(room_num, arv_date, dep_date, res_list):
                file_str = "{}\n{}".format(file_str, res_room_unavailable_str(room_num, arv_date, dep_date, res_list))
        elif action == 'lr':
            file_str = "{}\n{}".format(file_str, list_reservations(res_list))
        elif action == 'dr':
            confirmation_number = int(text[0])
            if check_reservation(confirmation_number, res_list):
                res_list = DR_command(confirmation_number, res_list)
            else:
                file_str = "{}\n{}".format(file_str, del_res_str(confirmation_number))
##    print(BnB)
##    print(res_list)
    print(file_str)
    outfile = open('BBresults.txt', 'w')
    outfile.write(file_str)
    outfile.close


## Stage I ##


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


def new_bedroom(room_num):
    """Add a new bedroom based on number to list of rooms"""
    new_room = Room(room_num, True, "")
    return new_room


def list_bedrooms(room_list:list):
    """Returns list of available rooms"""
    available_rooms = []
    for index in range(len(room_list)):
        current = room_list[index]
        if current.available:
            available_rooms.append(current)
    return available_rooms

def print_line(cmd: Cmd):
    """Take text in Cmd, and return as str"""
    line = " ".join(cmd.text)
    return line

def skip_command():
    """skip command"""
    return ''


## Stage II ##


### Delete Room Functions ###


def delete_room(del_room, room_list: list):
    """Return room based on number from list of rooms"""
    for room in room_list:
        if int(room.room_num) == int(del_room):
            room_list.remove(room)
    return room_list


def del_fail_str(del_room):
    """Return delete room failure str"""
    file_str = "Sorry, can't delete room {}; it is not in service now".format(del_room)
    return file_str


def check_room(room, room_list):
    """Check if room exist in list of rooms"""
    return any(int(Room.room_num) == int(room) for Room in room_list)


## Stage III ###


###Reservation Functions###


def new_reservation(text: list, res_list, BnB, confirm):
    """Return a Reservation or error msg based on Cmd.text"""
    request_room = text[0]
    arrival = text[1]
    departure = text[2]
    name = " ".join(text[3:])
    reservation = create_reservation(confirm, request_room, arrival, departure, name, res_list)
    return reservation


def create_reservation(confirm, rev_room, arrival: 'mm/dd/yyyy', departure: 'mm/dd/yyyy',
                       name: 'last, first', res_list):
    """Return a Reservation"""
    arrival_date = convert_date(arrival)
    departure_date = convert_date(departure)
    reservation = Reservation(confirm, rev_room, arrival_date, departure_date, name)
    return reservation


def res_str(r: Reservation):
    """Return reservation string from Reservation"""
    res_str = "Reserving room {} for {} -- Confirmation #{}\n\t(arriving {}, departing {})".format(
        r.room_num, r.name, r.confirmation, r.arv_date, r.dep_date)
    return res_str


def not_res_str(room_num):
    """Return error string with room number"""
    not_res_str = "Sorry; can't reserve room {}; room not in service\n".format(room_num)
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


def list_reservations(rl: "List of Reservations"):
    header = "Number of reservations: {}\nNo. Rm. Arrive      Depart     Guest\n------------------------------------------------".format(len(rl))
    body = ''
    for r in rl:
        arv = r.arv_date.strftime('%m/%d/%Y')
        dep = r.dep_date.strftime('%m/%d/%Y')
        reserve_str = "\n{:3} {:3} {} {}  {}".format(r.confirmation, r.room_num, arv, dep, r.name)
        body = body + reserve_str 
    return (header + body)


###DR Delete Reservation###


def check_reservation(confirmation_num: int, rl: "List of Reservations"):
    """Return boolean if confirmation number is in list of reservation"""
    return any(int(reservation.confirmation) == int(confirmation_num) for reservation in rl)


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


## Stage IV ####

### Reservation Logic Check ###


def check_logic(BnB, text, res_list):
    """Return boolean for if all of the following logic functions are true"""
    if len(res_list) == 0:
        return len(res_list) == 0
    else:
        res_room_number = text[0]
        arv_date = convert_date(text[1])
        dep_date = convert_date(text[2])
        logic = [res_room_unavailable_check(res_room_number, arv_date, dep_date, res_list),
                 res_date_check(arv_date, dep_date),
                 check_room(res_room_number, BnB),
                 same_date_check(arv_date, dep_date)]
        return logic == [True, False, True, False]
    

def res_date_check(arv_date, dep_date):
    """Return boolean if departure date is before arrival date"""
    return dep_date < arv_date


def res_date_error_str(room_num, arv_date, dep_date):
    """Return error string for date logic check"""
    date_check_str = "Sorry, can't reserve room {} ({} to {});\n\tcan't leave before you arrive.".format(
        room_num, arv_date, dep_date)
    return date_check_str


def same_date_check(arv_date, dep_date):
    """Return boolean if arv = dep"""
    return arv_date == dep_date


def same_date_error_str(room_num, arv_date, dep_date):
    """Return error string for same date logic check"""
    same_date_str = "Sorry, can't reserve room {} ({} to {});\n\tcan't arrive and leave on the same day.".format(
        room_num, arv_date, dep_date)
    return same_date_str
    

def res_room_unavailable_check(room_number, arv_date, dep_date, res_list):
    """Return boolean if room is already reserved"""
    requested_room_reservations = []
    for room in res_list:
        if int(room.room_num) == int(room_number):
            requested_room_reservations.append(room)
    requested_room_reservations.sort(key = arv_date_sort_key)
    return check_date_logic(arv_date, dep_date, requested_room_reservations)
    

def arv_date_sort_key(reservation):
    """Return arival date of reservation"""
    return reservation.arv_date


def check_date_logic(arv_date, dep_date, requested_room_resrvation):
    """Return boolean if dates of requested reservations is avaialable"""
    if len(requested_room_resrvation) == 0:
        return True
    else:
##        print(len(requested_room_resrvation))
        logic_arv_after_last_dep = requested_room_resrvation[-1].dep_date <= arv_date
##        print(len(requested_room_resrvation))
        logic_dept_b4_1st_arv = requested_room_resrvation[0].arv_date >= dep_date
        logic_between_dates = check_between_reservations(arv_date, dep_date, requested_room_resrvation)
        logic = [logic_arv_after_last_dep, logic_dept_b4_1st_arv, logic_between_dates]
        return any(logic)
        

def check_between_reservations(arv_date, dep_date, requested_room_resrvation):
    validate = [False, False]
    for i in range(len(requested_room_resrvation)):
        if i + 1 == len(requested_room_resrvation):
            break
        else:
            current_res = requested_room_resrvation[i]
            next_res = requested_room_resrvation[i+1]
            logic_arv_b4_dep = arv_date < current_res.dep_date
            logic_dep_b4_arv = dep_date > next_res.arv_date
            logic = [logic_arv_b4_dep, logic_dep_b4_arv]
            if logic == validate:
                return [logic == validate]
                break

###Ask viet for a client way to index the conflicting reservation###

def res_room_unavailable_str(room_number, arv_date, dep_date, res_list):
    unavailable_str = "Sorry, can't reserve room {} ({} to {});\n\tit's already booked (Conf. #{})".format(
        room_number, arv_date, dep_date, 'blank')
    return unavailable_str


def new_bedroom_error_str(room_num):
    error_str = "Sorry, can't add room {} again; it's already on the list.".format(room_num)
    return error_str


def remove_reservation(room_num, res_list):
    mod_res_list = []
    for room in res_list:
        if int(room_num) != int(room.room_num):
            mod_res_list.append(room)
    return mod_res_list

def remove_reservation_str(room_num, res_list):
    file_str = ''
    remove_reservation_str = "Deleting room {} forces cancellation of this reservation:\n\t{} arriving {} and departing  {} (Conf. #{})\n"
    for room in res_list:
        if int(room_num) == int(room.room_num):
            remove_res_str = remove_reservation_str.format(room.room_num, room.name, room.arv_date,
                                                           room.dep_date, room.confirmation)
            file_str = "{}{}".format(file_str, remove_res_str)
    return file_str[:-1]


def print_lines(line):
    for i in line:
        print(i)
    print('\n')
    
### Test ###
    
test1 = [Reservation(confirmation=1, room_num='301', arv_date=1, dep_date=2, name='Conrad Hilton'),
         Reservation(confirmation=2, room_num='301', arv_date=3, dep_date=4, name='Thang Nguyen'),
         Reservation(confirmation=3, room_num='302', arv_date=3, dep_date=4, name='Thang Nguyen')]


## Main Program ## 
Bed_n_Breakfast()

