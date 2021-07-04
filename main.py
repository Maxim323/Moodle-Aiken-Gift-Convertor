import docx
import docx2txt
import io
# img_viewer.py

import PySimpleGUI as sg
import os.path


# inca neimplentata
def info():
    print('- Aiken - press 0')
    print('- GIFT - press 1')
    format = input('Ce format vrei sa folosesti ? ')
    print(format)

    print('\n')
    print(r"ex: C:/Users/a1/Desktop/Poze absilvire/Radiologie.docx")
    path = input('Introdu calea fisierului inlocuind \ cu /: ')
    print(path)


def aiken(correct, path):
    questions = []
    answers_a = []
    answers_b = []
    answers_c = []
    answers_d = []
    answers_e = []
    temp = []

    with open(path, encoding="utf8") as f:
        content = f.readline()
        while content:
            content = f.readline()
            temp.append(content)

    for i in range(len(temp)):
        if (temp[i].startswith("a.") or temp[i].startswith("b.") or temp[i].startswith("c.") or temp[i].startswith(
                "d.") or temp[i].startswith("e.") or temp[i] != 0):
            if (temp[i].startswith("a.")):
                answers_a.append(temp[i])
            elif (temp[i].startswith("b.")):
                answers_b.append(temp[i])
            elif (temp[i].startswith("c.")):
                answers_c.append(temp[i])
            elif (temp[i].startswith("d.")):
                answers_d.append(temp[i])
            elif (temp[i].startswith("e.")):
                answers_e.append(temp[i])
            else:
                questions.append(temp[i])

    # stergere caracter \n, dupa stergerea locatiilor goale
    questions = [s.replace("\n", "") for s in questions]
    questions = [x for x in questions if x != []]
    questions = [x for x in questions if x]

    # stergere numerotare intrebari + spatiile de dupa
    for n in range(len(questions)):
        if n < 10:
            questions[n] = questions[n][3:]
        else:
            questions[n] = questions[n][4:]
        # verificare daca au mai ramas spatii (double space check)
        if (questions[n][0].isspace()):
            questions[n] = questions[n][1:]

    # inlocuirea a,b,c,d cu A.,B., etc..pentru formatul AIKEN
    answers_a = [s.replace("a.", "A.") for s in answers_a]
    answers_b = [s.replace("b.", "B.") for s in answers_b]
    answers_c = [s.replace("c.", "C.") for s in answers_c]
    answers_d = [s.replace("d.", "D.") for s in answers_d]
    answers_e = [s.replace("e.", "E.") for s in answers_e]

    # scrierea in fisier
    textfile = open("firstdemo.txt", "w", encoding='utf-8')
    for j in range(len(questions)):
        textfile.write(questions[j] + "\n"
                       + answers_a[j]
                       + answers_b[j]
                       + answers_c[j]
                       + answers_d[j]
                       + answers_e[j]
                       + "ANSWER: " + correct[j] + "\n" + "\n")
    textfile.close()


