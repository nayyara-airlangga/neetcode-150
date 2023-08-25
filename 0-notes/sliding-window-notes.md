# Sliding Window

## References

- [Technical Interview Questions: Sliding Window Technique](https://exceptionly.com/2021/08/17/technical-interview-questions-sliding-window-technique/)
- [Leetcode is Easy! The Sliding Window Pattern.](https://medium.com/@timpark0807/leetcode-is-easy-sliding-window-c44c11cc33e1)

## Overview

### 3 Key Steps

1. Expand our window
2. Meet the condition and process the window
3. Contract our window

### General Rules

We will always need these 3 variables:

1. Window Bounds — I use left and right. Some prefer low and high, or i and j. Whatever you choose, be consistent between problems.
2. Track Condition — Here we used ‘count_of_zeroes’. Try to be as descriptive as possible so when you read your code the variable name makes sense. It helps logically.
3. Return Value — Here we used ‘global_max’. Again, it doesn’t matter what you choose, but be consistent. I use ‘global_max’ and ‘global_min’ for all my sliding window problems.

### Steps

1. Define condition to stop expanding our window
2. Expand our window until we meet that condition but before expanding the window, process the element at the ‘right’ index.
3. If we meet our condition to stop expanding, process the current window.
4. Contract our current window, but before contracting, process the element at the ‘left’ index.
5. Process Edge Cases.
