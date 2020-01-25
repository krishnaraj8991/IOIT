import random

def recognise(roi):
    names=['krs','unknown','unknown','unknown','unknown','unknown','unknown']
    leng=len(names)
    i=random.randint(0,leng-1)

    return names[i]