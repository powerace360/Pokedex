# Code that creates a GUI with buttons to work with the Pokedex code

# Imports tkinter to make GUI applications
import tkinter
# Imports an already writen code Pokedex_2_0 as dex to search the Pokedex
import Pokedex_3_0 as dex


def Display():
    # Runs the Pokedex code to display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    Poke = dex.display(list2)           # Saves the string of Pokedex entries in Poke
    return Poke           # Displays the pokedex entries in the text window


def DisplayBase():
    # Runs the Pokedex code to display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    Poke = dex.display(list1)           # Saves the string of Pokedex entries in Poke
    list2 = list1
    entry.insert("1.0", Poke)           # Displays the pokedex entries in the text window


def DisplayEvolution():
    # Runs the Pokedex code to display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    Poke = dex.displayEvo(list1, list2)
    entry.insert("1.0", Poke)           # Displays the pokedex entries in the text window


def DisplayAlphZ():
    # Runs the Pokedex code to display Pokemon in alphabetical order Z-A
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.alpha(list2, "0")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayAlphA():
    # Runs the Pokedex code to display Pokemon in alphabetical order A-Z
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.alpha(list2, "1")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayWgtU():
    # Runs the Pokedex code to sort the pokemon by weight lightest to heaviest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.weight_order(list2, "1")  # Saves the weight list in poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayWgtD():
    # Runs the Pokedex code to sort the pokemon by weight heaviest to lightest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.weight_order(list2, "0")  # Saves the weight list in poke
    Poke = Display()
    entry.insert("1.0", Poke)           # displays the list in the text window


def DisplayHgtU():
    # Runs the Pokedex code to sort the pokemon by height shortest to tallest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.height_order(list2, "1")  # Saves the height list in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayHgtD():
    # Runs the Pokedex code to sort the pokemon by height tallest to shortest
    global  list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.height_order(list2, "0")  # Saves the height list in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayNumU():
    # Runs the Pokedex code to display Pokemon in numerical order upwards
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.numerical_order(list2, "1")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayNumD():
    # Runs the Pokedex code to display Pokemon in numerical order downwards
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = dex.numerical_order(list2, "0")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayRegion():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    reg = entry2.get()                  # Saves the entered region for easier testing in if statement
    reg = reg.capitalize()              # Saves the region as a capitalized string for easier testing
    # If statement to ensure a region was entered, if incorrect region entered then states it
    if reg == 'Kanto' or reg == 'Johto' or reg == 'Hoenn' or reg == 'Sinnoh' or reg == 'Unova':
        list2 = dex.region(list2, entry2.get())
        Poke = Display()
    elif reg == 'Kalos' or reg == 'Alola' or reg == 'Galar':
        list2 = dex.region(list2, entry2.get())
        Poke = Display()
    else:
        Poke = "Region does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeM():
    # Runs the Pokedex code to display Monotype pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    # If statement to ensure a type was entered, if incorrect type entered then states it
    if typ == 'Normal' or typ == 'Fire' or typ == 'Water' or typ == 'Grass' or typ == 'Poison':
        list2 = dex.show_type(list2, entry3.get(), "4")
        Poke = Display()
    elif typ == 'Fighting' or typ == 'Ice' or typ == 'Electric' or typ == 'Ground' or typ == 'Flying':
        list2 = dex.show_type(list2, entry3.get(), "4")
        Poke = Display()
    elif typ == 'Psychic' or typ == 'Bug' or typ == 'Rock' or typ == 'Ghost' or typ == 'Dragon':
        list2 = dex.show_type(list2, entry3.get(), "4")
        Poke = Display()
    elif typ == 'Dark' or typ == 'Steel' or typ == 'Fairy':
        list2 = dex.show_type(list2, entry3.get(), "4")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeP():
    # Runs the Pokedex code to display Primary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    # If statement to ensure a type was entered, if incorrect type entered then states it
    if typ == 'Normal' or typ == 'Fire' or typ == 'Water' or typ == 'Grass' or typ == 'Poison':
        list2 = dex.show_type(list2, entry3.get(), "2")
        Poke = Display()
    elif typ == 'Fighting' or typ == 'Ice' or typ == 'Electric' or typ == 'Ground' or typ == 'Flying':
        list2 = dex.show_type(list2, entry3.get(), "2")
        Poke = Display()
    elif typ == 'Psychic' or typ == 'Bug' or typ == 'Rock' or typ == 'Ghost' or typ == 'Dragon':
        list2 = dex.show_type(list2, entry3.get(), "2")
        Poke = Display()
    elif typ == 'Dark' or typ == 'Steel' or typ == 'Fairy':
        list2 = dex.show_type(list2, entry3.get(), "2")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeS():
    # Runs the Pokedex code to display Secondary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    # If statement to ensure a type was entered, if incorrect type entered then states it
    if typ == 'Normal' or typ == 'Fire' or typ == 'Water' or typ == 'Grass' or typ == 'Poison':
        list2 = dex.show_type(list2, entry3.get(), "3")
        Poke = Display()
    elif typ == 'Fighting' or typ == 'Ice' or typ == 'Electric' or typ == 'Ground' or typ == 'Flying':
        list2 = dex.show_type(list2, entry3.get(), "3")
        Poke = Display()
    elif typ == 'Psychic' or typ == 'Bug' or typ == 'Rock' or typ == 'Ghost' or typ == 'Dragon':
        list2 = dex.show_type(list2, entry3.get(), "3")
        Poke = Display()
    elif typ == 'Dark' or typ == 'Steel' or typ == 'Fairy':
        list2 = dex.show_type(list2, entry3.get(), "3")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeB():
    # Runs the Pokedex code to display Primary and Secondary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    # If statement to ensure a type was entered, if incorrect type entered then states it
    if typ == 'Normal' or typ == 'Fire' or typ == 'Water' or typ == 'Grass' or typ == 'Poison':
        list2 = dex.show_type(list2, entry3.get(), "1")
        Poke = Display()
    elif typ == 'Fighting' or typ == 'Ice' or typ == 'Electric' or typ == 'Ground' or typ == 'Flying':
        list2 = dex.show_type(list2, entry3.get(), "1")
        Poke = Display()
    elif typ == 'Psychic' or typ == 'Bug' or typ == 'Rock' or typ == 'Ghost' or typ == 'Dragon':
        list2 = dex.show_type(list2, entry3.get(), "1")
        Poke = Display()
    elif typ == 'Dark' or typ == 'Steel' or typ == 'Fairy':
        list2 = dex.show_type(list2, entry3.get(), "1")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def FindPoke():
    # Runs the Pokedex code to find and display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)        # Clears the text window
    list2 = dex.find(list2, entry4.get())  # Saves the data of the found pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)               # Displays the list in the text window


