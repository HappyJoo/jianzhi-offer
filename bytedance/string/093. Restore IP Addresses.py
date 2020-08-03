# BF
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
		# 判读是否满足ip的条件
        def helper(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True
		# 三个循环,把数字分成四份
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        # print(tmp1, tmp2, tmp3, tmp4)

                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res


# backtrack
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3): # check the next 3 bit at most
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res
        

# backtrack 2
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []
        def restore(count=0, ip='', s=''): # count record split times, ip record ip, s record remaining string
            if count == 4:
                if s == '':
                    r.append(ip[:-1])
                return
            if len(s) > 0:
                restore(count+1, ip+s[0]+'.', s[1:])
            if len(s) > 1 and s[0] != '0':
                restore(count+1, ip+s[:2]+'.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                restore(count+1, ip+s[:3]+'.', s[3:])
        restore(0, '', s)
        return r
