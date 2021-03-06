class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        def cmp(ch1, ch2):
            return ord(ch1) - ord(ch2)

        begin = 0
        end = 0
        flag = False
        for i, ch in enumerate(str):
            print(ch, cmp(ch, '0'), cmp(ch, '9'))
            if not flag and ch == ' ':
                continue
            if ch == '-' or ch == '+':
                if not flag:
                    flag = True
                    begin = i
                    continue
                else:
                    end = i
                    break
            if cmp(ch, '0') >= 0 and cmp(ch, '9') <= 0:
                flag = True
            else:
                end = i
                break
        if end == 0:
            end = len(str)
        try:
            result = int(str[begin:end])
            if result > INT_MAX:
                return INT_MAX
            if result < INT_MIN:
                return INT_MIN
            return result
        except:Exception
        return 0