def FindPokeW():
    # Runs the Pokedex code to find and display Pokemon containing the entered characters
    global list2
    entry.delete("1.0", tkinter.END)            # Clears the text window
    list2 = dex.find_with(list2, entry5.get())  # Saves the data of the found pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)                   # Displays the list in the text window


def Clr():
    # Clearts the text window of any characters
    global list2
    list2 = list1
    entry.delete("1.0", tkinter.END)


# Runs code to save the pokedex in the CSV in the list
list1 = dex.define_list()
# Creates a copy and clears the list for global variable
list2 = list1.copy()
#list2.clear()
# Creates a global string
Poke = ""
# Creates the master window
window = tkinter.Tk()
# Titles the window
window.title("Pokedex")

# creates frame for display all pokemon and display evolution
listFrame = tkinter.Frame(window)
# Adds a label to the sorting frame
listL = tkinter.Label(listFrame, text='List:')
# First sortingFrame in listFrame to organize the buttons (Houses the List pokedex button)
listframeL = tkinter.Frame(listFrame)
# Second sortingFrame in listFrame to organize the buttons (Houses the display evolutions button)
listframeR = tkinter.Frame(listFrame)

# Creates first large sortingFrame to organize the buttons
sortingFrame = tkinter.Frame(window)
# Adds a label to the sorting frame
sorting = tkinter.Label(sortingFrame, text='Sorting Options:')
# First sortingFrame in sortingFrame to organize the buttons (Houses the List Numerically button)
sortingframeL = tkinter.Frame(sortingFrame)
# Second sortingFrame in sortingFrame to organize the buttons (Houses the List Alphabetically buttons)
sortingframeCL = tkinter.Frame(sortingFrame)
# Third sortingFrame in sortingFrame to organize the buttons (Houses the List by Weight Buttons)
sortingframeCR = tkinter.Frame(sortingFrame)
# Fourth sortingFrame in sortingFrame to organize the buttons (Houses the List by Height buttons)
sortingframeR = tkinter.Frame(sortingFrame)
# Creates a sortingFrame in sortingframeL to shift the button for a better look (Shifts the List Numerically button)
#frameleftE = tkinter.Frame(sortingframeL, height="0.2i")

