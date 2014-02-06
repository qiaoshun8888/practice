class Solution:
    # @return an integer

    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0

        best = 0
        for k, i in enumerate(height):
            w = 0
            for j in height[k + 1:]:
                w += 1
                if j < i:
                    break
            area = i * w
            if best < area:
                best = area

        return best


def main():
    s = Solution()
    print s.maxArea([1, 2, 1])

if __name__ == '__main__':
    main()
