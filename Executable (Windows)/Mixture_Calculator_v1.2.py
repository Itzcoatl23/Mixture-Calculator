#!/usr/bin/env python
# coding: utf-8

import PySimpleGUI as sg
import webbrowser
import pandas as pd
from math import fsum
import sys
import os

os.chdir(sys._MEIPASS)
data_path = 'data\\Element_Data.csv'





Element_Data = pd.read_csv(data_path)


Elements = Element_Data['Element'].tolist()


Atomic_Mass = Element_Data['Atomic_Mass'].tolist()


Quantity = [1,2,3,4,5,6,7,8,9]


Subs = ['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']


def make_window1():
    layout = [[sg.Text('\n Calculate the mass needed for each compound given a system in terms of mole percent: \n')],
              [sg.Frame('Compound 1',[[sg.Text(' ', text_color=('black'),
                                                background_color=('gray70'),
                                                size=(10,1),
                                                key='-COMP1_TXT-'),
                                      sg.Button('Edit', key='-EDIT_1-')],
                                      [sg.Text('Compound mass (u):')],
                                      [sg.Text('0.000', size=(10,1), key='-COMP1_MASS_TXT-')],
                                      [sg.Input('0',size=(5,1), key='-MOL_IN1-'),
                                       sg.Text('mol%', pad=(0,0))]]),
              sg.Frame('Compound 2', [[sg.Text(' ', text_color=('black'),
                                                background_color=('gray70'),
                                                size=(10,1),
                                                key='-COMP2_TXT-'),
                                      sg.Button('Edit', key='-EDIT_2-')],
                                      [sg.Text('Compound mass (u):')],
                                      [sg.Text('0.000', size=(10,1), key='-COMP2_MASS_TXT-')],
                                      [sg.Input('0',size=(5,1), key='-MOL_IN2-'),
                                       sg.Text('mol%', pad=(0,0))]]),
              sg.Frame('Compound 3', [[sg.Text(' ', text_color=('black'),
                                                background_color=('gray70'),
                                                size=(10,1),
                                                key='-COMP3_TXT-'),
                                      sg.Button('Edit', key='-EDIT_3-')],
                                      [sg.Text('Compound mass (u):')],
                                      [sg.Text('0.000', size=(10,1), key='-COMP3_MASS_TXT-')],
                                      [sg.Input('0',size=(5,1), key='-MOL_IN3-'),
                                       sg.Text('mol%', pad=(0,0))]]),
              sg.Frame('Compound 4', [[sg.Text(' ', text_color=('black'),
                                                background_color=('gray70'),
                                                size=(10,1),
                                                key='-COMP4_TXT-'),
                                      sg.Button('Edit', key='-EDIT_4-')],
                                      [sg.Text('Compound mass (u):')],
                                      [sg.Text('0.000', size=(10,1), key='-COMP4_MASS_TXT-')],
                                      [sg.Input('0',size=(5,1), key='-MOL_IN4-'),
                                       sg.Text('mol%', pad=(0,0))]]),
              sg.Frame('Compound 5', [[sg.Text(' ', text_color=('black'),
                                                background_color=('gray70'),
                                                size=(10,1),
                                                key='-COMP5_TXT-'),
                                      sg.Button('Edit', key='-EDIT_5-')],
                                      [sg.Text('Compound mass (u):')],
                                      [sg.Text('0.000', size=(10,1), key='-COMP5_MASS_TXT-')],
                                      [sg.Input('0',size=(5,1), key='-MOL_IN5-'),
                                       sg.Text('mol%', pad=(0,0))]])],
              [sg.Text('')],
              [sg.Text(''),
               sg.Text('Calculate for a mixture of:',pad=(0,0)),
               sg.Input('1', size=(3,1), key='-GRAMS-', pad=(0,0) ),
               sg.Text('grams    ',pad=(0,0)),
               sg.Button('Calculate', key='-CALC-'),
               sg.Text('                     ', pad=(140,0)),
               sg.Text('github.com/Itzcoatl23', text_color=('blue2'), key='-LINK-', enable_events=True)]]

    return sg.Window('Mixture Calculator v1.1', layout, finalize=True, font=('Cambria',12))

