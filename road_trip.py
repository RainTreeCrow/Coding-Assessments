distances = {}

line = input()
pairs = line.replace(" ", "").split(";")
for the_pair in pairs:
    pair = the_pair.split(",")
    if len(pair) == 2:
        city, distance = pair[0], int(pair[1])
        distances[city] = distance

sorted_distance = sorted(distances.items(), key=lambda item: item[1])
last_stop = sorted_distance[0][1]
result = str(last_stop)

for pair in sorted_distance[1:]:
    current_stop = pair[1]
    result += "," + str(current_stop - last_stop)
    last_stop = current_stop

print(result)