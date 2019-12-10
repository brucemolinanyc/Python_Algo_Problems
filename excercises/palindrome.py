def isPalindrome(string):
    return string[0:] == string[::-1]

	
print(isPalindrome("aabcdcbaa"))