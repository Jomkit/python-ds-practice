def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    j = 0
    vowel = [0] * len(s)    #vowel list for storing vowels
    s = list(s)

    #storing the vowels separately
    for i in range(len(s)):
        if s[i] in 'AEIOUaeiou':
            vowel[j] = s[i]
            j += 1

    #Placing the vowels in rev order in s
    for i in range(len(s)):
        if s[i] in 'AEIOUaeiou':
            j -= 1
            s[i] = vowel[j]
        
    return ''.join(s)