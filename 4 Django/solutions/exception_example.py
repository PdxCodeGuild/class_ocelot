



def myfunc(v):
    if v == 4:
        raise Exception('how dare you')
    return v+1



for v in range(5):
    try:
        print(myfunc(v))
    except:
        print('ERROR')




