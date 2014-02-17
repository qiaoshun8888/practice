class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def permuteUnique(self, num):
        if len(num) <= 1:
            return [num]
        else:
            visited = set()
            result = list()
            for t in num:
                if t not in visited:
                    tmp = list(num)
                    tmp.remove(t)
                    for i in self.permuteUnique(tmp):
                        # if [t] + i not in result:
                        result.append([t] + i)
                    visited.add(t)
            return list(result)


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([-1, 2, -1, 2, 1, -1, 2, 1])
