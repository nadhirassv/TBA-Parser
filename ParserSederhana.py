import string

#input
kalimat = input('Masukkan Token : ')
input_string = kalimat.lower()+'#'

#initialization
listalphabet = list(string.ascii_lowercase)
listState = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', '38', '39', '40', '41', '42', '43', 'q44', 'q45']

tabelTransisi = {}

for state in listState:
    for alphabet in listalphabet:
        tabelTransisi[(state, alphabet)] = 'error'
    tabelTransisi[(state, '#')] = 'error'
    tabelTransisi[(state, ' ')] = 'error'

# space before input string
tabelTransisi['q0', ' '] = 'q0'

#update the transition table for the following token : paman
tabelTransisi[('q0', 'p')] = 'q1'
tabelTransisi[('q1', 'a')] = 'q2'
tabelTransisi[('q2', 'm')] = 'q3'
tabelTransisi[('q3', 'a')] = 'q4'
tabelTransisi[('q4', 'n')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : halaman
tabelTransisi[('q0', 'd')] = 'q17'
tabelTransisi[('q17', 'i')] = 'q38'
tabelTransisi[('q38', ' ')] = 'q39'
tabelTransisi[('q39', 'h')] = 'q5'
tabelTransisi[('q5', 'a')] = 'q6'
tabelTransisi[('q6', 'l')] = 'q7'
tabelTransisi[('q7', 'a')] = 'q8'
tabelTransisi[('q8', 'm')] = 'q3'
tabelTransisi[('q3', 'a')] = 'q4'
tabelTransisi[('q4', 'n')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : ketela
tabelTransisi[('q0', 'k')] = 'q9'
tabelTransisi[('q9', 'e')] = 'q10'
tabelTransisi[('q10', 't')] = 'q11'
tabelTransisi[('q11', 'e')] = 'q12'
tabelTransisi[('q12', 'l')] = 'q13'
tabelTransisi[('q13', 'a')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: baju
tabelTransisi[('q0', 'b')] = 'q14'
tabelTransisi[('q14', 'a')] = 'q15'
tabelTransisi[('q15', 'j')] = 'q16'
tabelTransisi[('q16', 'u')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: daun
tabelTransisi[('q0', 'd')] = 'q17'
tabelTransisi[('q17', 'a')] = 'q18'
tabelTransisi[('q18', 'u')] = 'q19'
tabelTransisi[('q19', 'n')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: bibi
tabelTransisi[('q0', 'b')] = 'q15'
tabelTransisi[('q15', 'i')] = 'q20'
tabelTransisi[('q20', 'b')] = 'q21'
tabelTransisi[('q21', 'i')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : memotong
tabelTransisi[('q0', 'm')] = 'q22'
tabelTransisi[('q22', 'e')] = 'q23'
tabelTransisi[('q23', 'm')] = 'q24'
tabelTransisi[('q24', 'o')] = 'q25'
tabelTransisi[('q25', 't')] = 'q26'
tabelTransisi[('q26', 'o')] = 'q27'
tabelTransisi[('q27', 'n')] = 'q28'
tabelTransisi[('q28', 'g')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : mencuci
tabelTransisi[('q0', 'm')] = 'q22'
tabelTransisi[('q22', 'e')] = 'q23'
tabelTransisi[('q23', 'n')] = 'q29'
tabelTransisi[('q29', 'y')] = 'q30'
tabelTransisi[('q30', 'u')] = 'q31'
tabelTransisi[('q31', 'c')] = 'q32'
tabelTransisi[('q32', 'i')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: memakan
tabelTransisi[('q0', 'm')] = 'q22'
tabelTransisi[('q22', 'e')] = 'q23'
tabelTransisi[('q23', 'm')] = 'q24'
tabelTransisi[('q24', 'a')] = 'q33'
tabelTransisi[('q33', 'k')] = 'q34'
tabelTransisi[('q34', 'a')] = 'q35'
tabelTransisi[('q35', 'n')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: menyapu
tabelTransisi[('q0', 'm')] = 'q22'
tabelTransisi[('q22', 'e')] = 'q23'
tabelTransisi[('q23', 'n')] = 'q29'
tabelTransisi[('q49', 'y')] = 'q30'
tabelTransisi[('q30', 'a')] = 'q36'
tabelTransisi[('q36', 'p')] = 'q37'
tabelTransisi[('q37', 'u')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: di kebun
tabelTransisi[('q0', 'd')] = 'q17'
tabelTransisi[('q17', 'i')] = 'q38'
tabelTransisi[('q38', ' ')] = 'q39'
tabelTransisi[('q39', 'k')] = 'q40'
tabelTransisi[('q40', 'e')] = 'q41'
tabelTransisi[('q41', 'b')] = 'q42'
tabelTransisi[('q42', 'u')] = 'q43'
tabelTransisi[('q43', 'n')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# transition for new token
tabelTransisi[('q45', 'p')] = 'q1'
tabelTransisi[('q45', 'h')] = 'q5'
tabelTransisi[('q45', 'k')] = 'q9'
tabelTransisi[('q45', 'b')] = 'q14'
tabelTransisi[('q45', 'd')] = 'q17'
tabelTransisi[('q45', 'm')] = 'q22'

# Lexical analysis
idx = 0
state = 'q0'
token = ''
tokens = []  # List to store valid tokens

while state != 'acc':
    char = input_string[idx]
    token += char
    state = tabelTransisi[(state, char)]
    if state == 'q44':
        tokens.append(token.strip())
        print('Token Saat Ini : ', token.strip(), ', valid')
        token = ''
    elif state == 'error':
        print('Error, input token tidak valid')
        break
    idx = idx + 1

# Conclusion
if state == 'acc':
    print('Semua token yang diinput : ', kalimat, ', valid')
    print('Tokens:', tokens)
else:
    print('Terdapat token yang tidak valid')

# Defining groups for S, P, O, and K
subyek = ['paman', 'bibi']  # Example subjects
predikat = ['memotong', 'mencuci', 'memakan', 'menyapu']  # Example predicates
objek = ['daun', 'baju', 'ketela']  # Example objects
keterangan = ['di halaman', 'di kebun']  # Example adverbs

def identify_token_group(token):
    if token in subyek:
        return 'S'
    elif token in predikat:
        return 'P'
    elif token in objek:
        return 'O'
    elif token in keterangan:
        return 'K'
    else:
        return 'Invalid'

# Identify the group for each token
token_groups = [identify_token_group(token) for token in tokens]
print('Token Groups:', token_groups)

# Parsing using Pushdown Automata
stack = []
valid = True

for group in token_groups:
    if group == 'S':
        if not stack:
            stack.append('S')
        else:
            valid = False
            break
    elif group == 'P':
        if stack and stack[-1] == 'S':
            stack.append('P')
        else:
            valid = False
            break
    elif group == 'O':
        if stack and stack[-1] == 'P':
            stack.append('O')
        else:
            valid = False
            break
    elif group == 'K':
        if stack and stack[-1] in ['P', 'O']:
            stack.append('K')
        else:
            valid = False
            break
    else:
        valid = False
        break

# Check for final valid state
if valid and stack in [['S', 'P'], ['S', 'P', 'O'], ['S', 'P', 'K'], ['S', 'P', 'O', 'K']]:
    print('Kalimat valid:', kalimat)
else:
    print('Kalimat tidak valid:', kalimat)

