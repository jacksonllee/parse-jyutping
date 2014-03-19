#!usr/bin/python

# This is a function in Python that parses a Cantonese syllable transcribed in Jyutping.
# The Jyutping romanization scheme is devised by the Linguistic Society of Hong Kong:
# http://www.lshk.org
#
# Jackson L. Lee
# jsllee.phon@gmail.com
# 2014-03-18
#
# code downloaded here:
# https://github.com/JacksonLLee/parse-jyutping
#
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

    >>> jyutping(123)
    Traceback (most recent call last):
    JyutPingError: 'argument needs to be a string -- 123'

    >>> jyutping('jit')
    Traceback (most recent call last):
    JyutPingError: "tone error -- 'jit'"

    >>> jyutping('jit7')
    Traceback (most recent call last):
    JyutPingError: "tone error -- 'jit7'"

    >>> jyutping('jix6')
    Traceback (most recent call last):
    JyutPingError: "coda error -- 'jix6'"

    >>> jyutping('jxt6')
    Traceback (most recent call last):
    JyutPingError: "nucleus error -- 'jxt6'"

    >>> jyutping('fjit6')
    Traceback (most recent call last):
    JyutPingError: "onset error -- 'fjit6'"

    """

    class JyutPingError(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return repr(self.msg)

    ## check jp as a valid argument string

    if type(jp) is not str:
        raise JyutPingError('argument needs to be a string -- ' + repr(jp))

    jp = jp.lower()

    if len(jp) < 2:
        raise JyutPingError('argument string needs to contain at least 2 characters -- ' + repr(jp))

    ## tone

    if (not jp[-1].isdigit()) or (jp[-1] not in '123456'):
        raise JyutPingError('tone error -- ' + repr(jp))

    tone = jp[-1]
    cvc = jp[:-1]

    ## coda

    if not (cvc[-1] in 'ieaouptkmng'):
        raise JyutPingError('coda error -- ' + repr(jp))

    if cvc in ['m', 'ng', 'i', 'e', 'aa', 'o', 'u']:
        return ('', cvc, '', tone)
    elif cvc[-2:] == 'ng':
        coda = 'ng'
        cv = cvc[:-2]
    elif (cvc[-1] in 'ptkmn') or ((cvc[-1] in 'iu') and (cvc[-2] == 'a')):
        coda = cvc[-1]
        cv = cvc[:-1]
    else:
        coda = ''
        cv = cvc

    # nucleus, and then onset

    nucleus = ''

    while cv[-1] in 'ieaouy':
        nucleus = nucleus + cv[-1]
        cv = cv[:-1]
        if not cv:
            break

    if not nucleus:
        raise JyutPingError('nucleus error -- ' + repr(jp))

    onset = cv

    onsetList = ['b', 'd', 'g', 'gw', 'z', 'p', 't', 'k', 'kw', 'c', 'm', 'n', 'ng', 'f', 'h', 's',
                 'l', 'w', 'j', '']

    if onset not in onsetList:
        raise JyutPingError('onset error -- ' + repr(jp))

    return (onset, nucleus, coda, tone)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

