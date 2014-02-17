class Solution:
    # @param strs, a list of strings
    # @return a list of strings

    def ana(self, s):
        ana = 0
        for k, i in enumerate('abcdefghijklmnopqrstuvwxyz'):
            ana = ana * 26 + k * s.count(i)
        return ana

    def anagrams(self, strs):
        anadic = {}
        anakey = None
        for i in strs:
            if i:
                if self.ana(i) in anadic:
                    anakey = self.ana(i)
                    anadic[self.ana(i)].append(i)
                else:
                    anadic[self.ana(i)] = [i]

        if anakey:
            return anadic[anakey]
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    print s.anagrams([''])
    print s.anagrams(
        ['nolzze', "nozzle", "punjabi", "waterlogged", "imprison", "crux", "numismatists", "sultans", "rambles", "deprecating", "aware", "outfield", "marlborough", "guardrooms", "roast", "wattage", "shortcuts", "confidential", "reprint", "foxtrot", "dispossession", "floodgate", "unfriendliest", "semimonthlies", "dwellers", "walkways", "wastrels", "dippers", "engrossing", "undertakings",
         "unforeseen", "oscilloscopes", "pioneers", "geller", "neglects", "cultivates", "mantegna", "elicit", "couriered", "shielded", "shrew", "heartening", "lucks", "teammates", "jewishness", "documentaries", "subliming", "sultan", "redo", "recopy", "flippancy", "rothko", "conductor", "e", "carolingian", "outmanoeuvres", "gewgaw", "saki", "sarah", "snooping", "hakka", "highness", "mewling", ])