def gift(correct, path):
    questions = []
    answers_a = []
    answers_b = []
    answers_c = []
    answers_d = []
    answers_e = []
    temp = []

    with open(path, encoding="utf8") as f:
        content = f.readline()
        while content:
            content = f.readline()
            temp.append(content)

    for i in range(len(temp)):
        if (temp[i].startswith("a.") or temp[i].startswith("b.") or temp[i].startswith("c.") or temp[i].startswith(
                "d.") or temp[i].startswith("e.") or temp[i] != 0):
            if (temp[i].startswith("a.")):
                answers_a.append(temp[i])
            elif (temp[i].startswith("b.")):
                answers_b.append(temp[i])
            elif (temp[i].startswith("c.")):
                answers_c.append(temp[i])
            elif (temp[i].startswith("d.")):
                answers_d.append(temp[i])
            elif (temp[i].startswith("e.")):
                answers_e.append(temp[i])
            else:
                questions.append(temp[i])

        # stergere caracter \n, dupa stergerea locatiilor goale
    questions = [s.replace("\n", "") for s in questions]
    questions = [x for x in questions if x != []]
    questions = [x for x in questions if x]

    # stergere numerotare intrebari + spatiile de dupa
    for n in range(len(questions)):
        if n < 10:
            questions[n] = questions[n][3:]
        else:
            questions[n] = questions[n][4:]
        # verificare daca au mai ramas spatii (double space check)
        if (questions[n][0].isspace()):
            questions[n] = questions[n][1:]

    # stergere a,b,c,d
    answers_a = [s.replace("a.", "") for s in answers_a]
    answers_b = [s.replace("b.", "") for s in answers_b]
    answers_c = [s.replace("c.", "") for s in answers_c]
    answers_d = [s.replace("d.", "") for s in answers_d]
    answers_e = [s.replace("e.", "") for s in answers_e]

    # stergere spatiu ramas la raspunsuri
    for n in range(len(questions)):
        answers_a[n] = answers_a[n][1:]
        answers_b[n] = answers_b[n][1:]
        answers_c[n] = answers_c[n][1:]
        answers_d[n] = answers_d[n][1:]
        answers_e[n] = answers_e[n][1:]

    for y in range(len(correct)):
        if (len(correct[y])) == 1:
            if (correct[y][0] == "A"):
                answers_a[y] = "%99.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%99.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%99.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%99.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%99.99999%" + answers_e[y]

        if (len(correct[y])) == 2:
            if (correct[y][0] == "A"):
                answers_a[y] = "%49.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%49.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%49.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%49.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%49.99999%" + answers_e[y]

            if (correct[y][1] == "A"):
                answers_a[y] = "%49.99999%" + answers_a[y]
            elif (correct[y][1] == "B"):
                answers_b[y] = "%49.99999%" + answers_b[y]
            elif (correct[y][1] == "C"):
                answers_c[y] = "%49.99999%" + answers_c[y]
            elif (correct[y][1] == "D"):
                answers_d[y] = "%49.99999%" + answers_d[y]
            elif (correct[y][1] == "E"):
                answers_e[y] = "%49.99999%" + answers_e[y]

        if (len(correct[y])) == 3:
            if (correct[y][0] == "A"):
                answers_a[y] = "%33.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%33.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%33.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%33.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%33.99999%" + answers_e[y]

            if (correct[y][1] == "A"):
                answers_a[y] = "%33.99999%" + answers_a[y]
            elif (correct[y][1] == "B"):
                answers_b[y] = "%33.99999%" + answers_b[y]
            elif (correct[y][1] == "C"):
                answers_c[y] = "%33.99999%" + answers_c[y]
            elif (correct[y][1] == "D"):
                answers_d[y] = "%33.99999%" + answers_d[y]
            elif (correct[y][1] == "E"):
                answers_e[y] = "%33.99999%" + answers_e[y]

            if (correct[y][2] == "A"):
                answers_a[y] = "%33.99999%" + answers_a[y]
            elif (correct[y][2] == "B"):
                answers_b[y] = "%33.99999%" + answers_b[y]
            elif (correct[y][2] == "C"):
                answers_c[y] = "%33.99999%" + answers_c[y]
            elif (correct[y][2] == "D"):
                answers_d[y] = "%33.99999%" + answers_d[y]
            elif (correct[y][2] == "E"):
                answers_e[y] = "%33.99999%" + answers_e[y]

        if (len(correct[y])) == 4:
            if (correct[y][0] == "A"):
                answers_a[y] = "%24.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%24.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%24.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%24.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%24.99999%" + answers_e[y]

            if (correct[y][1] == "A"):
                answers_a[y] = "%24.99999%" + answers_a[y]
            elif (correct[y][1] == "B"):
                answers_b[y] = "%24.99999%" + answers_b[y]
            elif (correct[y][1] == "C"):
                answers_c[y] = "%24.99999%" + answers_c[y]
            elif (correct[y][1] == "D"):
                answers_d[y] = "%24.99999%" + answers_d[y]
            elif (correct[y][1] == "E"):
                answers_e[y] = "%24.99999%" + answers_e[y]

            if (correct[y][2] == "A"):
                answers_a[y] = "%24.99999%" + answers_a[y]
            elif (correct[y][2] == "B"):
                answers_b[y] = "%24.99999%" + answers_b[y]
            elif (correct[y][2] == "C"):
                answers_c[y] = "%24.99999%" + answers_c[y]
            elif (correct[y][2] == "D"):
                answers_d[y] = "%24.99999%" + answers_d[y]
            elif (correct[y][2] == "E"):
                answers_e[y] = "%24.99999%" + answers_e[y]

            if (correct[y][3] == "A"):
                answers_a[y] = "%24.99999%" + answers_a[y]
            elif (correct[y][3] == "B"):
                answers_b[y] = "%24.99999%" + answers_b[y]
            elif (correct[y][3] == "C"):
                answers_c[y] = "%24.99999%" + answers_c[y]
            elif (correct[y][3] == "D"):
                answers_d[y] = "%24.99999%" + answers_d[y]
            elif (correct[y][3] == "E"):
                answers_e[y] = "%24.99999%" + answers_e[y]

        if (len(correct[y])) == 5:
            if (correct[y][0] == "A"):
                answers_a[y] = "%9.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%9.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%9.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%9.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%9.99999%" + answers_e[y]

            if (correct[y][1] == "A"):
                answers_a[y] = "%9.99999%" + answers_a[y]
            elif (correct[y][1] == "B"):
                answers_b[y] = "%9.99999%" + answers_b[y]
            elif (correct[y][1] == "C"):
                answers_c[y] = "%9.99999%" + answers_c[y]
            elif (correct[y][1] == "D"):
                answers_d[y] = "%9.99999%" + answers_d[y]
            elif (correct[y][1] == "E"):
                answers_e[y] = "%9.99999%" + answers_e[y]

            if (correct[y][2] == "A"):
                answers_a[y] = "%9.99999%" + answers_a[y]
            elif (correct[y][2] == "B"):
                answers_b[y] = "%9.99999%" + answers_b[y]
            elif (correct[y][2] == "C"):
                answers_c[y] = "%9.99999%" + answers_c[y]
            elif (correct[y][2] == "D"):
                answers_d[y] = "%9.99999%" + answers_d[y]
            elif (correct[y][2] == "E"):
                answers_e[y] = "%9.99999%" + answers_e[y]

            if (correct[y][3] == "A"):
                answers_a[y] = "%9.99999%" + answers_a[y]
            elif (correct[y][3] == "B"):
                answers_b[y] = "%9.99999%" + answers_b[y]
            elif (correct[y][3] == "C"):
                answers_c[y] = "%9.99999%" + answers_c[y]
            elif (correct[y][3] == "D"):
                answers_d[y] = "%9.99999%" + answers_d[y]
            elif (correct[y][3] == "E"):
                answers_e[y] = "%9.99999%" + answers_e[y]

            if (correct[y][4] == "A"):
                answers_a[y] = "%9.99999%" + answers_a[y]
            elif (correct[y][4] == "B"):
                answers_b[y] = "%9.99999%" + answers_b[y]
            elif (correct[y][4] == "C"):
                answers_c[y] = "%9.99999%" + answers_c[y]
            elif (correct[y][4] == "D"):
                answers_d[y] = "%9.99999%" + answers_d[y]
            elif (correct[y][4] == "E"):
                answers_e[y] = "%9.99999%" + answers_e[y]

    # scrierea in fisier
    textfile = open("seconddemo.txt", "w", encoding='utf-8')
    for j in range(len(questions)):
        textfile.write(questions[j] + "{" + "\n"
                       + "~" + answers_a[j]
                       + "~" + answers_b[j]
                       + "~" + answers_c[j]
                       + "~" + answers_d[j]
                       + "~" + answers_e[j] + "}" + "\n" + "\n")
    textfile.close()

    print(answers_a)
    print(answers_b)
    print(answers_c)
    print(answers_d)
    print(answers_e)


if __name__ == '__main__':
    answers_gift = ['A', 'AB', 'ABC', 'ABCD', 'ABCDE', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                    'A',
                    'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

    answers_aiken = ['A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                     'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'
        , 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

    path = 'C:/Users/a1/PycharmProjects/MedAceesAutomation/test.txt'

    # raspunsuri corecte, path`ul fisierului sursa

    gift(answers_gift, path)
    aiken(answers_aiken, path)
