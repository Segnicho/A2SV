import textwrap

def wrap(string, max_width):
    i = 0
    while i < (len(string)//max_width):
        print(string[max_width*i: max_width*(i+1)])
        i+=1
    return (string[max_width*i:])
    # return
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
