"""Lesson 13 — List methods. Author: Adarsh."""
fruits = ["banana", "apple"]

fruits.append("cherry")           # add to the end
print(fruits)                     # ['banana', 'apple', 'cherry']

fruits.insert(1, "mango")         # insert at index
print(fruits)

fruits.remove("apple")            # remove first matching VALUE
popped = fruits.pop()             # remove and return LAST item
print(popped, fruits)

del fruits[0]                     # delete by INDEX
print(fruits)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                       # sort in place (ascending)
print(nums)
nums.sort(reverse=True)           # descending
print(nums)
print(sorted("python"))           # sorted() works on any iterable -> list

nums2 = [3, 1, 4]
print(sorted(nums2, reverse=True))
print(nums2)                      # unchanged — sorted() returns new list

nums.extend([5, 5])               # add many items at the end
print(nums2 + [5, 5])             # same result via +
print(nums.count(1))              # count occurrences
print(nums.index(9))              # position of first 9
nums.reverse()                    # flip order in place

words = ["pear", "fig", "banana"]
print(sorted(words, key=len))     # sort by custom key: length

nums3 = [1, 2, 3, 4, 5]
print(sum(nums3), min(nums3), max(nums3))   # 15 1 5

# Practice: given [5, 3, 8, 1], sort descending then insert 4 in the right spot.
