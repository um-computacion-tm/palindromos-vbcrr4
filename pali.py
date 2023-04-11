def palindrome (phrase):
    phrase = phrase.lower()
    if phrase == phrase[::-1]:
        return True
    else:
        return False



'''def palindrome_rec (frase):
    if len(frase) <= 1:
        return True
    if frase [0] == frase [-1]:
        return palindrome_rec(frase[1:-2])'''
    


if __name__=='__main__':
    pass