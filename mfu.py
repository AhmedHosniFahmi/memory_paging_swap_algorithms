"""
#################################################################################
MFU implementation in the right way (I think)
Algorithm followed explanation link : https://www.youtube.com/watch?v=SvZe7DljziM
#################################################################################
"""
# initialize processes and split them into list
processes = [int(i) for i in str(input("processes : ")).strip().split(' ')]

# initialize the queue which we will work on
q_length = int(input("queue length : "))
queue = []

# ask user for queue elements if not empty
if int(input("(0) empty queue (1) initialize one : ").strip()) == 1:
    queue = [int(i) for i in str(input("default queue : ")).strip().split(' ')]

# initialize another queue to locate the least recently used process and their counter
# least recently used -> [p1, p2, p3, p4, p5] <- Most recently used
lru_queue = [] if len(queue) == 0 else [i for i in queue]

# initialize another counter queue which we will update with the lru_queue
count_queue = [] if len(queue) == 0 else [1 for i in queue]

page_fault, page_hit = 0, 0

print("\n\nqueues in every operation : \n\n")

for process in processes:
    if process not in queue:
        page_fault += 1
        # if the queue is full we look for the frequency if it's equal we delete the most recently used
        if len(queue) == q_length:
            # getting a list of max counter occurrence in the counter list
            indices = [i for i, x in enumerate(count_queue) if x == max(count_queue)]

            # add the new process to the queue
            queue[queue.index(lru_queue[indices[0]])] = process

            # remove the least recently used or most frequently used process then add the new process to be the most recently used
            del lru_queue[indices[0]]
            lru_queue.append(process)

            # edit the counter queue to keep track with the LRU queue
            count_queue.remove(count_queue[indices[0]])
            count_queue.append(1)

        # if the queue isn't full
        else:
            # add the process to the queue
            queue.append(process)
            # add the process to LRU queue to keep track of it's use
            lru_queue.append(process)
            # add a counter = 1 for the process in the counter queue
            count_queue.append(1)

    else:
        page_hit += 1
        # increment the counter for the process
        temp = count_queue[lru_queue.index(process)] + 1
        count_queue.remove(count_queue[lru_queue.index(process)])
        count_queue.append(temp)

        # update the LRU queue to keep track of processes use
        lru_queue.remove(process)
        lru_queue.append(process)

    print("queue : ", str(queue).rjust(q_length+10), "  lru_queue : ", str(lru_queue).rjust(q_length+10),
          "  counter : ", str(count_queue).rjust(q_length+10), "  p(", process, ") inserted")

print(f"\npage hits : {page_hit}")
print(f"page faults :  {page_fault}")
