# importam toata partea de backend (variablie, clase, functii, instante)
from Backend import *

# setari pentru aspectul general al programului
sg.set_options(font=('Courier', 12))
sg.theme('DarkGrey5')

# delimitarea elementelor layout-ului pe 3 coloane: stanga, centru, dreapta
stanga = [
    [sg.Push(), sg.Text('Orar\n\n', font=('Times New Roman', 20), text_color='navajo white'), sg.VPush()],
    [sg.Push(), sg.Text('Saptamana: ', font=('Courier', 16)), sg.Combo(['para', 'impara'], readonly=True,
                                                                       key='COMBO'), sg.VPush()],
    [sg.Push(), sg.Text(obiectOrar.ore, justification='center', key='textorar'), sg.Push()],
    [sg.VPush(), sg.Push(), sg.Button('Afiseaza'), sg.Push(), sg.VPush()]
]

centru = [
    [sg.Push(), sg.Text('Titlul lectiei:', ), sg.Input(obiectMultiline.titluLectie, size=30, key='numeLectieDeLaUser',
                                                       do_not_clear=False), sg.Push()],
    [sg.Multiline(obiectMultiline.TextLectie, key="txtLectie", size=(80, 30))],
    [sg.Button('Salveaza Lectia'), sg.Push(), sg.Button('Goleste')]
]

dreapta = [
    [sg.Push(), sg.Text('Lista lectii', font=('Times New Roman', 20), text_color='navajo white'), sg.Push()],
    [sg.Listbox(values=obiectListbox.fisiere, size=(25, 25), key='listaFisiere')],
    [sg.Button('Deschide', size=(10, 1), ), sg.Push(), sg.Button('Sterge', size=(10, 1))]
]

# constructia layout-ului
layout = [
    [sg.Push(), sg.Text('ORGANIZATOR', font=('Times New Roman', 20), text_color='navajo white'), sg.Push(),
     sg.Button('Exit')],
    [sg.Column(stanga), sg.Column(centru), sg.Column(dreapta)],
    [sg.Text('© Călin Andrei-Emil', font=('Times New Roman', 10), text_color='navajo white'), sg.Push()]
    ]

# Creeaza Window-ul. Finalize permite window-ului sa isi ia update.
window = sg.Window('Organizator', layout, size=(1500, 700), enable_close_attempted_event=True, finalize=True)

# Loop care tine window-ul deschis, il updateaza si pune conditia de inchidere
while True:
    event, values = window.read()

    if ((event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and
        sg.popup_ok_cancel("     Esti sigur ca vrei sa iesi?", " Asigura-te ca ai salvat totul inainte.",
                           title="Atentie!", keep_on_top=True) == 'OK'):
        break

    if values['COMBO'] == 'impara':
        ore = obiectOrar.afisareOrar_impar(window)
    elif values['COMBO'] == 'para':
        ore = obiectOrar.afisareOrar_par(window)

    if event == 'Afiseaza':
        window['textorar'].update()

    if event == 'Salveaza Lectia':
        obiectMultiline.functieSalvare(values, window)

    if event == 'Goleste':
        obiectMultiline.functieGolire(window)

    if event == 'Deschide':
        obiectListbox.deschidereFisier(values, window)

    if event == 'Sterge':
        obiectListbox.functieStergere(values, window)

# inchide window-ul
window.close()