# Creates second large sortingFrame to organize the buttons
searchingFrame = tkinter.Frame(window)
# adds label to the searching frame
search = tkinter.Label(searchingFrame, text='Searching Options:')
# First sortingFrame in searchingFrame to organize the buttons (Houses the List from Region button)
searchingframeL = tkinter.Frame(searchingFrame)
# Creates a sortingFrame in searchingframeL to shift the button for a better look (Shifts the List from Region button)
regionframeL = tkinter.Frame(searchingframeL, height="0.25i")
# Second sortingFrame in sortingFrame to organize the buttons (Houses the list by Type button)
searchingframeCL = tkinter.Frame(searchingFrame)
# Frame in searchingframeCL to organize the buttons (Houses the Type buttons and helps organize them neatly)
typeframeCL = tkinter.Frame(searchingframeCL)
# Third sortingFrame in sortingFrame to organize the buttons (Houses the find pokemon)
searchingframeCR = tkinter.Frame(searchingFrame)
# Fourth sortingFrame in sortingFrame to organize the buttons (Houses the find pokemon with)
searchingframeR = tkinter.Frame(searchingFrame)
# Creates a sortingFrame in searchingframeCR to shift the button for a better look(Houses the find pokemon)
findPokeframeCR = tkinter.Frame(searchingframeCR, height="0.5i")
# Creates a sortingFrame in searchingframeR to shift the button for a better look (Houses the find pokemon with)
findPokeWframeR = tkinter.Frame(searchingframeR, height="0.5i")

# a window to show the text of the pokemon
entry = tkinter.Text()
# creates scroll buttons for the text window
scroll = tkinter.Scrollbar(window, command=entry.yview)
# Sets the scroll buttons to scroll in the Y direction
entry['yscrollcommand'] = scroll.set

# Labels the window at the top as Pokedex
label = tkinter.Label(text="Pokedex")

# Creates a button named List Pokedex that runs the subroutine Display
dispP = tkinter.Button(listframeL, text="List Pokedex", command=DisplayBase)
# Creates a button named List Evolutions that runs the subroutine Display
dispE = tkinter.Button(listframeR, text="List Evolutions", command=DisplayEvolution)

# Creates a button named List Numerically that runs the subroutine Display
NumU = tkinter.Button(sortingframeL, text="List Numerically Lowest to Highest", command=DisplayNumU)
# Creates a button named List Numerically that runs the subroutine Display
NumD = tkinter.Button(sortingframeL, text="List Numerically Highest to Lowest", command=DisplayNumD)

# Creates a button named List Alphabetically Z-A that runs the subroutine DisplayAlphZ
alphZ = tkinter.Button(sortingframeCL, text="List Alphabetically Z-A", command=DisplayAlphZ)
# Creates a button named List Alphabetically A-Z that runs the subroutine DisplayAlphA
alphA = tkinter.Button(sortingframeCL, text="List Alphabetically A-Z", command=DisplayAlphA)

# Creates a button named List Height Shortest to Tallest that runs the subroutine DisplayHgtU
HgtU = tkinter.Button(sortingframeCR, text="List Height Shortest to Tallest", command=DisplayHgtU)
# Creates a button named List Height Tallest to Shortest that runs the subroutine DisplayHgtD
HgtD = tkinter.Button(sortingframeCR, text="List Height Tallest to Shortest", command=DisplayHgtD)

# Creates a button named List Weight Lightest to Heaviest that runs the subroutine DisplayWgtU
WgtU = tkinter.Button(sortingframeR, text="List Weight Lightest to Heaviest", command=DisplayWgtU)
# Creates a button named List Weight Heaviest to Lightest that runs the subroutine DisplayWgtD
WgtD = tkinter.Button(sortingframeR, text="List Weight Heaviest to Lightest", command=DisplayWgtD)

# Creates a button named clear that runs the Clr subroutine to clear the window
clrWind = tkinter.Button(window, text="Clear", command=Clr)

# Places the label Pokedex
label.pack()
# Places the data window
entry.pack()
# Places the scroll buttons
scroll.pack()
# Places the clear button
clrWind.pack()
# Places the List Numerically button
listFrame.pack(side='top', fill='both', expand=1)
listL.pack()
listframeL.pack(side='left', fill='both', expand=1)
listframeR.pack(side='right', fill='both', expand=1)
dispP.pack()
dispE.pack()


