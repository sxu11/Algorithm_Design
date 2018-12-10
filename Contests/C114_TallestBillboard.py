class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """

        my_dict = {0: 0}

        def put_into_dict(key, val):
            if not key in my_dict:
                my_dict[key] = val
            else:
                my_dict[key] = max(val, my_dict[key])

        for rod in rods:
            # diffs = my_dict.keys()
            for diff, y in my_dict.items():  # TODO: cannot use for diff in diffs! y cannot be changed inside loop.
                put_into_dict(rod + diff, y)

                if rod >= diff:
                    put_into_dict(rod - diff, y + diff)
                else:
                    put_into_dict(diff - rod, y + rod)

            # print rod, my_dict
        return my_dict[0]