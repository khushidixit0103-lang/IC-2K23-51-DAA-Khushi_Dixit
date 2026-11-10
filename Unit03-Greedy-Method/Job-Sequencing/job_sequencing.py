"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 03: Greedy Method
Experiment: Job Sequencing with Deadlines

Problem Statement:
Given N jobs where every job has a deadline and associated profit if completed
within the deadline. Each job takes 1 unit of time to complete and only one machine
is available. Schedule jobs to maximize total profit.
Greedy Choice: Sort jobs by profit in descending order and schedule each job in the
latest available free time slot before its deadline.
"""

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"Job({self.job_id}: dl={self.deadline}, profit={self.profit})"


def job_sequencing(jobs):
    """
    Schedules jobs to maximize profit using Greedy choice.
    
    Returns:
        tuple: (total_profit, scheduled_sequence)
    """
    # 1. Sort jobs in descending order of profit
    sorted_jobs = sorted(jobs, key=lambda j: j.profit, reverse=True)
    
    # 2. Find maximum deadline to determine timeline capacity
    max_deadline = max(j.deadline for j in jobs) if jobs else 0
    
    # Time slots from 1 to max_deadline (0 is unused, None indicates empty slot)
    slots = [None] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs = []
    
    # 3. Greedily place jobs into latest permissible slot
    for job in sorted_jobs:
        # Search backwards from min(max_deadline, job.deadline) down to 1
        for slot in range(job.deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job
                total_profit += job.profit
                scheduled_jobs.append((slot, job))
                break
                
    # Sort scheduled jobs chronologically by time slot
    scheduled_jobs.sort(key=lambda x: x[0])
    return total_profit, scheduled_jobs, slots


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 3 - JOB SEQUENCING WITH DEADLINES")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    jobs = [
        Job("J1", deadline=4, profit=70),
        Job("J2", deadline=1, profit=80),
        Job("J3", deadline=2, profit=30),
        Job("J4", deadline=1, profit=100),
        Job("J5", deadline=2, profit=60),
        Job("J6", deadline=3, profit=40),
        Job("J7", deadline=4, profit=20)
    ]
    
    print(f"Total Available Jobs ({len(jobs)}):")
    for j in jobs:
        print(f"  {j.job_id} | Deadline: t={j.deadline} | Profit: {j.profit}")
        
    total_profit, schedule, slots = job_sequencing(jobs)
    
    print("\n--- Final Greedy Job Schedule (Chronological Order) ---")
    for slot, job in schedule:
        print(f"  Time Slot [{slot-1} -> {slot}]: Executed {job.job_id} (Profit: {job.profit}, Deadline: {job.deadline})")
        
    print("-" * 70)
    print(f"  Total Scheduled Jobs : {len(schedule)}")
    print(f"  Total Maximum Profit : {total_profit}")
    print("=" * 70)


if __name__ == "__main__":
    main()
