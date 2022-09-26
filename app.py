from interface_grafica import *
from consulta_cep import *

tela_inicial()
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Consultar':
        try:
            logradouro = consulta(values['cep'])['logradouro']
            localidade = consulta(values['cep'])['localidade']
            bairro = consulta(values['cep'])['bairro']
            uf = consulta(values['cep'])['uf']
            ibge = consulta(values['cep'])['ibge']
            ddd = consulta(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['localidade'].update(localidade)
            window['bairro'].update(bairro)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)

        except:
            sg.Popup('Verifique se o o campo "Cep" foi preenchido corretamente\n'
                     'ou se esta conectado a internet', font='arial 12', title='ERRO')
