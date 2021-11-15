### 1 Two Sum
Use Hashmaps to map values to idcs
Check differences
Time:   O(n)
Memory: O(n)

### 121 Best Time to Buy and Sell
Pointer to buy, sell, profit
Time: O(n)
Memory: O(1)

### 217. Contains Duplicate

### 238. Product of Array Except Self [not solved]
Use suffix and prefix list
Time: O(n)
Memory: O(n)

### 53. Maximum Subarray
Use curr_sum and max_sum. Reset  curr_sum to current value if curr_sum is < 0 as sum will always get smaller then.
Time O(n)
Memory O(1)

### 152. Maximum Product Subarray
Dynmic Programming
maintain values of current max and current min of product and check if cur_max is larger than global max
Zero will split array into subarrays

Time O(n)
Memory O(1)


### 153. Find Minimum in Rotated Sorted Array
binary search with left and right pointer. split array and search either left or right portion of array

Time O(logn)
Memory O(1)

### 33. Search in Rotated Sorted Array
discret cases! binary search where we check if right or left subarray is sorted. for the sorted array, we determine if the element is inside, if not it must be in the other subarray not not there!

Time O(logn)
Memory O(1)


### 15. 3Sum
Work with sorted array to eliminate duplicates. Fix one of the three values and the rest reduces to "Two Sum"

Time: O(nlogn) + O(n**2) -> O(n**2)
Space: Depend on use of hashmap or pointer and sorting! O(n)

### 11. Container With Most Water
pointer left and right, update left if height[l] < height[r] and vice versa

Time: O(n)
Memory: O(1)

### 191. Number of 1 Bits
Smart: n AND (n-1)
Time O(1)
Memory O(n)

### 338. Counting Bits
number of bits are the same as previous number of bits + 1 when going in 2**n steps
Time: O(n)
Memory: O(n)

### 268. Missing Number
(n XOR n) = 0, (n XOR j XOR n XOR j) = 0 -> xor is invariant to permutations!
Time: O(n)
Memory: O(1)

### 190. Reverse Bits
Usinf Logic AND, OR and shifting ;)
Time O(1)
Mem O(1)

### 70. Climbing Stairs
Option 1)
Decision Tree with choice 1 or 2 steps. recursive search with map to prevent multiple calculations.
Draw tree to see how many choices are duplicate
Binary Tree of hight n -> 2^2 Timecomplexity which is really bad!
Memory O(n)
Time O(n)

Option 2)
Bottom Up Calculation with O(1) extra memory! (See Fibonacci)
Time O(n)
Memory O(1)
