
def dictss(str):
    items = str.split('&')
    print(items)
    temp = []
    for item in items:
        temp.append(item.split('='))
    print(temp)    
    return dict(temp)

   


str = 'led=on&motor=off&switch=off'    
print(dictss(str))    
