data = []

with open('input1.txt') as f:
    for line in f:
        data.append(int(line))

data = sorted(data)

def day1_part1(array):
    for i in range(len(array)):
        for k in range(len(array) - 1, -1, -1):
            val = array[i] + array[k]
            if val == 2020:
                return array[i]*array[k]
            elif val < 2020:
                break
                
def day1_part2(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            val = array[i] + array[j]
            if val >= 2020:
                break
            for k in range(len(array)):
                val2 = val + array[k]
                if val2 > 2020:
                    break
                elif val2 == 2020:
                    return array[i]*array[j]*array[k]
                
print(day1_part1(data)) 
print(day1_part2(data))
