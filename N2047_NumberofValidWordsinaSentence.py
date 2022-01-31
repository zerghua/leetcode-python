#
# Create by Hua on 1/31/22.
#

"""
" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "


A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'),
hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only.
Each sentence can be broken down into one or more tokens separated
by one or more spaces ' '.

A token is a valid word if all three of the following are true:

    1. It only contains lowercase letters, hyphens, and/or
    punctuation (no digits).
    2. There is at most one hyphen '-'. If present, it must be surrounded
    by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
    3. There is at most one punctuation mark. If present, it must be at the
    end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.,"
    are not valid).

Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.



Example 1:
Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".

Example 2:
Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.

Example 3:
Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are",
and "playing".
"stone-game10" is invalid because it contains digits.



Constraints:
    1 <= sentence.length <= 1000
    sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
    There will be at least 1 token.
"""


class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int

        easy 30min, stragihtforward but long code.

        thought: split words by space, and validate each word with the above
        3 rules.

        corner case: "q-,"

        1. It only contains lowercase letters, hyphens, and/or
        punctuation (no digits).
        2. There is at most one hyphen '-'. If present, it must be surrounded
        by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
        3. There is at most one punctuation mark. If present, it must be at the
        end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.,"
        are not valid).

        01/31/2022 14:12	Accepted	54 ms	13.6 MB	python

        """

        def is_word(w):
            import string
            digits = "0123456789"
            marks = "!,."
            hyphen = "-"
            count_of_marks = 0
            count_of_hyphen = 0
            mark_pos = 0
            hyphen_pos = 0

            for i in range(len(w)):
                c = w[i]
                if c in digits: return False   # rule 1
                if c in marks:
                    count_of_marks += 1
                    mark_pos = i
                if c in hyphen:
                    count_of_hyphen += 1
                    hyphen_pos = i

            if count_of_marks > 1 or count_of_hyphen > 1: return False

            # rule 2
            if count_of_hyphen == 1:
                if len(word) < 3: return False
                if hyphen_pos == 0 or hyphen_pos == len(word) - 1: return False

                # corner case: "q-,"
                if w[hyphen_pos-1] and w[hyphen_pos+1] not in string.ascii_lowercase:
                    return False

            # rule 3
            if count_of_marks == 1:
                if mark_pos != len(word) - 1: return False

            return True

        ret = 0
        for word in sentence.split():
            if is_word(word):
                ret += 1
        return ret

