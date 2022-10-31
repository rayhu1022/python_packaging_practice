def cipher(text, shift, encrypt=True):
    """Encrypt or decrypt a string

    Given a string, this function either encrypt it or decrypt it by shifting each letter a fixed number of positions down the 
    alphabet. Numbers, symbols, and spaces are not affected. 

    Parameters
    ----------
    text : string
         A string that can either be a single word or a sentence.
    shift : integer != 0
         An integer that determines the number of positions each letter should be shifted
    encrypt : bool, default=True
         When the value is True, the function encrypts, otherwise it decrypts

    Returns
    -------
    string
        The new string, either encrypted or decrypted

    Examples
    --------
    >>> cipher('test', 2)
    'vguv'

    >>> cipher('vguv', 2, encrypt=False)
    'test'

    """
    assert isinstance(shift, int), f"shift must be an integer but shift = {shift}"
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text