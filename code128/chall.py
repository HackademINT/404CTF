from PIL import Image
import base64
import string
import random
from inputimeout import inputimeout, TimeoutOccurred
import io

CharSetB = {
                ' ':0, '!':1, '"':2, '#':3, '$':4, '%':5, '&':6, "'":7,
                '(':8, ')':9, '*':10, '+':11, ',':12, '-':13, '.':14, '/':15,
                '0':16, '1':17, '2':18, '3':19, '4':20, '5':21, '6':22, '7':23,
                '8':24, '9':25, ':':26, ';':27, '<':28, '=':29, '>':30, '?':31,
                '@':32, 'A':33, 'B':34, 'C':35, 'D':36, 'E':37, 'F':38, 'G':39,
                'H':40, 'I':41, 'J':42, 'K':43, 'L':44, 'M':45, 'N':46, 'O':47,
                'P':48, 'Q':49, 'R':50, 'S':51, 'T':52, 'U':53, 'V':54, 'W':55,
                'X':56, 'Y':57, 'Z':58, '[':59, '\\':60, ']':61, '^':62, '_':63,
                '' :64, 'a':65, 'b':66, 'c':67, 'd':68, 'e':69, 'f':70, 'g':71,
                'h':72, 'i':73, 'j':74, 'k':75, 'l':76, 'm':77, 'n':78, 'o':79,
                'p':80, 'q':81, 'r':82, 's':83, 't':84, 'u':85, 'v':86, 'w':87,
                'x':88, 'y':89, 'z':90, '{':91, '|':92, '}':93, '~':94, '\x7F':95,
                'FNC3':96, 'FNC2':97, 'SHIFT':98, 'Code C':99, 'FNC4':100, 'Code A':101, 'FNC1':102, 'START A':103,
                'START B':104, 'START C':105, 'STOP':106
           }

ValueEncodings = {  0:'11011001100',  1:'11001101100',  2:'11001100110',
        3:'10010011000',  4:'10010001100',  5:'10001001100',
        6:'10011001000',  7:'10011000100',  8:'10001100100',
        9:'11001001000', 10:'11001000100', 11:'11000100100',
        12:'10110011100', 13:'10011011100', 14:'10011001110',
        15:'10111001100', 16:'10011101100', 17:'10011100110',
        18:'11001110010', 19:'11001011100', 20:'11001001110',
        21:'11011100100', 22:'11001110100', 23:'11101101110',
        24:'11101001100', 25:'11100101100', 26:'11100100110',
        27:'11101100100', 28:'11100110100', 29:'11100110010',
        30:'11011011000', 31:'11011000110', 32:'11000110110',
        33:'10100011000', 34:'10001011000', 35:'10001000110',
        36:'10110001000', 37:'10001101000', 38:'10001100010',
        39:'11010001000', 40:'11000101000', 41:'11000100010',
        42:'10110111000', 43:'10110001110', 44:'10001101110',
        45:'10111011000', 46:'10111000110', 47:'10001110110',
        48:'11101110110', 49:'11010001110', 50:'11000101110',
        51:'11011101000', 52:'11011100010', 53:'11011101110',
        54:'11101011000', 55:'11101000110', 56:'11100010110',
        57:'11101101000', 58:'11101100010', 59:'11100011010',
        60:'11101111010', 61:'11001000010', 62:'11110001010',
        63:'10100110000', 64:'10100001100', 65:'10010110000',
        66:'10010000110', 67:'10000101100', 68:'10000100110',
        69:'10110010000', 70:'10110000100', 71:'10011010000',
        72:'10011000010', 73:'10000110100', 74:'10000110010',
        75:'11000010010', 76:'11001010000', 77:'11110111010',
        78:'11000010100', 79:'10001111010', 80:'10100111100',
        81:'10010111100', 82:'10010011110', 83:'10111100100',
        84:'10011110100', 85:'10011110010', 86:'11110100100',
        87:'11110010100', 88:'11110010010', 89:'11011011110',
        90:'11011110110', 91:'11110110110', 92:'10101111000',
        93:'10100011110', 94:'10001011110', 95:'10111101000',
        96:'10111100010', 97:'11110101000', 98:'11110100010',
        99:'10111011110',100:'10111101110',101:'11101011110',
        102:'11110101110',103:'11010000100',104:'11010010000',
        105:'11010011100',106:'11000111010'
    }

flag = "404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}"

alphabet = string.ascii_letters + string.digits

for nb_fois in range(128):
    # préparation de l'image
    answer = "".join([alphabet[random.randrange(len(alphabet))] for i in range(random.randrange(10, 40))])
    img = Image.new("RGB", (len(answer) * 11, 100), color="white")
    for c in range(len(answer)):
        for i in range(11):
            if ValueEncodings[CharSetB[answer[c]]][i] == "1":
                for j in range(100):
                    img.putpixel((c * 11 + i, j), (0, 0, 0))

    raw_data = io.BytesIO()
    img.save(raw_data, "PNG")
    data = base64.b64encode(raw_data.getvalue())

    # send challenge
    print(f"[{nb_fois}/128] Il paraît qu'il y a un mot de passe dans cette image... Peux-tu m'aider ? Vite vite vite !!!")
    print(data.decode())
    # l'utilisateur a une seconde pour répondre
    try:
        user_answer = inputimeout(prompt='>> ', timeout=5)
    except:
        print("Trop tard ! Je n'ai pas pu ouvrir la porte à temps, l'alarme retentit !")
        exit()
    # vérification de la réponse 
    if user_answer == answer:
        print("Ouf, merci ! C'est le bon code ! Je fonce vers la porte suivante !")
    else:
        print("Oh non ! C'est le mauvais mot de passe ! L'alarme retentit !")
        exit()

# si on est là, c'est qu'on a réussi les 128 codes
print("Oh merci merci merci ! Me voilà enfin libre ! Voilà un cadeau pour te remercier :")
print(flag)

