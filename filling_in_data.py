def calcMissing(n, readings):
    known_data = []
    missing_indices = []
    
    for i in range(0, n):
        line = readings[i].strip()
        split_line = line.split('\t')
        date, value = split_line[0], split_line[-1]
        
        if value.startswith("Missing"):
            missing_indices.append(i - 1)
            known_data.append((date, None))
        else:
            known_data.append((date, float(value)))
    
    window_size = 3
    estimated_values = []
    
    for idx in missing_indices:
        sum_values = 0
        count = 0

        for i in range(max(0, idx - window_size), idx):
            if known_data[i][1] is not None:
                sum_values += known_data[i][1]
                count += 1
        
        for i in range(idx + 1, min(n, idx + window_size + 1)):
            if known_data[i][1] is not None:
                sum_values += known_data[i][1]
                count += 1

        if count == 0:
            estimated_value = 0.0
        else:
            estimated_value = sum_values / count
        
        estimated_values.append(estimated_value)
    
    for value in estimated_values:
        print(value)


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings_count, readings)