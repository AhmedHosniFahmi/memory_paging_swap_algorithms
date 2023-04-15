# initialize processes and split them into list
processes = [int(i) for i in str(input("processes : ")).strip().split(' ')]

# initialize the queue which we will work on
q_length = int(input("queue length : "))
queue = []

# ask user for stack elements if not empty
if int(input("(0) empty queue (1) initialize one : ").strip()) == 1:
    queue = [int(i) for i in str(input("default queue : ")).strip().split(' ')]

page_fault, page_hit = 0, 0

print("\n\nqueues in every operation : \n\n")

for process in processes:
    if process not in queue:
        page_fault += 1
        if len(queue) == q_length:
            queue.pop(0)
            queue.append(process)
        else:
            queue.append(process)
    else:
        page_hit += 1

    print("queue : ", str(queue).rjust(q_length+10), "  p(", process, ") inserted")

print(f"\npage hits : {page_hit}")
print(f"page faults : {page_fault}")









