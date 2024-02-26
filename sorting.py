print("Py1 created")

#implement list comprehension
x = [y for y in range(12)]

class Sorting:
    def __init__(self, nums):
        self.nums = nums
        self.length = len(self.nums)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def selection_sort(self):
        for i in range(self.length):
            min_index = i
            for j in range(i + 1, self.length):
                if self.nums[j] < self.nums[min_index]:
                    min_index = j
            if min_index != i:
                self.swap(i, min_index)
        return self.nums

    def insertion_sort(self):
        for i in range(1, self.length):
            j = i
            while j > 0 and self.nums[j] < self.nums[j - 1]:
                self.swap(j, j - 1)
                j -= 1
        return self.nums

    def bubble_sort(self):
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.nums[j] < self.nums[i]:
                    self.swap(i, j)
        return self.nums


sort = Sorting([12, 4, 1, -7, 6, 2, 5, 9])
print(sort.selection_sort())
