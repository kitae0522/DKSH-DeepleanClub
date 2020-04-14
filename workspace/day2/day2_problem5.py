'''
FileName : day2_problem5.py
Coder : Song Ki Tae
'''

def toUpper(words):
    Upper_alphabet = {"a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F", "g":"G", "h":"H", "i":"I",
                      "j":"J", "k":"K", "l":"L", "m":"M", "n":"N", "o":"O", "p":"P", "q":"Q", "r":"R",
                      "s":"S","t":"T", "u":"U", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z"}
    Lower_alphabet = {"A":"a", "B":"b", "C":"c", "D":"d", "E":"e", "F":"f", "G":"g", "H":"h", "I":"i",
                      "J":"j", "K":"k", "L":"l", "M":"m", "N":"n", "O":"o", "P":"p", "Q":"q", "R":"r",
                      "S":"s","T":"t", "U":"u", "V":"v", "W":"w", "X":"x", "Y":"y", "Z":"z"}
    list_word = list(words)
    for x in range(len(list_word)-1):
        if list_word[x] == " ":
            del list_word[x]
    for y in range(len(list_word)):
        if list_word[y] not in Lower_alphabet:
            list_word[y] = Upper_alphabet[list_word[y]]
            res = "".join(list_word)
    return res


def toLower(words):
    Upper_alphabet = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I",
                      "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R",
                      "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}
    Lower_alphabet = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i",
                      "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
                      "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}
    list_word = list(words)
    for x in range(len(list_word)-1):
        if list_word[x] == " ":
            del list_word[x]
    for y in range(len(list_word)):
        if list_word[y] not in Upper_alphabet:
            list_word[y] = Lower_alphabet[list_word[y]]
            res = "".join(list_word)
    return res


if __name__ == '__main__':

    word = "Iron Man"
    print(toUpper(word))
    # print(toLower(word))
