class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        word_map = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in pattern_map:
                if pattern_map[char] != word:
                    return False
            else:
                pattern_map[char] = word

            if word in word_map:
                if word_map[word] != char:
                    return False
            else:
                word_map[word] = char

        return True
        