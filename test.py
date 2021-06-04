def is_even():
    newlist=[]
    for i in range(1,51):
        if i % 2 == 0:
            newlist.append(i)
    return newlist
print(is_even())