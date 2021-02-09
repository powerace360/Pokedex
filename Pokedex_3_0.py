# Imports the CSV library
import csv


def display(list):

    start = 0
    Pokedex = ''

    if len(list) == 0:
        Pokedex = "No Entry Found"
        return Pokedex

    for x in list.keys():
        if start == 0:
            Pokedex = f"{'###':<4} {'Name':<13} {'Region':<8} {'Weight':<11} {'Height':<8} {'Type 1':<10} {'Type 2':<10}"
            Pokedex += "\n"
            Pokedex += ('-' * 80)
            Pokedex += "\n"
            start = 1

        Num = list[x]['number']
        name2 = list[x]['name']
        region = list[x]['region']
        weight = list[x]['weight']
        height = list[x]['height']
        typ1 = list[x]['type1']
        typ2 = list[x]['type2']
        Num = int(Num)
        Num = str(Num)

        Pokedex += f"{Num:<4} {name2:<13} {region:<8} {weight:<11} {height:<8} {typ1:<10} {typ2:<10}"
        Pokedex += "\n"

    return Pokedex


def displayEvo(list2, list3):

    Pokedex = ''
    Pokedex1 = list2.copy()
    Pokedex1.clear()
    place = 0
    already = 0
    second = 0

    if len(list2) == 0:
        Pokedex = "No Entry Found"
        return Pokedex

    for x in list3.keys():
        # Finds the pokemon with evolutions based on number of evolution possibilities

        if len(Pokedex1) == 0:
            already = 0
        else:
            for i in Pokedex1.keys():
                if list3[x]['name'] == Pokedex1[i]['name']:
                    already = 1
                    break
                else:
                    already = 0
        if already == 0:
            # finds first stage pokemon
            if list3[x]['EvStage'] == '1':
                # finds how many pokemon it evolves into
                evo = list3[x]['name']
                for i in list2.keys():
                    if evo == list2[i]['name']:
                        if list2[i]['Evo8'] != '':
                            # pokemon has 8 evolutions
                            evo8 = list2[i]['Evo8']
                            evo7 = list2[i]['Evo7']
                            evo6 = list2[i]['Evo6']
                            evo5 = list2[i]['Evo5']
                            evo4 = list2[i]['Evo4']
                            evo3 = list2[i]['Evo3']
                            evo2 = list2[i]['Evo2']
                            evo1 = list2[i]['Evo1']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other 2 evolutions
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    e11 = list2[ii]
                                    Pokedex1[place] =e11
                                    place += 1
                                elif evo2 == list2[ii]['name']:
                                    e12 = list2[ii]
                                    Pokedex1[place] = e12
                                    place += 1
                                elif evo3 == list2[ii]['name']:
                                    e13 = list2[ii]
                                    Pokedex1[place] = e13
                                    place += 1
                                elif evo4 == list2[ii]['name']:
                                    e14 = list2[ii]
                                    Pokedex1[place] = e14
                                    place += 1
                                elif evo5 == list2[ii]['name']:
                                    e15 = list2[ii]
                                    Pokedex1[place] = e15
                                    place += 1
                                elif evo6 == list2[ii]['name']:
                                    e16 = list2[ii]
                                    Pokedex1[place] = e16
                                    place += 1
                                elif evo7 == list2[ii]['name']:
                                    e17 = list2[ii]
                                    Pokedex1[place] = e17
                                    place += 1
                                elif evo8 == list2[ii]['name']:
                                    e18 = list2[ii]
                                    Pokedex1[place] = e18
                                    place += 1
                                else:
                                    continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM4']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e14['number'])):<4} {e14['name']:<13} {e14['region']:<8} {e14['type1']:<10} {e14['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM5']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e15['number'])):<4} {e15['name']:<13} {e15['region']:<8} {e15['type1']:<10} {e15['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM6']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e16['number'])):<4} {e16['name']:<13} {e16['region']:<8} {e16['type1']:<10} {e16['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM7']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e17['number'])):<4} {e17['name']:<13} {e17['region']:<8} {e17['type1']:<10} {e17['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM8']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e18['number'])):<4} {e18['name']:<13} {e18['region']:<8} {e18['type1']:<10} {e18['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo3'] != '':
                            # pokemon has 3 evolutions
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            evo3 = list2[i]['Evo3']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # Compares the names to each other
                            if evo1 == evo2 and evo1 == evo3:
                                # searches for the evolution name of single pokemon
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        e13 = list2[ii + 2]
                                        Pokedex1[place] = e13
                                        place += 1
                                        break
                                    else:
                                        continue
                            else:
                                # searches for the 3 evolutions
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                    elif evo2 == list2[ii]['name']:
                                        e12 = list2[ii]
                                        Pokedex1[place] = e12
                                        place += 1
                                    elif evo3 == list2[ii]['name']:
                                        e13 = list2[ii]
                                        Pokedex1[place] = e13
                                        place += 1
                                    else:
                                        continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo2'] != '':
                            # pokemon has 2 evolution
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            # pops out the first evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other evolutions
                            if evo1 == evo2:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        if e11['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        elif e12['Evo1'] != '':
                                            evo12 = list2[ii + 1]['Evo1']
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        break
                                    else:
                                        continue
                            else:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                                for ii in list2.keys():
                                    if evo2 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo12 = list2[ii]['Evo1']
                                            e12 = list2[ii]
                                            Pokedex1[place] = e12
                                            place += 1
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                            if e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e12['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += '\n\n'
                        else:
                            # pokemon has single evolution
                            evo1 = list2[i]['Evo1']
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # finds the second evolution
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    # Sees if evolution has another evolution/two evolutions
                                    if list2[ii]['Evo2'] != '':
                                        # pokemon has 2 third evolution
                                        evo12 = list2[ii]['Evo2']
                                        evo11 = list2[ii]['Evo1']
                                        # pops out the second evolution
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        # sees if the evolution has regional variant
                                        if evo11 == evo12:
                                            # searches for first instance of evolution
                                            for iii in list2.keys():
                                                # Finds the evolution
                                                if evo11 == list2[iii]['name']:
                                                    # Saves the two evolutions and ends the loop to prevent using regional in next iteration
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    e112 = list2[iii + 1]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        else:
                                            # searches for the other 2 evolutions
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                elif evo12 == list2[iii]['name']:
                                                    e112 = list2[iii]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                else:
                                                    continue
                                    elif list2[ii]['Evo1'] != '':
                                        # Second evolution has single evolution
                                        if e1['region'] == 'Galar':
                                            if list2[ii]['region'] == 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        elif e1['region'] == 'Alola':
                                            if list2[ii]['region'] == 'Alola':
                                                evo11 = list2[i]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Alola':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        else:
                                            if list2[ii]['region'] != 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] != 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                                break
                                    else:
                                        # has no third evolution
                                        if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            break
                                        elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                        else:
                                            continue
                                else:
                                    continue
                            if e11['Evo2'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM2']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e112['number'])):<4} {e112['name']:<13} {e112['region']:<8} {e112['type1']:<10} {e112['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += '\n\n'
            elif list3[x]['EvStage'] == '0':
                e0 = list3[x]
                Pokedex1[place] = e0
                place += 1
                Pokedex += f"{str(int(e0['number'])):<4} {e0['name']:<13} {e0['region']:<8} {e0['type1']:<10} {e0['type2']:<10}"
                Pokedex += "\n\n"
            elif list3[x]['EvStage'] == '2':
                evo = list3[x]['name']
                for i in list2.keys():
                    if evo == list2[i]['Evo1'] or evo == list2[i]['Evo2'] or evo == list2[i]['Evo3'] or evo == list2[i]['Evo4']:
                        if list2[i]['Evo8'] != '':
                            # pokemon has 8 evolutions
                            evo8 = list2[i]['Evo8']
                            evo7 = list2[i]['Evo7']
                            evo6 = list2[i]['Evo6']
                            evo5 = list2[i]['Evo5']
                            evo4 = list2[i]['Evo4']
                            evo3 = list2[i]['Evo3']
                            evo2 = list2[i]['Evo2']
                            evo1 = list2[i]['Evo1']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other 2 evolutions
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    e11 = list2[ii]
                                    Pokedex1[place] =e11
                                    place += 1
                                elif evo2 == list2[ii]['name']:
                                    e12 = list2[ii]
                                    Pokedex1[place] = e12
                                    place += 1
                                elif evo3 == list2[ii]['name']:
                                    e13 = list2[ii]
                                    Pokedex1[place] = e13
                                    place += 1
                                elif evo4 == list2[ii]['name']:
                                    e14 = list2[ii]
                                    Pokedex1[place] = e14
                                    place += 1
                                elif evo5 == list2[ii]['name']:
                                    e15 = list2[ii]
                                    Pokedex1[place] = e15
                                    place += 1
                                elif evo6 == list2[ii]['name']:
                                    e16 = list2[ii]
                                    Pokedex1[place] = e16
                                    place += 1
                                elif evo7 == list2[ii]['name']:
                                    e17 = list2[ii]
                                    Pokedex1[place] = e17
                                    place += 1
                                elif evo8 == list2[ii]['name']:
                                    e18 = list2[ii]
                                    Pokedex1[place] = e18
                                    place += 1
                                else:
                                    continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM4']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e14['number'])):<4} {e14['name']:<13} {e14['region']:<8} {e14['type1']:<10} {e14['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM5']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e15['number'])):<4} {e15['name']:<13} {e15['region']:<8} {e15['type1']:<10} {e15['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM6']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e16['number'])):<4} {e16['name']:<13} {e16['region']:<8} {e16['type1']:<10} {e16['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM7']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e17['number'])):<4} {e17['name']:<13} {e17['region']:<8} {e17['type1']:<10} {e17['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM8']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e18['number'])):<4} {e18['name']:<13} {e18['region']:<8} {e18['type1']:<10} {e18['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo3'] != '':
                            # pokemon has 3 evolutions
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            evo3 = list2[i]['Evo3']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # Compares the names to each other
                            if evo1 == evo2 and evo1 == evo3:
                                # searches for the evolution name of single pokemon
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        e13 = list2[ii + 2]
                                        Pokedex1[place] = e13
                                        place += 1
                                        break
                                    else:
                                        continue
                            else:
                                # searches for the 3 evolutions
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                    elif evo2 == list2[ii]['name']:
                                        e12 = list2[ii]
                                        Pokedex1[place] = e12
                                        place += 1
                                    elif evo3 == list2[ii]['name']:
                                        e13 = list2[ii]
                                        Pokedex1[place] = e13
                                        place += 1
                                    else:
                                        continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo2'] != '':
                            # pokemon has 2 evolution
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            # pops out the first evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other evolutions
                            if evo1 == evo2:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        if e11['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        elif e12['Evo1'] != '':
                                            evo12 = list2[ii + 1]['Evo1']
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        break
                                    else:
                                        continue
                            else:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                                for ii in list2.keys():
                                    if evo2 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo12 = list2[ii]['Evo1']
                                            e12 = list2[ii]
                                            Pokedex1[place] = e12
                                            place += 1
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                            if e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e12['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += '\n\n'
                        else:
                            # pokemon has single evolution
                            evo1 = list2[i]['Evo1']
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # finds the second evolution
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    # Sees if evolution has another evolution/two evolutions
                                    if list2[ii]['Evo2'] != '':
                                        # pokemon has 2 third evolution
                                        evo12 = list2[ii]['Evo2']
                                        evo11 = list2[ii]['Evo1']
                                        # pops out the second evolution
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        # sees if the evolution has regional variant
                                        if evo11 == evo12:
                                            # searches for first instance of evolution
                                            for iii in list2.keys():
                                                # Finds the evolution
                                                if evo11 == list2[iii]['name']:
                                                    # Saves the two evolutions and ends the loop to prevent using regional in next iteration
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    e112 = list2[iii + 1]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        else:
                                            # searches for the other 2 evolutions
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                elif evo12 == list2[iii]['name']:
                                                    e112 = list2[iii]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                else:
                                                    continue
                                    elif list2[ii]['Evo1'] != '':
                                        # Second evolution has single evolution
                                        if e1['region'] == 'Galar':
                                            if list2[ii]['region'] == 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        elif e1['region'] == 'Alola':
                                            if list2[ii]['region'] == 'Alola':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Alola':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        else:
                                            if list2[ii]['region'] != 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] != 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                                break
                                    else:
                                        # has no third evolution
                                        if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            break
                                        elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                        else:
                                            continue
                                else:
                                    continue
                            if e11['Evo2'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM2']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e112['number'])):<4} {e112['name']:<13} {e112['region']:<8} {e112['type1']:<10} {e112['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += '\n\n'
                    elif evo == list2[i]['Evo5'] or evo == list2[i]['Evo6'] or evo == list2[i]['Evo7'] or evo == list2[i]['Evo8']:
                        if list2[i]['Evo8'] != '':
                            # pokemon has 8 evolutions
                            evo8 = list2[i]['Evo8']
                            evo7 = list2[i]['Evo7']
                            evo6 = list2[i]['Evo6']
                            evo5 = list2[i]['Evo5']
                            evo4 = list2[i]['Evo4']
                            evo3 = list2[i]['Evo3']
                            evo2 = list2[i]['Evo2']
                            evo1 = list2[i]['Evo1']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other 2 evolutions
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    e11 = list2[ii]
                                    Pokedex1[place] = e11
                                    place += 1
                                elif evo2 == list2[ii]['name']:
                                    e12 = list2[ii]
                                    Pokedex1[place] = e12
                                    place += 1
                                elif evo3 == list2[ii]['name']:
                                    e13 = list2[ii]
                                    Pokedex1[place] = e13
                                    place += 1
                                elif evo4 == list2[ii]['name']:
                                    e14 = list2[ii]
                                    Pokedex1[place] = e14
                                    place += 1
                                elif evo5 == list2[ii]['name']:
                                    e15 = list2[ii]
                                    Pokedex1[place] = e15
                                    place += 1
                                elif evo6 == list2[ii]['name']:
                                    e16 = list2[ii]
                                    Pokedex1[place] = e16
                                    place += 1
                                elif evo7 == list2[ii]['name']:
                                    e17 = list2[ii]
                                    Pokedex1[place] = e17
                                    place += 1
                                elif evo8 == list2[ii]['name']:
                                    e18 = list2[ii]
                                    Pokedex1[place] = e18
                                    place += 1
                                else:
                                    continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM4']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e14['number'])):<4} {e14['name']:<13} {e14['region']:<8} {e14['type1']:<10} {e14['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM5']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e15['number'])):<4} {e15['name']:<13} {e15['region']:<8} {e15['type1']:<10} {e15['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM6']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e16['number'])):<4} {e16['name']:<13} {e16['region']:<8} {e16['type1']:<10} {e16['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM7']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e17['number'])):<4} {e17['name']:<13} {e17['region']:<8} {e17['type1']:<10} {e17['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM8']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e18['number'])):<4} {e18['name']:<13} {e18['region']:<8} {e18['type1']:<10} {e18['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo3'] != '':
                            # pokemon has 3 evolutions
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            evo3 = list2[i]['Evo3']
                            # pops out the second evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # Compares the names to each other
                            if evo1 == evo2 and evo1 == evo3:
                                # searches for the evolution name of single pokemon
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        e13 = list2[ii + 2]
                                        Pokedex1[place] = e13
                                        place += 1
                                        break
                                    else:
                                        continue
                            else:
                                # searches for the 3 evolutions
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                    elif evo2 == list2[ii]['name']:
                                        e12 = list2[ii]
                                        Pokedex1[place] = e12
                                        place += 1
                                    elif evo3 == list2[ii]['name']:
                                        e13 = list2[ii]
                                        Pokedex1[place] = e13
                                        place += 1
                                    else:
                                        continue
                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM1']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM2']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                            Pokedex += "\n\t|\t" + e1['EvoM3']
                            Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                            Pokedex += '\n\n'
                        elif list2[i]['Evo2'] != '':
                            # pokemon has 2 evolution
                            evo1 = list2[i]['Evo1']
                            evo2 = list2[i]['Evo2']
                            # pops out the first evolution
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # searches for the other evolutions
                            if evo1 == evo2:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        e12 = list2[ii + 1]
                                        Pokedex1[place] = e12
                                        place += 1
                                        if e11['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        elif e12['Evo1'] != '':
                                            evo12 = list2[ii + 1]['Evo1']
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        break
                                    else:
                                        continue
                            else:
                                for ii in list2.keys():
                                    if evo1 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo11 = list2[ii]['Evo1']
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                                for ii in list2.keys():
                                    if evo2 == list2[ii]['name']:
                                        if list2[ii]['Evo1'] != '':
                                            evo12 = list2[ii]['Evo1']
                                            e12 = list2[ii]
                                            Pokedex1[place] = e12
                                            place += 1
                                            for iii in list2.keys():
                                                if evo12 == list2[iii]['name']:
                                                    e121 = list2[iii]
                                                    Pokedex1[place] = e121
                                                    place += 1
                                                else:
                                                    continue
                                        else:
                                            if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                                break
                                            elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                e12 = list2[ii]
                                                Pokedex1[place] = e12
                                                place += 1
                                            else:
                                                continue
                                    else:
                                        continue
                            if e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e12['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM2']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                Pokedex += '\n\n'
                        else:
                            # pokemon has single evolution
                            evo1 = list2[i]['Evo1']
                            e1 = list2[i]
                            Pokedex1[place] = e1
                            place += 1
                            # finds the second evolution
                            for ii in list2.keys():
                                if evo1 == list2[ii]['name']:
                                    # Sees if evolution has another evolution/two evolutions
                                    if list2[ii]['Evo2'] != '':
                                        # pokemon has 2 third evolution
                                        evo12 = list2[ii]['Evo2']
                                        evo11 = list2[ii]['Evo1']
                                        # pops out the second evolution
                                        e11 = list2[ii]
                                        Pokedex1[place] = e11
                                        place += 1
                                        # sees if the evolution has regional variant
                                        if evo11 == evo12:
                                            # searches for first instance of evolution
                                            for iii in list2.keys():
                                                # Finds the evolution
                                                if evo11 == list2[iii]['name']:
                                                    # Saves the two evolutions and ends the loop to prevent using regional in next iteration
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                    e112 = list2[iii + 1]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        else:
                                            # searches for the other 2 evolutions
                                            for iii in list2.keys():
                                                if evo11 == list2[iii]['name']:
                                                    e111 = list2[iii]
                                                    Pokedex1[place] = e111
                                                    place += 1
                                                elif evo12 == list2[iii]['name']:
                                                    e112 = list2[iii]
                                                    Pokedex1[place] = e112
                                                    place += 1
                                                else:
                                                    continue
                                    elif list2[ii]['Evo1'] != '':
                                        # Second evolution has single evolution
                                        if e1['region'] == 'Galar':
                                            if list2[ii]['region'] == 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        elif e1['region'] == 'Alola':
                                            if list2[ii]['region'] == 'Alola':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] == 'Alola':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                        else:
                                            if list2[ii]['region'] != 'Galar':
                                                evo11 = list2[ii]['Evo1']
                                                e11 = list2[ii]
                                                Pokedex1[place] = e11
                                                place += 1
                                                # finds the third evolution
                                                for iii in list2.keys():
                                                    if evo11 == list2[iii]['name']:
                                                        if list2[iii]['region'] != 'Galar':
                                                            e111 = list2[iii]
                                                            Pokedex1[place] = e111
                                                            place += 1
                                                            break
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                                break
                                    else:
                                        # has no third evolution
                                        if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                            break
                                        elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                            e11 = list2[ii]
                                            Pokedex1[place] = e11
                                            place += 1
                                        else:
                                            continue
                                else:
                                    continue
                            if e11['Evo2'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM2']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e112['number'])):<4} {e112['name']:<13} {e112['region']:<8} {e112['type1']:<10} {e112['type2']:<10}"
                                Pokedex += '\n\n'
                            elif e11['Evo1'] != '':
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                Pokedex += '\n\n'
                            else:
                                Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                Pokedex += "\n\t|\t" + e1['EvoM1']
                                Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                Pokedex += '\n\n'
                    else:
                        continue
            elif list3[x]['EvStage'] == '3':
                evo = list3[x]['name']
                for i in list2.keys():
                    if evo == list2[i]['Evo1'] or evo == list2[i]['Evo2']:
                        evo0 = list2[i]['name']
                        for ii in Pokedex1.keys():
                            if list2[i] == Pokedex1[ii]: # and list2[i]['region'] == Pokedex1[ii]['region']:
                                second = 1
                                break
                            else:
                                second = 0
                        if second == 0:
                            for ii in list2.keys():
                                if evo0 == list2[ii]['Evo1'] or evo == list2[ii]['Evo2']:
                                    if list2[ii]['Evo8'] != '':
                                        # pokemon has 8 evolutions
                                        evo8 = list2[ii]['Evo8']
                                        evo7 = list2[ii]['Evo7']
                                        evo6 = list2[ii]['Evo6']
                                        evo5 = list2[ii]['Evo5']
                                        evo4 = list2[ii]['Evo4']
                                        evo3 = list2[ii]['Evo3']
                                        evo2 = list2[ii]['Evo2']
                                        evo1 = list2[ii]['Evo1']
                                        # pops out the second evolution
                                        e1 = list2[ii]
                                        Pokedex1[place] = e1
                                        place += 1
                                        # searches for the other 2 evolutions
                                        for iii in list2.keys():
                                            if evo1 == list2[iii]['name']:
                                                e11 = list2[iii]
                                                Pokedex1[place] = e11
                                                place += 1
                                            elif evo2 == list2[iii]['name']:
                                                e12 = list2[iii]
                                                Pokedex1[place] = e12
                                                place += 1
                                            elif evo3 == list2[iii]['name']:
                                                e13 = list2[iii]
                                                Pokedex1[place] = e13
                                                place += 1
                                            elif evo4 == list2[iii]['name']:
                                                e14 = list2[iii]
                                                Pokedex1[place] = e14
                                                place += 1
                                            elif evo5 == list2[iii]['name']:
                                                e15 = list2[iii]
                                                Pokedex1[place] = e15
                                                place += 1
                                            elif evo6 == list2[iii]['name']:
                                                e16 = list2[iii]
                                                Pokedex1[place] = e16
                                                place += 1
                                            elif evo7 == list2[iii]['name']:
                                                e17 = list2[iii]
                                                Pokedex1[place] = e17
                                                place += 1
                                            elif evo8 == list2[ii]['name']:
                                                e18 = list2[iii]
                                                Pokedex1[place] = e18
                                                place += 1
                                            else:
                                                continue
                                        Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM1']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM2']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM3']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM4']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e14['number'])):<4} {e14['name']:<13} {e14['region']:<8} {e14['type1']:<10} {e14['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM5']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e15['number'])):<4} {e15['name']:<13} {e15['region']:<8} {e15['type1']:<10} {e15['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM6']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e16['number'])):<4} {e16['name']:<13} {e16['region']:<8} {e16['type1']:<10} {e16['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM7']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e17['number'])):<4} {e17['name']:<13} {e17['region']:<8} {e17['type1']:<10} {e17['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM8']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e18['number'])):<4} {e18['name']:<13} {e18['region']:<8} {e18['type1']:<10} {e18['type2']:<10}"
                                        Pokedex += '\n\n'
                                    elif list2[ii]['Evo3'] != '':
                                        # pokemon has 3 evolutions
                                        evo1 = list2[ii]['Evo1']
                                        evo2 = list2[ii]['Evo2']
                                        evo3 = list2[ii]['Evo3']
                                        # pops out the second evolution
                                        e1 = list2[ii]
                                        Pokedex1[place] = e1
                                        place += 1
                                        # Compares the names to each other
                                        if evo1 == evo2 and evo1 == evo3:
                                            # searches for the evolution name of single pokemon
                                            for iii in list2.keys():
                                                if evo1 == list2[iii]['name']:
                                                    e11 = list2[iii]
                                                    Pokedex1[place] = e11
                                                    place += 1
                                                    e12 = list2[iii + 1]
                                                    Pokedex1[place] = e12
                                                    place += 1
                                                    e13 = list2[iii + 2]
                                                    Pokedex1[place] = e13
                                                    place += 1
                                                    break
                                                else:
                                                    continue
                                        else:
                                            # searches for the 3 evolutions
                                            for iii in list2.keys():
                                                if evo1 == list2[iii]['name']:
                                                    e11 = list2[iii]
                                                    Pokedex1[place] = e11
                                                    place += 1
                                                elif evo2 == list2[iii]['name']:
                                                    e12 = list2[iii]
                                                    Pokedex1[place] = e12
                                                    place += 1
                                                elif evo3 == list2[iii]['name']:
                                                    e13 = list2[iii]
                                                    Pokedex1[place] = e13
                                                    place += 1
                                                else:
                                                    continue
                                        Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM1']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM2']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                        Pokedex += "\n\t|\t" + e1['EvoM3']
                                        Pokedex += '\n\t\u21B3 ' f"{str(int(e13['number'])):<4} {e13['name']:<13} {e13['region']:<8} {e13['type1']:<10} {e13['type2']:<10}"
                                        Pokedex += '\n\n'
                                    elif list2[ii]['Evo2'] != '':
                                        # pokemon has 2 evolution
                                        evo1 = list2[ii]['Evo1']
                                        evo2 = list2[ii]['Evo2']
                                        # pops out the first evolution
                                        e1 = list2[ii]
                                        Pokedex1[place] = e1
                                        place += 1
                                        # searches for the other evolutions
                                        if evo1 == evo2:
                                            for iii in list2.keys():
                                                if evo1 == list2[iii]['name']:
                                                    e11 = list2[iii]
                                                    Pokedex1[place] = e11
                                                    place += 1
                                                    e12 = list2[iii + 1]
                                                    Pokedex1[place] = e12
                                                    place += 1
                                                    if e11['Evo1'] != '':
                                                        evo11 = list2[iii]['Evo1']
                                                        for iiii in list2.keys():
                                                            if evo11 == list2[iiii]['name']:
                                                                e111 = list2[iiii]
                                                                Pokedex1[place] = e111
                                                                place += 1
                                                                break
                                                            else:
                                                                continue
                                                    elif e12['Evo1'] != '':
                                                        evo12 = list2[ii + 1]['Evo1']
                                                        for iiii in list2.keys():
                                                            if evo12 == list2[iiii]['name']:
                                                                e121 = list2[iiii]
                                                                Pokedex1[place] = e121
                                                                place += 1
                                                                break
                                                            else:
                                                                continue
                                                    break
                                                else:
                                                    continue
                                        else:
                                            for iii in list2.keys():
                                                if evo1 == list2[iii]['name']:
                                                    if list2[iii]['Evo1'] != '':
                                                        evo11 = list2[iii]['Evo1']
                                                        e11 = list2[iii]
                                                        Pokedex1[place] = e11
                                                        place += 1
                                                        for iiii in list2.keys():
                                                            if evo11 == list2[iiii]['name']:
                                                                e111 = list2[iiii]
                                                                Pokedex1[place] = e111
                                                                place += 1
                                                            else:
                                                                continue
                                                    else:
                                                        if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                            e11 = list2[iii]
                                                            Pokedex1[place] = e11
                                                            place += 1
                                                            break
                                                        elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                            e11 = list2[iii]
                                                            Pokedex1[place] = e11
                                                            place += 1
                                                        else:
                                                            continue
                                                else:
                                                    continue
                                            for iii in list2.keys():
                                                if evo2 == list2[iii]['name']:
                                                    if list2[iii]['Evo1'] != '':
                                                        evo12 = list2[iii]['Evo1']
                                                        e12 = list2[iii]
                                                        Pokedex1[place] = e12
                                                        place += 1
                                                        for iiii in list2.keys():
                                                            if evo12 == list2[iiii]['name']:
                                                                e121 = list2[iiii]
                                                                Pokedex1[place] = e121
                                                                place += 1
                                                            else:
                                                                continue
                                                    else:
                                                        if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                            e12 = list2[iii]
                                                            Pokedex1[place] = e12
                                                            place += 1
                                                            break
                                                        elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                            e12 = list2[iii]
                                                            Pokedex1[place] = e12
                                                            place += 1
                                                        else:
                                                            continue
                                                else:
                                                    continue
                                        if e11['Evo1'] != '':
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM2']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                            Pokedex += '\n\n'
                                        elif e12['Evo1'] != '':
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM2']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e12['EvoM1']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e121['number'])):<4} {e121['name']:<13} {e121['region']:<8} {e121['type1']:<10} {e121['type2']:<10}"
                                            Pokedex += '\n\n'
                                        else:
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM2']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e12['number'])):<4} {e12['name']:<13} {e12['region']:<8} {e12['type1']:<10} {e12['type2']:<10}"
                                            Pokedex += '\n\n'
                                    else:
                                        # pokemon has single evolution
                                        evo1 = list2[ii]['Evo1']
                                        e1 = list2[ii]
                                        Pokedex1[place] = e1
                                        place += 1
                                        # finds the second evolution
                                        for iii in list2.keys():
                                            if evo1 == list2[iii]['name']:
                                                # Sees if evolution has another evolution/two evolutions
                                                if list2[iii]['Evo2'] != '':
                                                    # pokemon has 2 third evolution
                                                    evo12 = list2[iii]['Evo2']
                                                    evo11 = list2[iii]['Evo1']
                                                    # pops out the second evolution
                                                    e11 = list2[iii]
                                                    Pokedex1[place] = e11
                                                    place += 1
                                                    # sees if the evolution has regional variant
                                                    if evo11 == evo12:
                                                        # searches for first instance of evolution
                                                        for iiii in list2.keys():
                                                            # Finds the evolution
                                                            if evo11 == list2[iiii]['name']:
                                                                # Saves the two evolutions and ends the loop to prevent using regional in next iteration
                                                                e111 = list2[iiii]
                                                                Pokedex1[place] = e111
                                                                place += 1
                                                                e112 = list2[iiii + 1]
                                                                Pokedex1[place] = e112
                                                                place += 1
                                                                break
                                                            else:
                                                                continue
                                                    else:
                                                        # searches for the other 2 evolutions
                                                        for iiii in list2.keys():
                                                            if evo11 == list2[iiii]['name']:
                                                                e111 = list2[iiii]
                                                                Pokedex1[place] = e111
                                                                place += 1
                                                            elif evo12 == list2[iiii]['name']:
                                                                e112 = list2[iiii]
                                                                Pokedex1[place] = e112
                                                                place += 1
                                                            else:
                                                                continue
                                                elif list2[iii]['Evo1'] != '':
                                                    # Second evolution has single evolution
                                                    if e1['region'] == 'Galar':
                                                        if list2[iii]['region'] == 'Galar':
                                                            evo11 = list2[iii]['Evo1']
                                                            e11 = list2[iii]
                                                            Pokedex1[place] = e11
                                                            place += 1
                                                            # finds the third evolution
                                                            for iiii in list2.keys():
                                                                if evo11 == list2[iiii]['name']:
                                                                    if list2[iiii]['region'] == 'Galar':
                                                                        e111 = list2[iiii]
                                                                        Pokedex1[place] = e111
                                                                        place += 1
                                                                        break
                                                                    else:
                                                                        continue
                                                                else:
                                                                    continue
                                                    elif e1['region'] == 'Alola':
                                                        if list2[iii]['region'] == 'Alola':
                                                            evo11 = list2[iii]['Evo1']
                                                            e11 = list2[iii]
                                                            Pokedex1[place] = e11
                                                            place += 1
                                                            # finds the third evolution
                                                            for iiii in list2.keys():
                                                                if evo11 == list2[iiii]['name']:
                                                                    if list2[iiii]['region'] == 'Alola':
                                                                        e111 = list2[iiii]
                                                                        Pokedex1[place] = e111
                                                                        place += 1
                                                                        break
                                                                    else:
                                                                        continue
                                                                else:
                                                                    continue
                                                    else:
                                                        if list2[iii]['region'] != 'Galar':
                                                            evo11 = list2[iii]['Evo1']
                                                            e11 = list2[iii]
                                                            Pokedex1[place] = e11
                                                            place += 1
                                                            # finds the third evolution
                                                            for iiii in list2.keys():
                                                                if evo11 == list2[iiii]['name']:
                                                                    if list2[iiii]['region'] != 'Galar':
                                                                        e111 = list2[iiii]
                                                                        Pokedex1[place] = e111
                                                                        place += 1
                                                                        break
                                                                    else:
                                                                        continue
                                                                else:
                                                                    continue
                                                            break
                                                else:
                                                    # has no third evolution
                                                    if e1['region'] != 'Alola' and e1['region'] != 'Galar':
                                                        e11 = list2[iii]
                                                        Pokedex1[place] = e11
                                                        place += 1
                                                        break
                                                    elif e1['region'] == 'Alola' or e1['region'] == 'Galar':
                                                        e11 = list2[iii]
                                                        Pokedex1[place] = e11
                                                        place += 1
                                                    else:
                                                        continue
                                            else:
                                                continue
                                        if e11['Evo2'] != '':
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e11['EvoM2']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e112['number'])):<4} {e112['name']:<13} {e112['region']:<8} {e112['type1']:<10} {e112['type2']:<10}"
                                            Pokedex += '\n\n'
                                        elif e11['Evo1'] != '':
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += "\n\t\t|\t" + e11['EvoM1']
                                            Pokedex += '\n\t\t\u21B3 ' f"{str(int(e111['number'])):<4} {e111['name']:<13} {e111['region']:<8} {e111['type1']:<10} {e111['type2']:<10}"
                                            Pokedex += '\n\n'
                                        else:
                                            Pokedex += f"{str(int(e1['number'])):<4} {e1['name']:<13} {e1['region']:<8} {e1['type1']:<10} {e1['type2']:<10}"
                                            Pokedex += "\n\t|\t" + e1['EvoM1']
                                            Pokedex += '\n\t\u21B3 ' f"{str(int(e11['number'])):<4} {e11['name']:<13} {e11['region']:<8} {e11['type1']:<10} {e11['type2']:<10}"
                                            Pokedex += '\n\n'
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

        already = 0

    return Pokedex


