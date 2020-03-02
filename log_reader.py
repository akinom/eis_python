import socket

def open_file():
    # fname = input("enter log file name> ")
    fname = 'resources/apache_logs'
    fd = open(fname, "r")
    return fd

def mainv7():
    #print actions and ips
    fd = open_file()
    for line in fd.readlines():
        ip, action = digest_line(line)
        if (action != "GET"):
            print(ip, '\t', action)

def digest_line(log_line):
    idx_blank = log_line.find(' ')
    ip = log_line[0:idx_blank]

    idx_action = log_line.find('"')
    idx_action_end = log_line.find(' ', idx_action)
    action = log_line[idx_action + 1:idx_action_end]

    return ip, action

def mainv7():
    #print actions and ips
    fd = open_file()
    for line in fd.readlines():
        ip, action = digest_line(line)
        if (action != "GET"):
            print(ip, '\t', action)
            print(line)
            input('enter for next')

def mainv6():
    #print actions and ips
    fd = open_file()
    for line in fd.readlines():
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]

        idx_action = line.find('"')
        idx_action_end = line.find(' ', idx_action )
        action = line[idx_action+1:idx_action_end]

        if (action != "GET"):
            print(line)
            print(ip, '\t', action)
            input('enter for next')


def mainv5():
    #print actions and ips
    fd = open_file()
    for line in fd.readlines():
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]

        idx_action = line.find('"')
        idx_action_end = line.find(' ', idx_action )
        action = line[idx_action+1:idx_action_end]

        print(line)
        print(ip, '\t', action)
        input('enter for next')

def mainv4():
    #print actions
    fd = open_file()
    for line in fd.readlines():
        idx_action = line.find('"')
        idx_action_end = line.find(' ', idx_action )
        # while developing eye ball
        print(line)
        print(line[idx_action+1:idx_action_end])
        input('enter for next')


def main():
    fname = 'resources/apache_logs'
    fd = open(fname, "r")
    for line in fd.readlines():
        # ip == text up to first blank
        ip = line[0: line.find(' ')]
        dname, _, _ = socket.gethostbyaddr(ip)
        print(dname, ' | ' , line, end='')

def mainv24():
    fname = 'resources/apache_logs'
    fd = open(fname, "r")
    for line in fd.readlines():
        # index of first blank
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]
        dname, _, _ = socket.gethostbyaddr(ip)
        print(dname, ' | ' , line, end='')

def mainv23():
    fname = 'resources/apache_logs'
    fd = open(fname, "r")
    for line in fd.readlines():
        # index of first blank
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]
        dname, _, _ = socket.gethostbyaddr(ip)
        print(dname, ip , ' ' , line)
        input("eyeball")

v = 23

if (v > 3):
    main()


if (v == 3):
    # help(socket.gethostbyaddr)
    while (True):
        ip = input('enter a valid ip addr> ')

        dname, _, _ = socket.gethostbyaddr(ip)
        print(ip, ' -> ' , dname)

if (v ==2):
    #just print ips
    # fname = input("enter log file name> ")
    fname = 'resources/apache_logs'
    fd = open(fname, "r")
    for line in fd.readlines():
        # index of first blank
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]
        print(ip)

if (v ==1):
    #print ips  with printing and stops to visually review what the code actually does
    fname = input("enter log file name> ")
    fd = open(fname, "r")
    for line in fd.readlines():
        # index of first blank
        idx_blank = line.find(' ')
        ip = line[0:idx_blank]
        # print while developing
        print(line, end='')
        print('IP ', ip)
        input("go on?")

if (v == 0):
    fname = input("enter log file name> ")
    fd = open(fname, "r")
    for line in fd.readlines():
        print(line, end='')
