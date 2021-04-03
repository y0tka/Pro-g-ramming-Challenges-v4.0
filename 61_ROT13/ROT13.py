alphablet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

input_string = input().upper()

for i in input_string:
    if i in alphablet:
        symbol_index = alphablet.index(i)
        converted_index = int((symbol_index+13-26*(symbol_index//13)))
        # What the fuck is happening here?
        # symbol_index+13 - index of the numer with rotation by 13 letters
        # -26*(symbol_index//13) - if the letter's index is lower then 13, just adds 13 to it
        # but if the index is more or equal to 13, substrtacts 13 to avoid IndexError
        
        print(alphablet[converted_index], end='')
    else:
        print(i, end='')
print("")