def alpha(list4, reverse):
    # creates list to sort names
    nam = []
    # integer to go through the whole pokedex
    y = 0
    # integer to place the new pokedex dictionary in the correct place
    place = 0

    # Creates new list called PokedexA that will be returned containing the list in alphabetical order
    PokedexA = list4.copy()
    # Clears list to start fresh
    PokedexA.clear()

    if len(list4) == 0:
        return PokedexA

    for count in list4.keys():
        # for the length of the pokedex add just the name to the list
        nam.append(list4[count]['name'])

    # If else to determine if the list is sorted A-Z or Z-A
    if reverse == "1":
        # List is sorted A-Z
        nam.sort()
    else:
        # List is sorted Z-A
        nam.sort(reverse=True)

    # While loop to go through the length of the dictionary list2
    while y < len(list4):
        # For loop to compare to each item in the dictionary
        for ne in list4.keys():
            # If else statement to compare list to dictionary for sorting of the dictionary
            if nam[y] == list4[ne]['name']:
                # Some pokemon are listed multiple times in pokedex this ensure correct entry is selected
                if nam[y] == nam[y - 5]:
                    PokedexA[place] = list4[ne + 5]
                    place += 1
                    break
                elif nam[y] == nam[y-4]:
                    PokedexA[place] = list4[ne + 4]
                    place += 1
                    break
                elif nam[y] == nam[y-3]:
                    PokedexA[place] = list4[ne + 3]
                    place += 1
                    break
                elif nam[y] == nam[y-2]:
                    PokedexA[place] = list4[ne + 2]
                    place += 1
                    break
                elif nam[y] == nam[y-1]:
                    PokedexA[place] = list4[ne + 1]
                    place += 1
                    break
                else:
                    PokedexA[place] = list4[ne]
                    place += 1
                    break
            else:
                continue

        y += 1
    return PokedexA


