def moving_average(numbers, window_size):
    moving_averages = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        window_average = sum(window) / window_size
        moving_averages.append(window_average)
    return moving_averages

numbers = [54, 65, 98, 95, 78, 65, 45, 87, 45, 12, 54, 32, 15, 8, 6, 7, 17, 25, 30, 41, 48, 49, 43, 40, 30, 25, 22, 20, 19]
window_size = 3
result = moving_average(numbers, window_size)
print(result)

