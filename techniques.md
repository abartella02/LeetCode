## Sliding window technique
have a left and right pointer that define a window
increment the right pointer each iteration
increment the left only if a condition is not met
i.e. 3, 424


## Two pointer
use two pointers to compare elements in an array in O(n) instead of O(n^2)
i.e. 11

## Fast and slow
Used to traverse linked lists
One pointer moves 2 nodes at a time, one moves one at a time
If there is a cycle, they will meet at the node where the cycle begins
i.e. 19

## Gas and car
Used to traverse nodes where some kind of 'fuel' is required (literally fuel or something like
jump distance). Don't use the next node's fuel unless it is greater than the fuel you have
already accumulated. If you run out of gas, traversing that path is not possible.
i.e. 55

