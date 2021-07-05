import PySimpleGUI as sg

def aiken(correct, path,filename):
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
    textfile = open(filename, "w", encoding='utf-8')
    for j in range(len(correct)):
        textfile.write(questions[j] + "\n"
                       + answers_a[j]
                       + answers_b[j]
                       + answers_c[j]
                       + answers_d[j]
                       + answers_e[j]
                       + "ANSWER: " + correct[j] + "\n" + "\n")
    textfile.close()

    print(questions)
    print(answers_a)
    print(answers_b)
    print(answers_c)
    print(answers_d)
    print(answers_e)
    print("Succes")

def gift(correct, path,filename):
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
                answers_a[y] = "%19.99999%" + answers_a[y]
            elif (correct[y][0] == "B"):
                answers_b[y] = "%19.99999%" + answers_b[y]
            elif (correct[y][0] == "C"):
                answers_c[y] = "%19.99999%" + answers_c[y]
            elif (correct[y][0] == "D"):
                answers_d[y] = "%19.99999%" + answers_d[y]
            elif (correct[y][0] == "E"):
                answers_e[y] = "%19.99999%" + answers_e[y]

            if (correct[y][1] == "A"):
                answers_a[y] = "%19.99999%" + answers_a[y]
            elif (correct[y][1] == "B"):
                answers_b[y] = "%19.99999%" + answers_b[y]
            elif (correct[y][1] == "C"):
                answers_c[y] = "%19.99999%" + answers_c[y]
            elif (correct[y][1] == "D"):
                answers_d[y] = "%19.99999%" + answers_d[y]
            elif (correct[y][1] == "E"):
                answers_e[y] = "%19.99999%" + answers_e[y]

            if (correct[y][2] == "A"):
                answers_a[y] = "%19.99999%" + answers_a[y]
            elif (correct[y][2] == "B"):
                answers_b[y] = "%19.99999%" + answers_b[y]
            elif (correct[y][2] == "C"):
                answers_c[y] = "%19.99999%" + answers_c[y]
            elif (correct[y][2] == "D"):
                answers_d[y] = "%19.99999%" + answers_d[y]
            elif (correct[y][2] == "E"):
                answers_e[y] = "%19.99999%" + answers_e[y]

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
    textfile = open(filename, "w", encoding='utf-8')
    for j in range(len(questions)):
        textfile.write(questions[j] + "{" + "\n"
                       + "~" + answers_a[j]
                       + "~" + answers_b[j]
                       + "~" + answers_c[j]
                       + "~" + answers_d[j]
                       + "~" + answers_e[j] + "}" + "\n" + "\n")
    textfile.close()

    print(questions)
    print(answers_a)
    print(answers_b)
    print(answers_c)
    print(answers_d)
    print(answers_e)
    print("Succes")

def gui():
    filename = sg.popup_get_file('Enter the file you wish to process')




    layout = [[
              sg.Titlebar("MedAcces Custom Software")],
              [sg.Text("Ce format doresti fisierul final ? (Aiken sau Gift)")],
              [sg.Input()],
              [sg.Text("Introdu numele fisierul nou: ")],
              [sg.Input()],
              [sg.Text("Introdu raspunsurile corecte pe rand, cu virgula intre ele: ")],
              [sg.Text("ex: A,B,C,DE,ABC")],
              [sg.Input()],
              [sg.Button('Procesare')]
    ]

    # Create the window
    window = sg.Window('Window Title', layout)  # Part 3 - Window Defintion

    # Display and interact with the Window
    event, values = window.read()  # Part 4 - Event loop or Window.read call


    return filename,values
    # Finish up by removing from the screen
    window.close()  # Part 5 - Close the Window

if __name__ == '__main__':

    info = gui()
    path = info[0]
    results = info[1][2]
    results = results.split(',')
    filename = info[1][1] +".txt"



    if info[1][0] == "Aiken":
        aiken(results,path,filename)
        print("Aikne")
    elif info[1][0] == "Gift":
        print("Gift")
        gift(results,path,filename)


