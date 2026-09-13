def calculate_fcfs_scheduling():
    print("--- FCFS CPU Scheduling Calculator ---")
    
    # 1. Take user input for number of processes
    n = int(input("Enter the number of processes: "))
    
    processes = []
    
    # 2. Collect Arrival Time (AT) and Burst Time (BT) for each process
    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter Arrival Time for {pid}: "))
        bt = int(input(f"Enter Burst Time for {pid}: "))
        processes.append({"id": pid, "at": at, "bt": bt})
        
    # 3. Sort processes strictly based on Arrival Time (FCFS Rule)
    processes.sort(key=lambda x: x["at"])
    
    current_time = 0
    total_tat = 0
    total_wt = 0
    
    print("\nExecution Table:")
    print(f"{'Process':<10}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}")
    print("-" * 50)
    
    for p in processes:
        # If the CPU is idle waiting for the next process to arrive
        if current_time < p["at"]:
            current_time = p["at"]
            
        # Completion Time (CT) = Current Time + Burst Time
        ct = current_time + p["bt"]
        
        # Turnaround Time (TAT) = Completion Time - Arrival Time
        tat = ct - p["at"]
        
        # Waiting Time (WT) = Turnaround Time - Burst Time
        wt = tat - p["bt"]
        
        # Update metrics tracking totals
        total_tat += tat
        total_wt += wt
        
        # Advance current time clock to this process's completion time
        current_time = ct
        
        print(f"{p['id']:<10}{p['at']:<8}{p['bt']:<8}{ct:<8}{tat:<8}{wt:<8}")
        
    # 4. Calculate and display Averages
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    
    print("-" * 50)
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

if __name__ == "__main__":
    calculate_fcfs_scheduling()
