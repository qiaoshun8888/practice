class Solution:
    # @param num, a list of integer
    # @return an integer

    def longestConsecutive(self, num):
            dic = {}
            visited = set()
            maximum = 1
            for i in num:
                if i in visited:
                    continue
                visited.add(i)

                if i + 1 not in dic and i - 1 not in dic:
                    dic[i] = [i]
                elif i + 1 in dic and i - 1 in dic:
                    # print dic[i - 1], dic[i + 1]
                    tmp = dic[i - 1] + [i] + dic[i + 1]
                    tmp_end = dic[i + 1][-1]
                    tmp_start = dic[i - 1][0]
                    del dic[i + 1]
                    dic[tmp_end] = tmp
                    dic[tmp_start] = tmp
                elif i + 1 in dic:
                    tmp = [i] + dic[i + 1]
                    tmp_end = dic[i + 1][-1]
                    del dic[i + 1]
                    dic[tmp_end] = tmp
                    dic[i] = tmp
                elif i - 1 in dic:
                    tmp = dic[i - 1] + [i]
                    tmp_start = dic[i - 1][0]
                    del dic[i - 1]
                    dic[i] = tmp
                    dic[tmp_start] = tmp
                # print dic
            maximum = max([len(i) for i in dic.values()])
            return maximum


if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
