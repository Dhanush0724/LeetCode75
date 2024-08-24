class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels  = set('aeiou')
        max_vow = 0
        curr_vow  = 0

        for i in range(k):
            if s[i] in vowels:
                curr_vow+=1
        max_vow = curr_vow

        for i in range(k,len(s)):

            if s[i] in vowels:
                curr_vow+=1
            if s[i-k] in vowels:
                curr_vow-=1
            max_vow = max(max_vow,curr_vow)

            if max_vow == k:
                break
        
        return max_vow




        
