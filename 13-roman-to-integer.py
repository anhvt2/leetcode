class Solution:
    def romanToInt(self, s: str) -> int:
        assert 1 <= len(s) <= 15, "invalid input"
        roman_int_dict = {'I': 1, "V": 5, "X": 10, 'L': 50,'C':100,'D': 500,'M':1000}
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and roman_int_dict[s[i]] < roman_int_dict[s[i+1]]:
                num += (roman_int_dict[s[i+1]] - roman_int_dict[s[i]])
                i += 2
            else:
                num += roman_int_dict[s[i]]
                i += 1
        return num

# from collections import deque

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         keys = ['', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
#         values = [0, 1, 5, 10, 50, 100, 500, 1000]

#         number = 0
#         lists = list(s)

#         RomanDict = dict(zip(keys, values))
#         queue = deque(s)

#         # read from left to right
#         if len(s) == 1:
#             return RomanDict[s[0]]

#         prev_last = ''
#         while queue:
#             curr_last = queue.popleft()
#             number += RomanDict[curr_last]
#             if RomanDict[prev_last] < RomanDict[curr_last] and prev_last != '':
#                 number -= 2*RomanDict[prev_last]
#             prev_last = curr_last
#         return number


# from collections import deque

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         keys = ['', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
#         values = [0, 1, 5, 10, 50, 100, 500, 1000]

#         number = 0
#         lists = list(s)

#         RomanDict = dict(zip(keys, values))
#         queue = deque(s)

#         # read from left to right
#         if len(s) == 1:
#             return RomanDict[s[0]]

#         prev_last = ''
#         while queue:
#             curr_last = queue.popleft()
#             number += RomanDict[curr_last]
#             if RomanDict[prev_last] < RomanDict[curr_last] and prev_last != '':
#                 number -= 2*RomanDict[prev_last]
#             prev_last = curr_last
#         return number

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         RomanDict = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000
#         }
#         total = 0
#         prev = 0
#         for c in reversed(s):
#             curr = RomanDict[c]
#             if curr < prev:
#                 total -= curr
#             else:
#                 total += curr
#             prev = curr
#         return total


# s = "LVIII" # 58
# # s = "MCMXCIV" # 1994
# sol = Solution()
# print(sol.romanToInt(s))
