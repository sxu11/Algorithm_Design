def callChunk(s):  # chunk of 3 or less
    names = {
        "0": "",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "15": "Fifteen",
        "18": "Eighteen"
    }

    if s == "000" or s == "00":
        res = ""
    elif len(s) == 1:
        res = names[s]
    elif len(s) == 2:
        if s[0] == "1":
            if s in names:
                res = names[s]
            else:
                res = names[s[1]] + "teen"  # 14
        elif s[0] == "2":
            res = " ".join(["Twenty", names[s[1]]])
        elif s[0] == "3":
            res = " ".join(["Thirty", names[s[1]]])
        elif s[0] == "4":
            res = " ".join(["Forty", names[s[1]]])
        elif s[0] == "5":
            res = " ".join(["Fifty", names[s[1]]])
        elif s[0] == "8":
            res = " ".join(["Eighty", names[s[1]]])
        else:
            res = " ".join([names[s[0]] + "ty", names[s[1]]])
    elif len(s) == 3:
        res = " ".join([names[s[0]], "Hundred", callChunk(s[1:])])

    return res.strip()


"""
edge cases:
0
10 ten
11 eleven
12 twelve
21 twenty one
1000
"""


# TODO: Wrong at 14!!!
# I gave "Oneteen", expected "Fourteen"

# TODO: Wrong at 20 !!!
# I gave "Twenty ", expected "Twenty"

# TODO: Wrong at 100 !!!
# "One Hundred ty", "One Hundred"

# TODO: below all wrong!
# 1000, "One Thousand Hundred ty"
# 10000, "Ten Thousand Hundred ty"
# 100000, "One Hundred ty Thousand Hundred ty"
# 1000000, "One Million Hundred ty Thousand Hundred ty"
# 10000000, "Ten Million Hundred ty Thousand Hundred ty"
# 100000000, "One Hundred ty Million Hundred ty Thousand Hundred ty"
# 1000000000, "One Billion Hundred ty Million Hundred ty Thousand Hundred ty"
# 1000000001, "One Billion Hundred ty Million Hundred ty Thousand Hundred ty One"


class Solution:
    def numberToWords(self, num: int) -> str:
        s = str(num)
        if s == "0":
            return "Zero"

        orders = ["Thousand", "Million", "Billion"]
        len_s = len(s)
        if len_s > 9:
            res = " ".join([callChunk(s[:len_s - 9]),
                            "Billion",
                            callChunk(s[len_s - 9:len_s - 6]),
                            "Million",
                            callChunk(s[len_s - 6:len_s - 3]),
                            "Thousand",
                            callChunk(s[len_s - 3:])])
        elif len_s > 6:
            res = " ".join([callChunk(s[:len_s - 6]),
                            "Million",
                            callChunk(s[len_s - 6:len_s - 3]),
                            "Thousand",
                            callChunk(s[len_s - 3:])])
        elif len_s > 3:
            res = " ".join([callChunk(s[:len_s - 3]),
                            "Thousand",
                            callChunk(s[len_s - 3:])])
        else:
            res = callChunk(s)
        return res.strip()