import PySimpleGUI as sg

def main():

    layout = [  [sg.Text('Calculadora de Porcentagem')],
                [sg.Text ("Número"), sg.Input(k='-IN1-'), sg.Text(size=(15,1), key='-OUT1-')],
                [sg.Text ("Quantos porcentos?"), sg.Input(k='-IN2-'), sg.Text(size=(15,1), key='-OUT2-')],
                [sg.Button('Calcular'), sg.Button('Grazie')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        #window['-OUT1-'].update(int(values['-IN1-'])+int(values['-IN2-']))
        c = int(values['-IN1-'])*float(values['-IN2-'])/100
        window['-OUT2-'].update( str(c) + "%")
    window.close()

def func():

    main()

func()
