class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            string = "".join(sorted(s))
            if string in hashmap:
                hashmap[string].append(s)
            else:
                hashmap[string] = [s]
        
        return list(hashmap.values())

            
        