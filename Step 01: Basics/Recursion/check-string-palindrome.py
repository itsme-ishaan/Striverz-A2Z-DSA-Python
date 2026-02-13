def checkPalindrome(str, i, j):
    if i >= j:
        return True
    
    if str[i] != str[j]:
        return False
    
    return checkPalindrome(str, i + 1, j - 1)




  