def weight_order(list5, reverse):

    # creates blank list to help with ordering
    whgt = []
    # Integer to ensure the whole pokedex is run through
    y = 0
    # integer to place the entry in a new dictionary
    place = 0
    # Creates and clears ne dictionary that is sent back to main code
    PokedexW = list5.copy()
    PokedexW.clear()

    if len(list5) == 0:
        return PokedexW

    for count in list5.keys():
        # The list is filled with both the name as a string and weight as a double
        whgt.append([list5[count]['name'], list5[count]['weightN']])

    # If else to determine if the list is sorted lightest to heaviest or vice versa
    if reverse == "1":
        # sorted lightest to heaviest
        whgt.sort(key=lambda weight: weight[1])
    else:
        # sorted heaviest to lightest
        whgt.sort(key=lambda weight: weight[1], reverse=True)

    # unknown
    columns = list(zip(*whgt))

    # separates the sorted list into name and weight for ease of looping through
    nameO = columns[0]
    weightO = columns[1]

    # For the length of the list
    while y < len(list5):
        # for the length of the number of keys
        for ne in list5.keys():
            # Compares the name of the sorted list to the dictionary
            if nameO[y] == list5[ne]['name']:
                # Compares the weight of the found name to the weight of the sorted list
                if weightO[y] == list5[ne]['weightN']:
                    #
                    if nameO[y] == nameO[y - 5]:
                        PokedexW[place] = list5[ne + 5]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 4]:
                        PokedexW[place] = list5[ne + 4]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 3]:
                        PokedexW[place] = list5[ne + 3]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 2]:
                        PokedexW[place] = list5[ne + 2]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 1]:
                        PokedexW[place] = list5[ne + 1]
                        place += 1
                        break
                    else:
                        PokedexW[place] = list5[ne]
                        place += 1
                        break
                else:
                    continue
            else:
                continue

        y += 1
    return PokedexW


