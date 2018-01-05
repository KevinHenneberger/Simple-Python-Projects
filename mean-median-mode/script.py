def mean(data):
    
    sum = 0

    for i in data:
        sum += i
    
    return sum / len(data)

def median(data):
    
    data.sort()
   
    middleIndex = len(data) // 2
    
    if (len(data) % 2 == 1):
        return data[middleIndex]
    else:
        return (data[middleIndex - 1] + data[middleIndex]) / 2

def mode(data):
    
    mode = 0
    maxFrequency = 0

    for i in data:
        currentFrequency = 0
    
        for j in data:
            if (i == j):
                currentFrequency += 1
                        
            if (currentFrequency > maxFrequency):
                maxFrequency = currentFrequency
                mode = j
    
    return mode
    
data = [5, 9, 7, 1, 3, 2, 9, 8, 2, 9]
    
print("Mean: " + str(mean(data)))
print("Median: "  + str(median(data)))
print("Mode: "  + str(mode(data)))
