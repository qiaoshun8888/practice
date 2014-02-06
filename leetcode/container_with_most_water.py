class Solution:
    # @return an integer

    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0

        best = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = 0
            width = right - left
            if height[left] > height[right]:
                area = width * height[right]
                right -= 1
            else:
                area = width * height[left]
                left += 1
            if area > best:
                best = area
        return best


def main():
    s = Solution()
    print s.maxArea([0, 2])

if __name__ == '__main__':
    main()
