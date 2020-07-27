def func(data, new, final):
    if(len(data) > 0):
        for i in range(len(data)):
            new.append(data[i])
            element = data.pop(i)
            func(data, new, final)
            data.insert(i, element)
            new.pop()
    else:
        final.append(new[:])

data = [1,2,3]
new = list()
final = list()
func(data, new, final)
print(final)