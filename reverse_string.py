def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """ 

    phrase_list = list(phrase)
    reversed = phrase_list[len(phrase_list)-1: 0: -1] 
    reversed.insert(len(reversed), phrase[0])
    return ''.join(reversed)