def height_order(list6, reverse):

    hght = []
    y = 0
    place = 0
    PokedexH = list6.copy()
    PokedexH.clear()

    if len(list6) == 0:
        return PokedexH

    for count in list6.keys():
        hght.append([list6[count]['name'], list6[count]['height'], list6[count]['heightN']])

    if reverse == "1":
        hght.sort(key=lambda height: height[2])
    else:
        hght.sort(key=lambda height: height[2], reverse=True)

    columns = list(zip(*hght))

    nameO = columns[0]
    heightO = columns[1]

    while y < len(list6):
        for ne in list6.keys():
            if nameO[y] == list6[ne]['name']:
                if heightO[y] == list6[ne]['height']:
                    if nameO[y] == nameO[y - 5]:
                        PokedexH[place] = list6[ne + 5]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 4]:
                        PokedexH[place] = list6[ne + 4]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 3]:
                        PokedexH[place] = list6[ne + 3]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 2]:
                        PokedexH[place] = list6[ne + 2]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 1]:
                        PokedexH[place] = list6[ne + 1]
                        place += 1
                        break
                    else:
                        PokedexH[place] = list6[ne]
                        place += 1
                        break
                else:
                    continue
            else:
                continue

        y += 1
    return PokedexH


def numerical_order(list7, reverse):
    # creates list to sort names
    num = []
    # integer to go through the whole pokedex
    y = 0
    # integer to place the new pokedex dictionary in the correct place
    place = 0

    # Creates new list called PokedexN that will be returned containing the list in alphabetical order
    PokedexN = list7.copy()
    # Clears list to start fresh
    PokedexN.clear()

    if len(list7) == 0:
        return PokedexN

    for count in list7.keys():
        # for the length of the pokedex add just the name to the list
        num.append(list7[count]['number'])

    # If else to determine if the list is sorted A-Z or Z-A
    if reverse == "1":
        # List is sorted 1-898
        num.sort()
    else:
        # List is sorted 898-1
        num.sort(reverse=True)

    # While loop to go through the length of the dictionary list2
    while y < len(list7):
        # For loop to compare to each item in the dictionary
        for ne in list7.keys():
            # If else statement to compare list to dictionary for sorting of the dictionary
            if num[y] == list7[ne]['number']:
                # Some pokemon are listed multiple times in pokedex this ensure correct entry is selected
                if num[y] == num[y - 5]:
                    PokedexN[place] = list7[ne + 5]
                    place += 1
                    break
                elif num[y] == num[y - 4]:
                    PokedexN[place] = list7[ne + 4]
                    place += 1
                    break
                elif num[y] == num[y - 3]:
                    PokedexN[place] = list7[ne + 3]
                    place += 1
                    break
                elif num[y] == num[y - 2]:
                    PokedexN[place] = list7[ne + 2]
                    place += 1
                    break
                elif num[y] == num[y - 1]:
                    PokedexN[place] = list7[ne + 1]
                    place += 1
                    break
                else:
                    PokedexN[place] = list7[ne]
                    place += 1
                    break
            else:
                continue

        y += 1
    return PokedexN


