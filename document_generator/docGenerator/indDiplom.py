from docxtpl import DocxTemplate
def indtask1():
    doc = DocxTemplate("templates/indPd1.docx")

    tags = {'yearF': "2k16",
            'yearT': "2k17",
            'profil': "PROGRAMINJENER",
            'entityName': "ENTITYNAME",
            'studFio': "FIO",
            'studCours': "COURS",
            'dateF': "DATEFROM",
            'dateT': "DATETO",
            'tutorKfuFio': "TUTORKFUFIO",
            'task1': "TASK1",
            'dateF1': "DATEFROM1",
            'dateT1': "DATETO1",
            'tutorKfuStatus': "TUTORKFUSTATUS",
            'tutorEntityStatus': "TUTORENTITYSTATUS"}
    doc.render(tags)
    doc.save('prepairDocx/Индивидуальное задание преддиплом1.docx')
def indtask2():
    doc = DocxTemplate("templates/indPd2.docx")

    tags = {'yearF': "2k16",
            'yearT': "2k17",
            'profil': "PROGRAMINJENER",
            'entityName': "ENTITYNAME",
            'studFio': "FIO",
            'studCours': "COURS",
            'dateF': "DATEFROM",
            'dateT': "DATETO",
            'tutorKfuFio': "TUTORKFUFIO",
            'task1': "TASK1",
            'task2': "TASK2",
            'dateF1': "DATEFROM1",
            'dateF2': "DATEFROM2",
            'dateT1': "DATETO1",
            'dateT2': "DATETO2",
            'tutorKfuStatus': "TUTORKFUSTATUS",
            'tutorEntityStatus': "TUTORENTITYSTATUS"}
    doc.render(tags)
    doc.save('prepairDocx/Индивидуальное задание преддиплом2.docx')
def indtask3():
    doc = DocxTemplate("templates/indPd3.docx")

    tags = {'yearF': "2k16",
            'yearT': "2k17",
            'profil': "PROGRAMINJENER",
            'entityName': "ENTITYNAME",
            'studFio': "FIO",
            'studCours': "COURS",
            'dateF': "DATEFROM",
            'dateT': "DATETO",
            'tutorKfuFio': "TUTORKFUFIO",
            'task1': "TASK1",
            'task2': "TASK2",
            'task3': "TASK3",
            'dateF1': "DATEFROM1",
            'dateF2': "DATEFROM2",
            'dateF3': "DATEFROM3",
            'dateT1': "DATETO1",
            'dateT2': "DATETO2",
            'dateT3': "DATETO3",
            'tutorKfuStatus': "TUTORKFUSTATUS",
            'tutorEntityStatus': "TUTORENTITYSTATUS"}
    doc.render(tags)
    doc.save('prepairDocx/Индивидуальное задание преддиплом3.docx')
def indtask4():
    doc = DocxTemplate("templates/indPd4.docx")

    tags = {'yearF': "2k16",
            'yearT': "2k17",
            'profil': "PROGRAMINJENER",
            'entityName': "ENTITYNAME",
            'studFio': "FIO",
            'studCours': "COURS",
            'dateF': "DATEFROM",
            'dateT': "DATETO",
            'tutorKfuFio': "TUTORKFUFIO",
            'task1': "TASK1",
            'task2': "TASK2",
            'task3': "TASK3",
            'task4': "TASK4",
            'dateF1': "DATEFROM1",
            'dateF2': "DATEFROM2",
            'dateF3': "DATEFROM3",
            'dateF4': "DATEFROM4",
            'dateT1': "DATETO1",
            'dateT2': "DATETO2",
            'dateT3': "DATETO3",
            'dateT4': "DATETO4",
            'tutorKfuStatus': "TUTORKFUSTATUS",
            'tutorEntityStatus': "TUTORENTITYSTATUS"}
    doc.render(tags)
    doc.save('prepairDocx/Индивидуальное задание преддиплом4.docx')
def indtask5():
    doc = DocxTemplate("templates/indPd5.docx")

    tags = {'yearF': "2k16",
            'yearT': "2k17",
            'profil': "PROGRAMINJENER",
            'entityName': "ENTITYNAME",
            'studFio': "FIO",
            'studCours': "COURS",
            'dateF': "DATEFROM",
            'dateT': "DATETO",
            'tutorKfuFio': "TUTORKFUFIO",
            'task1': "TASK1",
            'task2': "TASK2",
            'task3': "TASK3",
            'task4': "TASK4",
            'task5': "TASK5",
            'dateF1': "DATEFROM1",
            'dateF2': "DATEFROM2",
            'dateF3': "DATEFROM3",
            'dateF4': "DATEFROM4",
            'dateF5': "DATEFROM5",
            'dateT1': "DATETO1",
            'dateT2': "DATETO2",
            'dateT3': "DATETO3",
            'dateT4': "DATETO4",
            'dateT5': "DATETO5",
            'tutorKfuStatus': "TUTORKFUSTATUS",
            'tutorEntityStatus': "TUTORENTITYSTATUS"}
    doc.render(tags)
    doc.save('prepairDocx/Индивидуальное задание преддиплом5.docx')

    # FOR TEST
def t(kolvo):
        if int(kolvo) == 5:
                indtask5()
        else:
                if int(kolvo) == 4:
                        indtask4()
                else:
                        if int(kolvo) == 3:
                                indtask3()
                        else:
                                if int(kolvo) == 2:
                                        indtask2()
                                else:
                                        if int(kolvo) == 1:
                                                indtask1()
for i in range(6):
        t(i)