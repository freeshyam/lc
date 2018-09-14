#!/usr/bin/env python

class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs:
            prefix = ""
            first_word = strs[0]
            rest = strs[1:]
            for i, c in enumerate(first_word):
                same_char = True
                for word in rest:
                    if word[i:i+1] != c:
                        same_char = False
                        break
                if c and same_char:
                    prefix += c
                else:
                    break
            return prefix
        return ""

    def longestCommonPrefix2(self, strs):
        if strs:
            prefix = ""
            i = 0
            while True:
                c = reduce(lambda x, y: x if x == y else False,
                           map(lambda w: w[i:i+1], strs))
                if c:
                    prefix += c
                    i += 1
                else:
                    break
            return prefix
        return ""

if __name__ == "__main__":
    t = Solution()
    ll = [["animal", "animate", "anim", "animaestro"],
          ["zajldajh", "zajjakdl", "zajsasdal"],
          ["", "", ""],
          []]

    for ls in ll:
        print "LCP of words in {}: '{}'".format(ls, t.longestCommonPrefix(ls))
        print "LCP of words in {}: '{}'".format(ls, t.longestCommonPrefix2(ls))
