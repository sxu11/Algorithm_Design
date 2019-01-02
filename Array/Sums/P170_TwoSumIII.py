
'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false




Method 1: Old method, based on TwoSum (Return the
unique true pair's INDs).

Method 2: REALLY smart.
Since the requirement is weakened, now only need to
know whether "there exists or not".
So cnt does not matter.

How to come up w/ Method 2?
If dare to use dict to think, should not be too hard.

'''

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.method  = 1

        if self.method == 0:
            self.sorted_list = []

        elif self.method == 1:
            self.dict = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if self.method == 0:
            import bisect
            bisect.insort(self.sorted_list, number)

        elif self.method == 1:
            if number in self.dict:
                self.dict[number] += 1
            else:
                self.dict[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        if self.method == 0:
            i = 0
            j = len(self.sorted_list) - 1
            while i < j:
                if self.sorted_list[i] + self.sorted_list[j] == value:
                    return True
                elif self.sorted_list[i] + self.sorted_list[j] < value:
                    i += 1
                else:
                    j -= 1
            return False

        elif self.method == 1:
            for num in self.dict:
                if value-num in self.dict and (num != value-num or self.dict[num]>1):
                    return True
            return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)