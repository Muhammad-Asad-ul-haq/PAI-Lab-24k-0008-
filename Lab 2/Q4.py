numbers = (-78, 54, 5, -1, 6)

length = len(numbers)


closest_sum = numbers[0] + numbers[1]
pair = (numbers[0], numbers[1])

for i in range(length):
    for j in range(i+1, length):
        s = numbers[i] + numbers[j]

        
        if (s >= 0 and closest_sum < 0 and s < -closest_sum) or \
           (s <= 0 and closest_sum > 0 and -s < closest_sum) or \
           (s >= 0 and closest_sum >= 0 and s < closest_sum) or \
           (s <= 0 and closest_sum <= 0 and s > closest_sum):

            closest_sum = s
            pair = (numbers[i], numbers[j])

print("Pair:", pair)
print("Sum:", closest_sum)
