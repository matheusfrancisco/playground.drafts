def isPalindrome(self, x: int) -> bool:
    list_x = [i for i in str(x)]
    list_y = list_x[::-1]
    return list_x == list_y
        
