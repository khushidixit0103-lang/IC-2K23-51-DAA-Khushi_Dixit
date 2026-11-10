"""
Program: part2_stack_queue.py
Description: Simulates task processing using Stack (LIFO) and Queue (FIFO),
             and explains printer job queue scheduling.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Lab Task 1 (Part 2)
"""

from collections import deque

def simulate_stack(tasks):
    print("\n--- 1. Stack Simulation (LIFO - Last-In, First-Out) ---")
    stack = []
    print("Pushing tasks onto stack:")
    for t in tasks:
        stack.append(t)
        print(f"  Push: {t} | Stack state: {stack}")
        
    print("\nProcessing/Popping tasks from stack (Completion Order):")
    completed = []
    while stack:
        done = stack.pop()
        completed.append(done)
        print(f"  Pop (Served): {done} | Stack state: {stack}")
        
    return completed


def simulate_queue(tasks):
    print("\n--- 2. Queue Simulation (FIFO - First-In, First-Out) ---")
    q = deque()
    print("Enqueuing tasks into queue:")
    for t in tasks:
        q.append(t)
        print(f"  Enqueue: {t} | Queue state: {list(q)}")
        
    print("\nProcessing/Dequeuing tasks from queue (Completion Order):")
    completed = []
    while q:
        done = q.popleft()
        completed.append(done)
        print(f"  Dequeue (Served): {done} | Queue state: {list(q)}")
        
    return completed


def printer_simulation(tasks):
    print("\n--- 3. Printer Job Scheduling Analysis ---")
    print("A printer serves incoming print jobs on a first-come, first-served basis.")
    print("Structure required: QUEUE (FIFO)")
    print("Reason: Fairness and order preservation. The first person who sends a print request")
    print("        must have their document printed first without being overtaken by newer requests.")
    print("\nPrinting order for Task1 to Task5:")
    order = list(tasks)
    for idx, job in enumerate(order, 1):
        print(f"  Print Order #{idx}: {job}")
    return order


def main():
    print("=" * 60)
    print("  DAA LAB TASK 1: PART 2 - STACK OR QUEUE")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
    print(f"Tasks arriving in sequence: {tasks}")
    
    stack_order = simulate_stack(tasks)
    print(f"\n=> Final Stack Completion Order: {stack_order}")
    
    queue_order = simulate_queue(tasks)
    print(f"\n=> Final Queue Completion Order: {queue_order}")
    
    printer_order = printer_simulation(tasks)
    print(f"\n=> Final Printer Order: {printer_order}")
    print("=" * 60)


if __name__ == "__main__":
    main()
