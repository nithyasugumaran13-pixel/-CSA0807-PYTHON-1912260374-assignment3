
import random
import time


# Generate rainfall readings for 365 days
readings = [random.randint(0, 50) for _ in range(365)]

# 1. Calculate weekly rainfall totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    week = readings[i:i + 7]
    weekly_totals.append(sum(week))

print("Weekly rainfall totals:", weekly_totals)

# 2. Find wettest and driest weeks
wettest = max(weekly_totals)
driest = min(weekly_totals)

print("Wettest week:", weekly_totals.index(wettest) + 1)
print("Wettest rainfall:", wettest, "mm")

print("Driest week:", weekly_totals.index(driest) + 1)
print("Driest rainfall:", driest, "mm")

# 3. Naive 7-day moving average
def naive_average(data):
    averages = []

    for i in range(len(data) - 6):
        total = 0
        for j in range(7):
            total += data[i + j]

        averages.append(total / 7)

    return averages


# 4. Running-sum 7-day moving average
def running_average(data):
    if len(data) < 7:
        return []

    averages = []
    total = sum(data[:7])
    averages.append(total / 7)

    for i in range(7, len(data)):
        total = total - data[i - 7] + data[i]
        averages.append(total / 7)

    return averages


naive = naive_average(readings)
running = running_average(readings)

print("Number of 7-day averages:", len(naive))
print("First 5 moving averages:", running[:5])

# 5. Find dry days
dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("Dry days:", dry_days)

# 6. Performance comparison
print("\nPERFORMANCE COMPARISON")

for n in [365, 36500, 365000]:

    data = [random.randint(0, 50) for _ in range(n)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("\nReadings:", n)
    print("Naive time:", naive_time, "seconds")
    print("Running sum time:", running_time, "seconds")

# 7. Edge case testing
print("\nEDGE CASE TESTING")

print("Empty list:", running_average([]))
print("Short list:", running_average([2, 4, 6, 8, 10]))