# Places the middle sortingFrame that containes 4 frames
sortingFrame.pack(side='top', fill='both', expand=1)
sorting.pack()
# Places the first of 4 frames in the middle sortingFrame
sortingframeL.pack(side='left', fill='both', expand=1)
# Places the second of 4 frames in the middle sortingFrame
sortingframeCL.pack(side='left', fill='both', expand=1)
# Places the third of 4 frames in the middle sortingFrame
sortingframeCR.pack(side='right', fill='both', expand=1)
# Places the fourth of 4 frames in the middle sortingFrame
sortingframeR.pack(side='right', fill='both', expand=1)

# Places the sortingFrame that spaces the List Numerically button
#frameleftE.pack()
# Places the List Numerically button
NumU.pack(padx=5, pady=5)
# Places the List Numerically button
NumD.pack(padx=5, pady=5)
# Places the List Alphabetically A-Z button
alphA.pack(padx=5, pady=5)
# Places the List Alphabetically Z-A button
alphZ.pack(padx=5, pady=5)
# Places the List Height shortest to tallest button
HgtU.pack(padx=5, pady=5)
# Places the List Height tallest to shortest button
HgtD.pack(padx=5, pady=5)
# Places the List Weight lightest to heaviest button
WgtU.pack(padx=5, pady=5)
# Places the List Weight heaviest to lightest button
WgtD.pack(padx=5, pady=5)

entry2 = tkinter.Entry(searchingframeL)
rgn1 = "Regions:" "\n" f"{'Kanto':<6} {'Johto':<6} {'Hoenn':<6}"\
       "\n" f"{'Sinnoh':<6} {'Unova':<6} {'Kalos':<6}"\
       "\n" f"{'Alola':<6} {'Galar':<6}"
label2 = tkinter.Label(searchingframeL, text=rgn1)
Rgn = tkinter.Button(searchingframeL, text="List Pokemon originally\nfrom in Selected Region", command=DisplayRegion)

entry3 = tkinter.Entry(searchingframeCL)
type1 = "Types of pokemon:" "\n" f"{'Normal':<9} {'Fire':<9} {'Water':<9} {'Grass':<9}"  "\n" \
       f"{'Electric':<9} {'Ice':<9} {'Fighting':<9} {'Poison':<9}" "\n"  f"{'Ground':<9} {'Flying':<9}" \
       f"{'Psychic':<9} {'Bug':<9}"  "\n" f"{'Rock':<9} {'Ghost':<9} {'Dragon':<9} {'Dark':<9}" \
        "\n" f" {'Steel':<9} {'Fairy':<9}"
label3 = tkinter.Label(searchingframeCL, text=type1)
typeframeCL.rowconfigure([0, 1], minsize=10, weight=1)
typeframeCL.columnconfigure([0, 1], minsize=10, weight=1)
Type = tkinter.Button(typeframeCL, text="Monotype", command=TypeM)
Type1 = tkinter.Button(typeframeCL, text="Primary", command=TypeP)
Type2 = tkinter.Button(typeframeCL, text="Secondary", command=TypeS)
Type3 = tkinter.Button(typeframeCL, text="Both", command=TypeB)

entry4 = tkinter.Entry(searchingframeCR)
Pokem = "Pokemon Name:"
label4 = tkinter.Label(searchingframeCR, text=Pokem)
Name = tkinter.Button(searchingframeCR, text="Find Pokemon", command=FindPoke)

entry5 = tkinter.Entry(searchingframeR)
PokemW = "Pokemon Contains:"
label5 = tkinter.Label(searchingframeR, text=PokemW)
NameW = tkinter.Button(searchingframeR, text="Find Pokemon Containing", command=FindPokeW)

searchingFrame.pack(side='bottom', fill='both', expand=1)
search.pack()
searchingframeL.pack(side='left', fill='both', expand=1)
searchingframeCL.pack(side='left', fill='both', expand=1)
searchingframeR.pack(side='right', fill='both', expand=1)
searchingframeCR.pack(side='right', fill='both', expand=1)

regionframeL.pack()
label2.pack()
entry2.pack(padx=4, pady=4)
Rgn.pack()

label3.pack()
entry3.pack(padx=2, pady=2)
typeframeCL.pack()
Type.grid(row=0, column=0, padx=2, pady=2)
Type1.grid(row=0, column=1, padx=2, pady=2)
Type2.grid(row=1, column=0, padx=2, pady=2)
Type3.grid(row=1, column=1, padx=2, pady=2)

findPokeframeCR.pack()
label4.pack()
entry4.pack(padx=4, pady=4)
Name.pack()

findPokeWframeR.pack()
label5.pack()
entry5.pack(padx=4, pady=4)
NameW.pack()

window.mainloop()
