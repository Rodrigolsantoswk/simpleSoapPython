from time import sleep

from zeep import Client
import PySimpleGUI as sg

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')


def Soma(n1, n2):
    return client.service.Add(n1, n2)


def Divisao(n1, n2):
    return client.service.Divide(n1, n2)


def Multiplicacao(n1, n2):
    return client.service.Multiply(n1, n2)


def Subtracao(n1, n2):
    return client.service.Subtract(n1, n2)


def layout0():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Please select operation')],
              [sg.Combo(['Sum', 'Mul', 'Div', 'Sub'], default_value='Sum', key='operation')],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    opt = []
    window = sg.Window('SOAP Sum: dneonline', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit(0)
            break
        opt = values
        print('You entered ', values)
        break
    return opt


def layout1():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Please insert data to sum')],
              [sg.Text('Enter num 1'), sg.InputText()],
              [sg.Text('Enter num 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    numbers = []
    windowsoma = sg.Window('SOAP Sum: dneonline', layout)
    while True:
        event, values = windowsoma.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        numbers = values
        print('You entered ', values)
        break
    windowsoma.close()
    return numbers


def layout2():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Please insert data to divide')],
              [sg.Text('Enter num 1'), sg.InputText()],
              [sg.Text('Enter num 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    numbers = []
    window = sg.Window('SOAP Div: dneonline', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        numbers = values
        print('You entered ', values)
        break
    return numbers


def layoutResult(result):
    sg.theme('DarkAmber')
    layout = [[sg.Text('Result of operation:')],
              [sg.Text(result)],
              [sg.Button('Close')]]
    window = sg.Window('SOAP Sum: dneonline', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            return 1
        break


def main():

    while True:
        opt = layout0()
        print(opt['operation'])

        if(opt['operation']) == 'Sum':
            numbers = layout1()
            if len(numbers) > 0:
                rs = layoutResult(Soma(numbers[0], numbers[1]))
        elif(opt['operation']) == 'Div':
            numbers = layout1()
            if len(numbers) > 0:
                layoutResult(Divisao(numbers[0], numbers[1]))
        elif (opt['operation']) == 'Mul':
            numbers = layout1()
            if len(numbers) > 0:
                layoutResult(Multiplicacao(numbers[0], numbers[1]))
        elif (opt['operation']) == 'Sub':
            numbers = layout1()
            if len(numbers) > 0:
                layoutResult(Subtracao(numbers[0], numbers[1]))
        else:
            print('Data not valid')
            exit(0)


if __name__ == '__main__':
    main()
