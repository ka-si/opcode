from sys import exit

motOpCode = {
    "MOV"   : 1,
    "A"     : 2,
    "S"     : 3,
    "M"     : 4,
    "D"     : 5,
    "AN"    : 6,
    "O"     : 7,
    "ADD"   : 8,
    "SUB"   : 9,
    "MUL"   : 10,
    "DIV"   : 11,
    "AND"   : 12,
    "OR"    : 13,
    "LOAD"  : 14,
    "STORE" : 15,
    "DCR"   : 16,
    "INC"   : 17,
    "JMP"   : 18,
    "JNZ"   : 19,
    "HALT"  : 20
}

motSize = {
    "MOV"   : 1,
    "A"     : 1,
    "S"     : 1,
    "M"     : 1,
    "D"     : 1,
    "AN"    : 1,
    "O"     : 1,
    "ADD"   : 1,
    "SUB"   : 2,
    "MUL"   : 2,
    "DIV"   : 2,
    "AND"   : 2,
    "OR"    : 2,
    "LOAD"  : 3,
    "STORE" : 3,
    "DCR"   : 1,
    "INC"   : 1,
    "JMP"   : 3,
    "JNZ"   : 3,
    "HALT"  : 1
}

l = []
relativeAddress = []
machineCode = []
RA = 0
current = 0
count = 0

while True:
    instructions = input("Enter instruction line (type 'done' when finished): ")
    if instructions.lower() == 'done':
        break
    l.append(instructions)

l = [x.upper() for x in l]

for i in range(len(l)):
    x = l[i]
    if " " in x:
        s1 = x.split(maxsplit=1)
        a = s1[0]
        if len(s1) > 1:
            b = s1[1]
        else:
            b = ""

        if a in motOpCode:
            value = motOpCode.get(a)
            size = motSize.get(a)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            if b.isalpha():
                machineCode.append(str(value))
            else:
                temp = list(b)
                for i in range(len(temp)):
                    if count == 2:
                        temp.insert(i, ' ')
                        count = 0
                    else:
                        count += 1
                s = ''.join(temp)
                machineCode.append(str(value) + " " + s)

        else:
            print("Instruction is not in Op Code Table.")
            exit(0)

    else:
        if x in motOpCode:
            value = motOpCode.get(x)
            size = motSize.get(x)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            machineCode.append(value)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)

print("+------------------+---------------+--------------+")
print("| Relative Address | Instruction   | Machine Code |")
print("+------------------+---------------+--------------+")
for i in range(len(l)):
    if " " in str(machineCode[i]):
        mc_bytes = machineCode[i].split()
        machine_code_str = ", ".join(mc_bytes)
    else:
        machine_code_str = machineCode[i]

    print("|{:<18}|{:<15}|{:<14}|".format(relativeAddress[i], l[i], machine_code_str))
print("+------------------+---------------+--------------+")

# Input -
# Enter instruction line (type 'done' when finished): MOV R
# Enter instruction line (type 'done' when finished): ADD R
# Enter instruction line (type 'done' when finished): SUB 30
# Enter instruction line (type 'done' when finished): STORE 1000
# Enter instruction line (type 'done' when finished): HALT
# Enter instruction line (type 'done' when finished): done

"""
Assembler: Assembler accepts ALP as input & produces its machine language equivalent 
along with other information for the loader (like externally defined symbols).

Pass-1 Algorithm:
1.Initialize Location Counter LC = 0.
2.Read card pointed by LC.
3.Search POT for particular Pseudo-op –
a)If DC or DS, then update LC to proper value, Goto step 5.
b)If EQU, then evaluate operand field & assign value to the label field, Go to step 7.
c)If USING or DROP, then Goto step 7.
d)If END, then assign storage for literals, rewind & reset copy.
Go to Pass-2.
4.Search MOT –
a)Obtain instruction length L from MOT.
b)Process literals (if present) & enter them to LTSTO.
5.If instruction has label, then assign value of LC to symbol in STSTO.
6.Update LC i.e. LC = LC + L.
7.Write copy of card on file for use by Pass - 2.
Go to step 2

Functions of Pass-1 of the Assembler:
1.Determine length of machine instructions. (MOTGET1)
2.Keep track of Location Counter. (LC)
3.Remember values of symbols until Pass-2. (STSTO)
4.Process some pseudo-ops like DS, DC. (POTGET1)
5.Remember literals. (LITSTO)
In brief, Pass-1 defines symbols & literals
"""





