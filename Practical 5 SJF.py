# Step 1: Get the number of processes
n = int(input("Enter number of processes: "))

# Step 2: Initialize lists to store data
pid = []
burst_time = []
waiting_time = [0] * n
turnaround_time = [0] * n

# Step 3: Take user input for burst times
for i in range(n):
    pid.append(i + 1)
    bt = int(input(f"Enter Burst Time for Process {i + 1}: "))
    burst_time.append(bt)

# Step 4: Sort processes based on Burst Time (Shortest Job First logic)
# We sort both lists together so the Process IDs match their new positions
for i in range(n):
    for j in range(0, n - i - 1):
        if burst_time[j] > burst_time[j + 1]:
            # Swap burst times
            burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
            # Swap process IDs to match
            pid[j], pid[j + 1] = pid[j + 1], pid[j]

# Step 5: Calculate Waiting Time
# The first process doesn't wait (Waiting Time = 0)
waiting_time[0] = 0
for i in range(1, n):
    waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# Step 6: Calculate Turnaround Time (Waiting Time + Burst Time)
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Step 7: Calculate Averages
total_wt = sum(waiting_time)
total_tat = sum(turnaround_time)
avg_wt = total_wt / n
avg_tat = total_tat / n

# Step 8: Display results
print("\nExecution Order: ", " -> ".join([f"P{p}" for p in pid]))
print("\nPID\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{pid[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
