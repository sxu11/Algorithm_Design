"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

def addCharToExistingValidStrings(c, existingValidStrings):
    newValidStrings = set()
    for existingValidString in existingValidStrings:
        newValidString = existingValidString + c
        newValidStrings.add(newValidString)

    return newValidStrings

def removeCharByIndToCurrentStillValidStrings(ind, existingValidStrings):
    newValidStrings = set()
    for existingValidString in existingValidStrings:
        newValidString = existingValidString[:ind] + existingValidString[ind+1:]
        newValidStrings.add(newValidString)

    return newValidStrings

def extendStillValidStringsAtIndI(s, i, currentStillValidStrings, leftStack, rightStack):
    """ N -> N + 1
    Conclusion: This is the iteration method, however too different to handle status (leftStack, rightStack) branching

    What is (still)validString:

    From current prefix, s[:i], we have the current existingValidStrings
        status are saved in leftStack, rightStack
    Return:
         newValidStrings, by adding s[i]


    Current input is s[i]
    - if s[i] is "(", still valid so far
        put into leftStack
    - elif s[i] is char, still valid so far
        keep going

    - s[i] is ")", need to compare len(leftInds) vs len(rightInds)
        - if len(leftInds) > len(rightInds), valid so far
            put into rightStack
        - else [checkpt] remove any one from left, combine with prefix set, return list of valid strings

    """
    if i == len(s):
        """ end of string """
        return currentStillValidStrings

    """ has sth to do """
    if s[i] == "(":
        leftStack.append(i)
        existingValidStrings = addCharToExistingValidStrings(s[i], currentStillValidStrings)
    elif s[i] == ")":
        if len(leftStack) > len(rightStack):
            existingValidStrings = addCharToExistingValidStrings(s[i], currentStillValidStrings)
            rightStack.append(i)
        else:
            """ broken """
            allNewStillValidStrings = set()
            for rightParentheseInd in rightStack:
                """ remove any 1 ')', and in each case:
                        start new branch, to collect all resulted eachNewValidStrings
                    add all eachNewValidStrings into new Set"""
                eachNewStillValidStrings = removeCharByIndToCurrentStillValidStrings(rightParentheseInd, currentStillValidStrings)
                newRightStack = rightStack.remove(rightParentheseInd) + [i]
                # newStrings = extendStillValidStringsAtIndI(s, i + 1, newValidStrings, leftStack, newRightStack)

                # newexistingValidStrings.add(newValidString)
            #     TODO: add here!

            existingValidStrings = newexistingValidStrings

    else:
        existingValidStrings = addCharToExistingValidStrings(s[i], currentStillValidStrings)

    # print existingValidStrings

    print i, existingValidStrings, leftStack, rightStack

    return extendStillValidStringsAtIndI(s, i+1, existingValidStrings, leftStack, rightStack)


class Solution:
    def removeInvalidParentheses(self, s):
        return extendStillValidStringsAtIndI(s, 0, set([""]), [], [])

tests = {
"()())()":["()()()", "(())()"],
# "(a)())()":["(a)()()", "(a())()"],
# ")(":[""]
}

sol = Solution()
for testInput, testOutput in tests.items():
    myOutput = sol.removeInvalidParentheses(testInput)
    print myOutput
    print testOutput
    print