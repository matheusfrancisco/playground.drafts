def minimumSum(self, num: int) -> int:
    num=sorted(str(num))
    a1= num[0]+num[3]
    a2=num[1]+num[2]
    return int(a1)+int(a2)
       
