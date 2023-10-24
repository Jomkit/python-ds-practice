def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.split(" ")
    lst_phrase = []
    for word in phrase:
        lst_phrase.append(word.capitalize())

    return ' '.join([word for word in lst_phrase])