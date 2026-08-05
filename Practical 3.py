# FCFS Scheduling Program

# code by OpenAI Agent ChatGPT GPTv4.2


# unit 2 Process Scheduling 

n = int(input("Enter the number of processes: "))

processes = []
burst_time = []

for i in range(n):
    processes.append(input(f"Enter Process ID for P{i+1}: "))
    burst_time.append(int(input(f"Enter Burst Time for {processes[i]}: ")))

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate Waiting Time
for i in range(1, n):
    waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Calculate Average Times
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

# Display Results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
