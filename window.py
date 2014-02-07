class Solution:
    best_length = float('inf')
    results = []
    # @return a string

    def minWindow(self, S, T):
        for si, i in enumerate(S):
            # print i
            # for r in self.results:
            #     r.append(i)
            #     if r[0] == i:
            #         self.results1.append(r)
            #         self.results.remove(r)
            removable = []
            for ri, r in enumerate(self.results):
                if not r[1]:
                    if len(r[0]) < self.best_length:
                        self.best_length = len(r[0])
                    # else:
                    #     self.results.pop(ri)

                if i in r[1]:
                    r[1].remove(i)
                r[0].append(i)

                if i in T and r[1] and i not in r[1]:
                    # print r
                    removable.append(r)
                    continue

            # print removable

            # for r in removable:
            #     self.results.remove(r)

            if i in T:
                lacking = list(T)
                lacking.remove(i)
                self.results.append(([i], lacking))

        for r in self.results:
            print r


def main():
    s = Solution()
    s.minWindow('ADOBECODEBANC', 'ABC')

if __name__ == '__main__':
    main()
