class Solution:
    # @return an integer

    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0

        best = float('-inf')
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] > height[right]:
                best = max(best, (right - left) * height[right])
                right -= 1
            else:
                best = max(best, (right - left) * height[left])
                left += 1
        return best


def main():
    s = Solution()
    print s.maxArea([0, 2])

if __name__ == '__main__':
    main()
