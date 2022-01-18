import argparse

def Get_Args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--ip",help="Your ip addr")
    args = parser.parse_args()
    return args
def setup():
    print(
        '''
    __     ______   ______     __    __     ______     ______  
    /\ \   /\  == \ /\  __ \   /\ "-./  \   /\  __ \   /\__  _\ 
    \ \ \  \ \  _-/ \ \ \/\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ 
    \ \_\  \ \_\    \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\ 
    \/_/   \/_/     \/_____/   \/_/  \/_/   \/_/\/_/     \/_/ 
                                                            
    usage: main.py [-h] [-u URL] [-a IP]

    optional arguments:
        -h, --help         show this help message and exit
        -a IP, --ip IP     Your ip addr
        '''            
    )
    global args
    if args.ip == None:
        raise ValueError("You must input a Value of IP ")

if __name__ == "__main__":  
    args = Get_Args()
    sum = 0
    ip = args.ip
    list = list(ip.split('.'))
    setup()
    for i in range(len(list)):
        sum += int(list[i])* pow(256,int(3-i))
    print(
        '''
        [*]Hex = {}
        [*]Dec = {}
        [*]Bin = {}
        '''.format(hex(sum),sum,bin(sum))
    )
