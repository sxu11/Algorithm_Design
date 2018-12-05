class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        sorted_A = sorted(A)[::-1]  # big to small

        ''' check the 1st digit '''
        res = ""
        for i in range(4):
            if sorted_A[i] > 2:
                continue

            else:
                # 2
                # 1
                # 0
                res += str(sorted_A[i])

                '''
                2nd digit
                '''
                rest_of_A = sorted_A[:i] + sorted_A[i + 1:]
                if sorted_A[i] == 2:
                    # 2
                    for j in range(3):
                        if rest_of_A[j] > 3:
                            continue

                        else:
                            # 2X

                            res += str(rest_of_A[j])
                            res += ":"

                            rest_of_A = rest_of_A[:j] + rest_of_A[j + 1:]

                            if rest_of_A[0] >= 6 and rest_of_A[1] >= 6:
                                # return "" #TODO:
                                res = ""
                                break

                            elif rest_of_A[0] >= 6:
                                return res + str(rest_of_A[1]) + str(rest_of_A[0])

                            else:
                                return res + str(rest_of_A[0]) + str(rest_of_A[1])

                else:  #
                    # 1
                    # 0
                    res += str(rest_of_A[0])
                    res += ":"

                    rest_of_A = rest_of_A[1:]

                    if rest_of_A[0] >= 6 and rest_of_A[1] >= 6:
                        # return "" #TODO
                        res = ""
                        continue

                    elif rest_of_A[0] >= 6:
                        return res + str(rest_of_A[1]) + str(rest_of_A[0])

                    else:
                        return res + str(rest_of_A[0]) + str(rest_of_A[1])

        return ""


