class Solution:
    # @return an integer

    def threeSumClosest(self, num, target):
        num.sort()
        i = 0
        j = len(num) - 1
        minimum = float('inf')
        for k in range(1, len(num) - 1):
            i = 0
            j = len(num) - 1
            while i < j:
                if i == k or j == k:
                    break
                # print[num[i], num[k], num[j], ], sum([num[i], num[j], num[k]])
                s = sum([num[i], num[j], num[k]])
                if target > s:
                    i += 1
                elif target < s:
                    j -= 1
                else:
                    return target
                if abs(target - s) < abs(minimum):
                    minimum = target - s
        return target - minimum
        # def helper(num, target, depth):
        # print num, target, depth
        #     if depth == 3:
        #         yield target
        #     else:
        #         for i in num:
        #             tmp = list(num)
        #             tmp.remove(i)
        #             for i in helper(tmp, target - i, depth + 1):
        #                 yield i
        # minimum = float('inf')
        # for i in helper(num, target, 0):
        #     if abs(i) < abs(minimum):
        #         minimum = i
        #         if minimum == 0:
        #             break
        # return target - minimum


if __name__ == '__main__':
    s = Solution()
    # print s.threeSumClosest([13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15,
    # 20, 5, 13, 14, -17, -7, 12, -6, 0, 20, -19, -1, -15, -2, 8, -2, -9, 13,
    # 0, -3, -18, -9, -9, -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20,
    # 18, 9, 0, 12, -1, 10, -17, -11, 16, -13, -14, -3, 0, 2, -18, 2, 8, 20,
    # -15, 3, -13, -12, -2, -19, 11, 11, -10, 1, 1, -10, -2, 12, 0, 17, -19,
    # -7, 8, -19, -17, 5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7,
    # 0, -16, -5, 16, -12, 0, 2, -16, 14, 18, 12, 13, 5, 0, 5, 6], -59)
    print s.threeSumClosest([-1, 2, 1, -4], 1)
