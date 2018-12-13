import  string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text=text.lower()
    text=text.replace(' ','')
    for char in string.punctuation:
       text= text.replace(char,'')

    return text== reverse(text)

something=input('Please input text')

while something!='exit':
    if(is_palindrome(something)):
        print("Yes, it is a palindrome")
    else:
        print("No, it isnot a palindrome")
    something=input('Please input text')
