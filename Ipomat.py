import argparse

def Get_Args():
    parser = argparse.ArgumentParser(
        usage= '''
    __     ______   ______     __    __     ______     ______  
    /\ \   /\  == \ /\  __ \   /\ "-./  \   /\  __ \   /\__  _\ 
    \ \ \  \ \  _-/ \ \ \/\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ 
    \ \_\  \ \_\    \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\ 
    \/_/   \/_/     \/_____/   \/_/  \/_/   \/_/\/_/     \/_/ 
                                                            
        '''         
    )
    parser.add_argument("ip",help="Your ip addr")
    args = parser.parse_args()
    return args
if __name__ == "__main__":  
    args = Get_Args()
    sum = 0
    ip = args.ip
    list = list(ip.split('.'))
    if len(list) != 4:
        raise ValueError("Value of IP is wrong") #check
    
    for i in range(len(list)):
        if int(list[i]) > 256:
            raise ValueError("The {}th digit of ip is wrong".format(int(i)+1))
            
        sum += int(list[i])* pow(256,int(3-i))
    print(
        '''
        [*]Hex = {}
        [*]Dec = {}
        [*]Bin = {}
        '''.format(hex(sum),sum,bin(sum))
    )
