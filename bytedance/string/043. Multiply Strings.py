
#kidding
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))


# string
# using int and str just using python's property.
# just like using '1' - '0' and get 1 in C.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        total = l1 + l2
        result = [0] * total

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                sum = result[i + j + 1] + int(num1[i]) * int(num2[j])
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10
        
        index = 0
        while result[index] == 0 and index < total - 1:
            index += 1
        
        re = ""
        while index < total:
            re+=str(result[index])
            index += 1
        return re