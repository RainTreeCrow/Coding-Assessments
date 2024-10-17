# Given an array of integers latencies where each element represents recorded latencies,
# and a positive integer threshold,
# your task is to determine the maximum length of a contiguous subarray
# such that the difference between the maximum and minimum latencies within this subarray
# does not exceed threshold.

# Return the length of the longest such contiguous subarray.

from collections import deque

def solution(latencies, threshold):
    min_indices = deque()  # To store the indices of minimum values in the current window
    max_indices = deque()  # To store the indices of maximum values in the current window
    left = 0  # Left pointer of the sliding window
    max_len = 0  # To keep track of the maximum length

    for right in range(len(latencies)):
        # Maintain decreasing order in max_indices
        while max_indices and latencies[max_indices[-1]] <= latencies[right]:
            max_indices.pop()
        max_indices.append(right)

        # Maintain increasing order in min_indices
        while min_indices and latencies[min_indices[-1]] >= latencies[right]:
            min_indices.pop()
        min_indices.append(right)

        # If difference between max and min in the window exceeds the threshold, move the left pointer
        while latencies[max_indices[0]] - latencies[min_indices[0]] > threshold:
            left += 1
            # Remove elements out of the window from both deques
            if max_indices[0] < left:
                max_indices.popleft()
            if min_indices[0] < left:
                min_indices.popleft()

        # Update the maximum length of the window
        max_len = max(max_len, right - left + 1)

    return max_len