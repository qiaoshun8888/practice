
class Solution:
    # @return a list of integers

    def generate(self, numRows):
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue
            if i == 1:
                res.append([1, 1])
                continue
            last_layer = res[i - 1]
            this_layer = [1]
            for i in range(len(last_layer) - 1):
                this_layer.append(last_layer[i] + last_layer[i + 1])
            this_layer.append(1)
            res.append(this_layer)
        return res

    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        last_layer = [1, 1]
        this_layer = [1]
        for i in range(rowIndex - 1):
            for i in range(len(last_layer) - 1):
                this_layer.append(last_layer[i] + last_layer[i + 1])
            this_layer.append(1)
            last_layer = this_layer
            this_layer = [1]
        return last_layer

if __name__ == '__main__':
    s = Solution()
    print s.getRow(0)