def make_window2():
    layout = [[sg.Text('HEADER')],
              [sg.Frame('Element',[[sg.Input(size=(4,1), key='-SEARCH_IN-'),
                                    sg.Button('Search', key='-SEARCH_GO-'),
                                    sg.Button('Reset List', key='-RESET_LIST-')],
                                   [sg.Listbox(values=Elements,
                                                    select_mode='single',
                                                    size=(20,10),
                                                    key='-ELEMENT_LIST-')]]),
               sg.Frame('Quantity',[[sg.Listbox(values=Quantity,
                                                    select_mode='single',
                                                    size=(8,12),
                                                    key='-QUANTITY-')]]),
              sg.Button('Add Elements', key='-ADD_ELEMENT-')],
              [sg.Text('Compound:'),
               sg.Text(' ', text_color=('black'), background_color=('gray70'), size=(10,1), key='-COMPOUND_TXT-'),
               sg.Button('Reset', key='-RESET_COMPUOND-')],
              [sg.Button('Add Compound', key='-ADD_COMPOUND-')]]

    return sg.Window('Program v1', layout, finalize=True, font=('Cambria',12))


window1 = make_window1()
window2 = None


comp_focus = ''
test = '-COMP1_TXT-'

Compound_Data = pd.DataFrame([['', 0],['', 0],['', 0],['', 0],['', 0]], columns=['Compound', 'Compound_mass'])





