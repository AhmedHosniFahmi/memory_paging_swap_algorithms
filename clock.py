# initialize processes and split them into list
processes = [int(i) for i in str(input("processes : ")).strip().split(' ')]

# initialize the queue which we will work on
q_length = int(input("queue length : "))
queue = []

# ask user for queue elements if not empty
if int(input("(0) empty queue (1) initialize one : ").strip()) == 1:
    queue = [int(i) for i in str(input("default queue : ")).strip().split(' ')]

# initialize a pointer that refer to an index in the queue
pointer = 0

# initialize another queue to hold the clock counter which will keep track with the operation's queue
use_bit = [] if len(queue) == 0 else [1 for i in range(q_length)]

print("\n\nqueues in every operation : \n\n")

page_fault, page_hit = 0, 0

for process in processes:
    if process not in queue:
        page_fault += 1
        if len(queue) == q_length:
            i = pointer
            while True:
                if use_bit[i] == 1:
                    use_bit[i] -= 1
                    i = (i + 1) % q_length
                    continue
                if use_bit[i] == 0:
                    queue[i] = process
                    use_bit[i] = 1
                    pointer = (i+1) % q_length
                    break
        else:
            page_hit += 1
            queue.append(process)
            use_bit.append(1)
            pointer = (pointer + 1) % q_length
    else:
        if use_bit[queue.index(process)] == 0:
            use_bit[queue.index(process)] += 1

    print("queue : ", str(queue).rjust(q_length + 10), "  use bits : ", str(use_bit).rjust(q_length + 10),
          "  pointer at index: ", str(pointer).rjust(1), "  p(", process, ") inserted")

print(f"\npage hits : {page_hit}")
print(f"page faults : {page_fault}")
