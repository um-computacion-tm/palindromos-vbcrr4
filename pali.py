def palindrome (phrase):
    phrase = phrase.lower()
    if phrase == phrase[::-1]:
        return True
    else:
        return False
    
if __name__=='__main__':
    pass