while True:
    window, event, values = sg.read_all_windows()



    if event == sg.WIN_CLOSED and window == window1:
        break



    if event == '-EDIT_1-' and not window2:
        window1.hide()
        window2 = make_window2()
        comp_focus = '-COMP1_TXT-'
        strx=''
        comp_mass_focus = '-COMP1_MASS_TXT-'
        Compound_index = 0
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0

    if event == '-EDIT_2-' and not window2:
        window1.hide()
        window2 = make_window2()
        comp_focus = '-COMP2_TXT-'
        strx=''
        comp_mass_focus = '-COMP2_MASS_TXT-'
        Compound_index = 1
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0

    if event == '-EDIT_3-' and not window2:
        window1.hide()
        window2 = make_window2()
        comp_focus = '-COMP3_TXT-'
        strx=''
        comp_mass_focus = '-COMP3_MASS_TXT-'
        Compound_index = 2
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0

    if event == '-EDIT_4-' and not window2:
        window1.hide()
        window2 = make_window2()
        comp_focus = '-COMP4_TXT-'
        strx=''
        comp_mass_focus = '-COMP4_MASS_TXT-'
        Compound_index = 3
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0

    if event == '-EDIT_5-' and not window2:
        window1.hide()
        window2 = make_window2()
        comp_focus = '-COMP5_TXT-'
        strx=''
        comp_mass_focus = '-COMP5_MASS_TXT-'
        Compound_index = 4
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0




    if event == '-SEARCH_GO-':
        if values['-SEARCH_IN-'] != '':
            search = values['-SEARCH_IN-']
            new_values = [x for x in Elements if search in x]

            if new_values != []:

                window['-ELEMENT_LIST-'].update(new_values)
            elif new_values == []:
                sg.popup('No elements found \n Input is case sensitive', title='ERROR')


    if event == '-RESET_LIST-':
        window['-ELEMENT_LIST-'].update(Elements)
        window['-SEARCH_IN-'].update('')


    if event == '-ADD_ELEMENT-':
        if values['-ELEMENT_LIST-']:
            if values['-QUANTITY-'] != []:
                if values['-QUANTITY-'][0] > 1:
                    strx = strx + values['-ELEMENT_LIST-'][0] + Subs[values['-QUANTITY-'][0]]
                    window['-COMPOUND_TXT-'].update(strx)

                    Atom_index = Element_Data[Element_Data['Element'] == values['-ELEMENT_LIST-'][0]].index.tolist()[0]
                    Element_mass_added = Element_Data.loc[Atom_index,'Atomic_Mass']*values['-QUANTITY-'][0]
                    Compound_Data.loc[Compound_index,'Compound_mass'] = Compound_Data.loc[Compound_index,'Compound_mass'] + Element_mass_added



                elif values['-QUANTITY-'][0] == 1:
                    strx = strx + values['-ELEMENT_LIST-'][0]
                    window['-COMPOUND_TXT-'].update(strx)


                    Atom_index = Element_Data[Element_Data['Element'] == values['-ELEMENT_LIST-'][0]].index.tolist()[0]

                    Element_mass_added = Element_Data.loc[Atom_index,'Atomic_Mass']


                    Compound_Data.loc[Compound_index,'Compound_mass'] = Compound_Data.loc[Compound_index,'Compound_mass'] + Element_mass_added



    if event == '-RESET_COMPUOND-':
        strx = ''
        window['-COMPOUND_TXT-'].update(strx)
        Compound_Data.loc[Compound_index,'Compound_mass'] = 0
        Compound_Data.loc[Compound_index,'Compound'] = ''


    if window == window2 and (event in (sg.WIN_CLOSED, '-ADD_COMPOUND-')):




        window1[comp_focus].update(strx)
        Compound_Data.loc[Compound_index,'Compound'] = strx
        window1[comp_mass_focus].update('%.3f' % Compound_Data.loc[Compound_index,'Compound_mass'])

        window2.close()
        window2=None
        window1.un_hide()









    if window == window1 and (event in '-CALC-'):
        only_digits = True


        stry = values['-MOL_IN1-']+values['-MOL_IN2-']+values['-MOL_IN3-']+values['-MOL_IN4-']+values['-MOL_IN5-']+values['-GRAMS-']

        for item in stry:
            if item not in ('.0123456789'):
                only_digits = False

        if only_digits == True:
            Total_sum_mol = fsum([float(values['-MOL_IN1-']),float(values['-MOL_IN2-']),float(values['-MOL_IN3-']),float(values['-MOL_IN4-']),float(values['-MOL_IN5-'])])
            if Total_sum_mol == 100.0:


                Compound_Data.loc[0,'mass_x_fracmol'] = Compound_Data.loc[0,'Compound_mass']*float(values['-MOL_IN1-'])/100
                Compound_Data.loc[1,'mass_x_fracmol'] = Compound_Data.loc[1,'Compound_mass']*float(values['-MOL_IN2-'])/100
                Compound_Data.loc[2,'mass_x_fracmol'] = Compound_Data.loc[2,'Compound_mass']*float(values['-MOL_IN3-'])/100
                Compound_Data.loc[3,'mass_x_fracmol'] = Compound_Data.loc[3,'Compound_mass']*float(values['-MOL_IN4-'])/100
                Compound_Data.loc[4,'mass_x_fracmol'] = Compound_Data.loc[4,'Compound_mass']*float(values['-MOL_IN5-'])/100




                Total_sum = Compound_Data['mass_x_fracmol'].sum()


                Compound_Data.loc[0,'fraction'] = Compound_Data.loc[0,'mass_x_fracmol']/Total_sum
                Compound_Data.loc[1,'fraction'] = Compound_Data.loc[1,'mass_x_fracmol']/Total_sum
                Compound_Data.loc[2,'fraction'] = Compound_Data.loc[2,'mass_x_fracmol']/Total_sum
                Compound_Data.loc[3,'fraction'] = Compound_Data.loc[3,'mass_x_fracmol']/Total_sum
                Compound_Data.loc[4,'fraction'] = Compound_Data.loc[4,'mass_x_fracmol']/Total_sum

                Compound_Data.loc[0,'mol_fraction'] = values['-MOL_IN1-']
                Compound_Data.loc[1,'mol_fraction'] = values['-MOL_IN2-']
                Compound_Data.loc[2,'mol_fraction'] = values['-MOL_IN3-']
                Compound_Data.loc[3,'mol_fraction'] = values['-MOL_IN4-']
                Compound_Data.loc[4,'mol_fraction'] = values['-MOL_IN5-']





                for gui in Compound_Data.index.tolist():
                    Compound_Data.loc[gui,'mass_needed'] = Compound_Data.loc[gui,'fraction'] * float(values['-GRAMS-'])



                print(Compound_Data)# NO BORRAR

                sg.Print('\n   \n')
                sg.Print(Compound_Data.loc[:,['Compound','mol_fraction','mass_needed']])


            elif Total_sum_mol != 100.0:
                sg.popup('Sum of mol% is different from 100', title='ERROR')

        elif only_digits == False:
            sg.popup('Only numeric items in inputs are acceptable', title='ERROR')




    if event == '-LINK-' :
        webbrowser.open('https://github.com/Itzcoatl23')





window1.close()
