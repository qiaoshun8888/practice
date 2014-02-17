class Solution:
    # @return a string

    def minWindow(self, S, T):
        window_start = 0
        window_end = 0
        window_char = [None, None]
        window_chars = {}
        for k, i in enumerate(s):
            if i in T:
                if i not in window_chars:
                    window_chars[i] = [k]
                    if window_start:
                else:
                    window_chars[i].append(k)

