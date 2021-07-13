'''
O(N) time
iterates through input only once. Although each iteration does have dict traversals, dict size is limited by 26.

O(1) space
maintains 2 dicts of up to size 26 only
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # two dicts used to maintain 1 to 1 mapping of 26 letters to 26 letters
        s_to_t_dict = {}
        t_to_s_dict = {}
        for i, c1 in enumerate(s):
            c2 = t[i]
            if c1 not in s_to_t_dict:
                # f(x)=y not stored
                if c2 in t_to_s_dict:
                    # f(z)=y so we can't add f(x)=y
                    return False
                else:
                    # make new rule f(x)=y g(y)=x
                    s_to_t_dict[c1] = c2
                    t_to_s_dict[c2] = c1
            elif s_to_t_dict[c1] == c2:
                # f(x)=y already stored
                continue
            elif s_to_t_dict[c1] != c2:
                # f(x)=z already stored
                return False
        return True
            