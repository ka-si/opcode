print("Enter the input source code (one line per instruction, type 'END' to finish):")
input_code = []
while True:
    line = input().strip()
    if line.upper() == 'END':
        break
    input_code.append(line)

print("Enter the macro definition (one line per instruction, type 'END' to finish):")
macro_definition = []
while True:
    line = input().strip().upper()
    if line.upper() == 'END':
        break
    macro_definition.append(line)

if 'MACRO' not in macro_definition:
    print("Error: 'MACRO' keyword not found in the macro definition.")
else:
    macro_start_index = macro_definition.index('MACRO')
    macro_name = macro_definition[macro_start_index + 1]
    macro_end_index = macro_definition.index('MEND')
    macro_body = macro_definition[macro_start_index + 2:macro_end_index]

    macro_count = 0
    expanded_code = []
    for instruction in input_code:
        if instruction == macro_name:
            expanded_code.extend(macro_body)
            macro_count += 1
        else:
            expanded_code.append(instruction)

    print("\nExpanded Source Code:")
    for instruction in expanded_code:
        print(instruction)

    print("\n\nStatistical Output")
    print("Number of instructions in input source code (excluding Macro calls) =", len(input_code) - macro_count)
    print("Number of Macro calls =", macro_count)
    print("Number of instructions defined in the Macro call =", len(macro_body))
    print("Total number of instructions in the expanded source code =", len(expanded_code))

# Input -
# Enter the input source code (one line per instruction, type 'END' to finish):
# MOV R
# RAHUL
# DCR R
# AND R
# RAHUL
# MUL 88
# HALT
# END
# Enter the macro definition (one line per instruction, type 'END' to finish):
# MACRO
# RAHUL
# ADD 30
# SUB 25
# OR R
# MEND
# END


"""
Macro: It is a single line abbreviation for the group of instructions.
1)Macro is defined for the block of instructions at the beginning if the Assembly Language Program (ALP).
2)Reduces the size of the ALP significantly and storage space.
3)In source ALP code, each occurrence of that block of instructions is represented by its macro.
4)Before the assembly process i.e. generating object code, the macro is expanded by the Macro Processor.
5)Macro expansion is the process of replacing each macro call by its block of instructions.

Need of Macros:
Sometimes it is needed to repeat block of instructions many numbers of times in ALP.
For example:
a)Save or exchange set of registers.
b)Series of arithmetic operations.
Macro is defined for such block of instructions.

Generalized format of the macro:
MACRO		; start of macro definition
{macro name}	; name of the macro
------------------}
------------------}	; block of instructions
------------------} 	(body/domain of the macro)
MEND	 	; end of macro definition

"""