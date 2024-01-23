# importarea librariilor folosite in program
import json
from datetime import date
import calendar
import os
import PySimpleGUI as sg

# definirea claselor proiectului
class Orar:
    # constructorul care ofera valori default clasei la instantiere
    def __init__(self):
        self.ore = "Alege saptamana"
        self.dataAzi = date.today()
        self.numeZi = calendar.day_name[self.dataAzi.weekday()]

    # metodele clasei Orar
    def afisareOrar_par(self, window):
        with open('orar_par.json') as fisjson1:
            orar = json.load(fisjson1)
            ore = orar[self.numeZi]
            window['textorar'].update(ore)
            return ore

    def afisareOrar_impar(self, window):
        with open('orar_impar.json') as fisjson2:
            orar = json.load(fisjson2)
            ore = orar[self.numeZi]
            window['textorar'].update(ore)
            return ore


class Listbox:
    # constructorul care ofera valori default clasei la instantiere
    def __init__(self):
        self.dirCurent = os.path.dirname(os.path.abspath(__file__))
        self.fisiere = [f for f in os.listdir(self.dirCurent) if f.endswith('.txt')]

    # metodele clasei Listbox
    def functieStergere(self, values, window):
        if values['listaFisiere']:
            fisierSelectat = values['listaFisiere'][0]
            if sg.popup_ok_cancel(f'Esti sigur ca vrei sa stergi {fisierSelectat}?', title="Atentie!",
                                  keep_on_top=True) == 'OK':
                os.remove(os.path.join(self.dirCurent, fisierSelectat))
                sg.popup('Fisierul a fost sters!', keep_on_top=True)
                self.fisiere = [f for f in os.listdir(self.dirCurent) if f.endswith('.txt')]
                window['listaFisiere'].update(self.fisiere)

    def deschidereFisier(self, values, window):
        if values['listaFisiere']:
            fisierSelectat = values['listaFisiere'][0]
            with open(fisierSelectat, 'r') as lectie:
                self.TextLectie = lectie.read()
                self.titluLectie = fisierSelectat
                print(self.titluLectie)
                window['numeLectieDeLaUser'].update(self.titluLectie)
                window['txtLectie'].update(self.TextLectie)
                return self.titluLectie, self.TextLectie

class Multiline:
    # constructorul care ofera valori default clasei la instantiere
    def __init__(self, obiectListbox):
        self.obiectListbox = obiectListbox
        self.TextLectie = ("    Bine ai (re)venit la organizatorul tau!\n\n    Daca este prima data cand folosesti "
                           "aceasta aplicatie, ti-am pregatit o mica introducere insotita de un set de instructiuni de"
                           " utilizare.\n\n    Tot ce trebuie sa faci pentru a accesa aceasta introducere este sa mergi"
                           " la lista din dreapta, sa dai click pe fisierul Instructiuni.txt, iar mai apoi sa apesi "
                           "butonul Deschide.")
        self.titluLectie = ''

    # metodele clasei Multiline
    def functieGolire(self, window):
        self.TextLectie = ''
        window['txtLectie'].update(self.TextLectie)

    def functieSalvare(self, values, window):
        titlu = values['numeLectieDeLaUser']
        text = values['txtLectie']
        path = obiectListbox.dirCurent + os.sep + titlu
        os.path.abspath(path)
        print(path)
        if os.path.isfile(path) == False or (os.path.isfile(path) == True and
                                             sg.popup_ok_cancel('Exista deja un fisier cu acelasi nume.',
                                                                'Esti sigur ca vrei sa il suprascrii?',
                                                                title="Atentie!", keep_on_top=True) == 'OK'):
            print(titlu)
            if titlu == '':
                sg.popup('Fisierul trebuie sa aiba un nume!', keep_on_top=True)
            else:
                with open(titlu, 'w') as fisSel:
                    fisSel.write(text)
        obiectListbox.fisiere = [f for f in os.listdir(obiectListbox.dirCurent) if f.endswith('.txt')]
        window['listaFisiere'].update(obiectListbox.fisiere)

#instantierea claselor
obiectOrar = Orar()
obiectListbox = Listbox()
obiectMultiline = Multiline(Listbox())
