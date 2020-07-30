vector = [(0, 0), (1, 4), (0,0)]
steps = 0
for x in range(len(vector)-1):
    delta = abs(vector[x][0] - vector[x+1][0])
    delta2 = abs(vector[x][1] - vector[x+1][1])
    if(delta < delta2): delta = delta2
    steps += delta

print(steps)
