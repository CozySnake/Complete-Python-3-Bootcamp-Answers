import string

# Here I check if this text is a pangram.
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '')
    print(len(str1))
    for letter in alphabet:
        if letter in str1.lower():
            alphabet = alphabet.replace(letter, '')
            print(alphabet)
    if len(alphabet) == 0:
        print('The string is a pangram.')
    else:
        print('The string is not a pangram.')

string.ascii_lowercase

ispangram("The quick brown fox jumps over he lazy dog")



def up_low(s):
    d = {'upper': 0, 'lower': 0}
    for letter in s:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d['lower'] += 1
        else:
            pass
    print('Original String : ' + s)
    print(f'No. of Upper case characters : {d["upper"]}')
    print(f'No. of Lower case Characters : {d["lower"]}')
    print(d['upper'], d['lower'])

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)