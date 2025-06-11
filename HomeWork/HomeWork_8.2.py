def is_palindrome(text):
    word_user = "".join(i.lower() for i in text if i.isalnum())
    return word_user == word_user[::-1]

     
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
print("ОК")