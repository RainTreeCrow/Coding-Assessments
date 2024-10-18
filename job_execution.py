# There are n jobs that can be executed in parallel on a processor,
# where the execution time of the ith job is executionTime[i].
# To speed up execution, the following strategy is used.

# In one operation, a job is chosen, the major job, and is executed for x seconds.
# All other jobs are executed for y seconds where y < x.

# A job is complete when it has been executed for at least executionTime[i], then it exits the pool.
# Find the minimum number of operations to completely execute all the jobs if run optimally.

import heapq

def getMinimumOperations(executionTime, x, y):
    # Use negative values to simulate a max heap since heapq is a min heap
    time_left = [-time for time in executionTime]
    heapq.heapify(time_left)
    
    # Initialize the current threshold and the number of operations
    threshold = 0
    operations = 0
    
    # Process the heap until it is empty
    while time_left:
        # Pop the top element from the heap (negate it to get the actual value)
        major_time = -heapq.heappop(time_left)
        
        # If the task's remaining time is below threshold, all tasks are complete
        if major_time <= threshold:
            return operations
        
        # Update the remaining time for the major task
        updated_time = major_time - (x - y)

        # Push it back into the heap if it's not yet complete
        if updated_time > 0:
            heapq.heappush(time_left, -updated_time)
        
        # Increment the threshold, meaning all minor tasks have executed for y seconds
        threshold += y
        
        # Increment the operation count
        operations += 1
    
    # Return the number of operations required to complete all tasks
    return operations

print(getMinimumOperations([3, 4, 1, 7, 6], 4, 2))