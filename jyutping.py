# This module defines a function in Python that parses a Cantonese syllable transcribed in Jyutping,
# the Cantonese romanization scheme devised by the Linguistic Society of Hong Kong
# (http://www.lshk.org).
#
# Jackson L. Lee
# jsllee.phon@gmail.com
#
# code downloaded here:
# https://github.com/JacksonLLee/parse-jyutping
#



def jyutping(jp):
    """
    parses the Cantonese romanization string jp and
    outputs a 4-tuple as (onset, nucleus, coda, tone), all elements as strings

    >>> jyutping('m4')
    ('', 'm', '', '4')

    >>> jyutping('ng4')
    ('', 'ng', '', '4')

    >>> jyutping('jit6')
    ('j', 'i', 't', '6')

    >>> jyutping('uk1')
    ('', 'u', 'k', '1')

    >>> jyutping('aa3')
    ('', 'aa', '', '3')

    >>> jyutping('aak1')
    ('', 'aa', 'k', '1')

    >>> jyutping('i1')
    ('', 'i', '', '1')

    >>> jyutping('wu4')
    ('w', 'u', '', '4')

    >>> jyutping('saa2')
    ('s', 'aa', '', '2')

    >>> jyutping('saan2')
    ('s', 'aa', 'n', '2')

    >>> jyutping('saang1')
    ('s', 'aa', 'ng', '1')

    >>> jyutping('sung3')
    ('s', 'u', 'ng', '3')

    >>> jyutping('sau2')
    ('s', 'a', 'u', '2')

    >>> jyutping('saau2')
    ('s', 'aa', 'u', '2')

    >>> jyutping('gui6')
    ('g', 'u', 'i', '6')

    >>> jyutping('jyut6')
    ('j', 'yu', 't', '6')

    >>> jyutping(123)
    Traceback (most recent call last):
    JyutpingError: 'argument needs to be a string -- 123'

    >>> jyutping('jit')
    Traceback (most recent call last):
    JyutpingError: "tone error -- 'jit'"

    >>> jyutping('jit7')
    Traceback (most recent call last):
    JyutpingError: "tone error -- 'jit7'"

    >>> jyutping('jix6')
    Traceback (most recent call last):
    JyutpingError: "coda error -- 'jix6'"

    >>> jyutping('jxt6')
    Traceback (most recent call last):
    JyutpingError: "nucleus error -- 'jxt6'"

    >>> jyutping('fjit6')
    Traceback (most recent call last):
    JyutpingError: "onset error -- 'fjit6'"

    """

    class JyutpingError(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return repr(self.msg)

    ## check jp as a valid argument string

    if type(jp) is not str:
        raise JyutpingError('argument needs to be a string -- ' + repr(jp))

    jp = jp.lower()

    if len(jp) < 2:
        raise JyutpingError('argument string needs to contain at least 2 characters -- ' + repr(jp))

    ## tone

    if (not jp[-1].isdigit()) or (jp[-1] not in '123456'):
        raise JyutpingError('tone error -- ' + repr(jp))

    tone = jp[-1]
    cvc = jp[:-1]

    ## coda

    if not (cvc[-1] in 'ieaouptkmng'):
        raise JyutpingError('coda error -- ' + repr(jp))

    if cvc in ['m', 'ng', 'i', 'e', 'aa', 'o', 'u']:
        return ('', cvc, '', tone)
    elif cvc[-2:] == 'ng':
        coda = 'ng'
        cv = cvc[:-2]
    elif (cvc[-1] in 'ptkmn') or ((cvc[-1] == 'i') and (cvc[-2] in 'eaou')) or \
                                 ((cvc[-1] == 'u') and (cvc[-2] in 'ieao')):
        coda = cvc[-1]
        cv = cvc[:-1]
    else:
        coda = ''
        cv = cvc

    # nucleus, and then onset

    nucleus = ''

    while cv[-1] in 'ieaouy':
        nucleus = cv[-1] + nucleus
        cv = cv[:-1]
        if not cv:
            break

    if not nucleus:
        raise JyutpingError('nucleus error -- ' + repr(jp))

    onset = cv

    onsetList = ['b', 'd', 'g', 'gw', 'z', 'p', 't', 'k', 'kw', 'c', 'm', 'n', 'ng', 'f', 'h', 's',
                 'l', 'w', 'j', '']

    if onset not in onsetList:
        raise JyutpingError('onset error -- ' + repr(jp))

    return (onset, nucleus, coda, tone)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
