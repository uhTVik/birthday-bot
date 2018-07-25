import re


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False


def invalad_nick(nick):
    return re.match('^[a-z0-9\_]$', nick) is None


def invalid_name(name):
    return re.match('^[a-zа-яA-ZА-Я]$', name) is None

def invalid_date(date):
    date = date.split(".")
    if len(date)!=3:
        return True
    if (len(date[0])!=4 or len(date[1])>2 or len(date[2])>2) or (not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit()):
        return True
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    if month > 12 or month == 0:
        return True
    if day > 31 or day == 0:
        return True
    if ((month in set([2, 4, 6, 9, 11])) and (day > 30)):
        return True
    if month == 2:
        if ((not is_leap_year(year)) and (day > 28)):
            return True
        if ((is_leap_year(year)) and (day > 29)):
            return True
    return False



def invalid(args):
    if len(args) != 4:
        return True
    if invalid_nick(args[0]):
       return True
    if invalid_name(args[1]):
       return True
    if invalid_name(args[2]):
       return True
    if invalid_date(args[3]):
        return True
    return False