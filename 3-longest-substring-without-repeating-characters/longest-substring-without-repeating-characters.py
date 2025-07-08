class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            counter[c]+=1
            while start <i and any([x for x in counter.values() if x>1]):
                counter[s[start]]-=1
                start +=1
            max_len = max(max_len, i-start+1)
        return max_len
        