def show_type(list8, typeA, choose):

    PokedexT = list8.copy()
    PokedexT.clear()
    place = 0

    if len(list8) == 0:
        return PokedexT

    if choose == "1":
        for x in list8.keys():
            if list8[x]['type2'] == typeA.capitalize() or list8[x]['type1'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "2":
        for x in list8.keys():
            if list8[x]['type1'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "3":
        for x in list8.keys():
            if list8[x]['type2'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "4":
        for x in list8.keys():
            if list8[x]['type1'] == typeA.capitalize() and list8[x]['type2'] == '':
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    else:
        PokedexT.clear()
    return PokedexT


def find(list9, name3):

    PokedexF = list9.copy()
    PokedexF.clear()
    place = 0
    found = 0

    if len(list9) == 0:
        return PokedexF

    for x in list9.keys():
        if name3.capitalize() == list9[x]['name']:
            PokedexF[place] = list9[x]
            place += 1
            found = 1
        else:
            continue
    if found == 0:
        PokedexF.clear()
    return PokedexF


def find_with(list10, name4):

    PokedexFW = list10.copy()
    PokedexFW.clear()
    place = 0
    found = 0

    if len(list10) == 0:
        return PokedexFW

    for x in list10.keys():
        if name4 == '':
            break
        elif name4.lower() in list10[x]['name'] or name4.capitalize() in list10[x]['name']:
            PokedexFW[place] = list10[x]
            place += 1
            found = 1
        else:
            continue
    if found == 0:
        PokedexFW.clear()
    return PokedexFW


def region(list11, reg):

    PokedexR = list11.copy()
    PokedexR.clear()
    place = 0

    if len(list11) == 0:
        return PokedexR

    for x in list11.keys():
        if list11[x]['region'] == reg.capitalize():
            PokedexR[place] = list11[x]
            place += 1
        else:
            continue

    return PokedexR


def define_list():
    # Sets up a blank dictionary
    pokemon = {
        'name': '',
        'number': 0.0,
        'region': '',
        'weight': '',
        'height': '',
        'type1': '',
        'type2': '',
        'heightN': 0.0,
        'weightN': 0.0,
        'Evo1': '',
        'Evo2': '',
        'Evo3': '',
        'Evo4': '',
        'Evo5': '',
        'Evo6': '',
        'Evo7': '',
        'Evo8': '',
        'EvoM1': '',
        'EvoM2': '',
        'EvoM3': '',
        'EvoM4': '',
        'EvoM5': '',
        'EvoM6': '',
        'EvoM7': '',
        'EvoM8': '',
        'EvStage': ''
    }
    # Name = Pokemon's name
    # Number = Pokemon's National Pokedex Number
    # Region = Pokemon's Original Region
    # Weight = Pokemon's Weight as a String
    # Height = Pokemon's Height as a String
    # Type1 = Pokemon's Primary Type
    # Type2 = Pokemon's Secondary Type
    # HeightN = Pokemon's Height as a Floating Number
    # WeightN = Pokemon's Weight as a Floating Number

    # Clears the dictionary to remove the first entry
    pokemon.clear()

    # Opens the csv file of pokemon entries
    with open('Pokedex_List.csv', encoding='utf-8', newline='') as f:
        reader = enumerate(csv.reader(f))

        # Increments through the rows
        for i, row in reader:
            if i > 0:
                # Saves the information of the different rows and columns
                numb = float(row[0])    # Saves the pokemon's number
                name = row[1]           # Saves the pokemon's name
                reg = row[2]            # Saves the pokemon's region
                wgt = row[3] + " lbs"   # Saves the pokemon's weight as a string
                wgt2 = float(row[3])    # Saves the pokemon's weight as a floating number
                hgt = row[4]            # Saves the pokemon's height
                tp1 = row[5]            # Saves the pokemon's first type
                tp2 = row[6]            # Saves the pokemon's second type
                hgtN = float(row[7])    # Saves the pokemon's height as a floating number
                evo1 = row[8]
                evo2 = row[9]
                evo3 = row[10]
                evo4 = row[11]
                evo5 = row[12]
                evo6 = row[13]
                evo7 = row[14]
                evo8 = row[15]
                evoM1 = row[16]
                evoM2 = row[17]
                evoM3 = row[18]
                evoM4 = row[19]
                evoM5 = row[20]
                evoM6 = row[21]
                evoM7 = row[22]
                evoM8 = row[23]
                evs = row[24]
                # Ensures the strings are capitalized
                name = str.title(name)      # Saves the name with each word capitalized
                reg = str.capitalize(reg)   # Saves the region capitalized
                tp1 = str.capitalize(tp1)   # Saves the first type capitalized
                tp2 = str.capitalize(tp2)   # Saves the second type capitalized
                evo1 = str.title(evo1)      # Saves the name with each word capitalized
                evo2 = str.title(evo2)      # Saves the name with each word capitalized
                evo3 = str.title(evo3)      # Saves the name with each word capitalized
                evo4 = str.title(evo4)      # Saves the name with each word capitalized
                evo5 = str.title(evo5)      # Saves the name with each word capitalized
                evo6 = str.title(evo6)      # Saves the name with each word capitalized
                evo7 = str.title(evo7)      # Saves the name with each word capitalized
                evo8 = str.title(evo8)      # Saves the name with each word capitalized
                evoM1 = str.title(evoM1)
                evoM2 = str.title(evoM2)
                evoM3 = str.title(evoM3)
                evoM4 = str.title(evoM4)
                evoM5 = str.title(evoM5)
                evoM6 = str.title(evoM6)
                evoM7 = str.title(evoM7)
                evoM8 = str.title(evoM8)
                # Saves the information to the directory
                pokemon.update({i: {'name': name, 'number': numb, 'region': reg, 'weight': wgt, 'height': hgt,
                                    'type1': tp1, 'type2': tp2, 'heightN': hgtN, 'weightN': wgt2, 'Evo1': evo1,
                                    'Evo2': evo2, 'Evo3': evo3, 'Evo4': evo4, 'Evo5': evo5, 'Evo6': evo6, 'Evo7': evo7,
                                    'Evo8': evo8, 'EvoM1': evoM1, 'EvoM2': evoM2, 'EvoM3': evoM3, 'EvoM4': evoM4,
                                    'EvoM5': evoM5, 'EvoM6': evoM6, 'EvoM7': evoM7, 'EvoM8': evoM8, 'EvStage': evs}})

    return pokemon  # Returns the list to the main program
