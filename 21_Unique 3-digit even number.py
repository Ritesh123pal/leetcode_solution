# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or i==k:
                      continue
                    if digits[i]==0:
                        continue
                    if digits[k]%2!=0:
                        continue
                    num=digits[i]*100+digits[j]*10+digits[k]
                    ans.add(num)
        return len(ans)                
                                
 