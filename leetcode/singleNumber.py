class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        # naive way
        s1 = set()
        s2 = set()
        for i in A:
            if i not in s1 and i not in s2:
                s1.add(i)
            elif i in s1:
                s1.remove(i)
                s2.add(i)
        if s1:
            return s1.pop()
        else:
            return None
