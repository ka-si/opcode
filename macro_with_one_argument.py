def expand_macro(code, macro):
    macro_lines = []
    macro_name = ' '
    code_lines = []
    arg_list = []
    macro_call_count = 0

    for line in macro:
        line = line.upper().strip()
        if line == 'MACRO':
            continue
        elif line == 'MEND':
            break
        else:
            macro_lines.append(line)
    macro_name = macro_lines[0].split()[0]
    macro_lines.pop(0)

    def call_macro(arg):
        return [line.replace('&ARG', arg) for line in macro_lines]

    for line in code:
        line = line.strip()
        parts = line.split()
        if parts[0].upper() == macro_name:

            macro_call_count += 1
            arg = parts[1]
            arg_list.append(arg)
            code_lines.extend(call_macro(arg))
        else:
            code_lines.append(line)

    return code_lines, macro_call_count, arg_list, len(macro_lines)


def main():

    print("Enter the input code line by line. Enter 'END' on a new line when finished.")
    code_input = []
    while True:
        line = input().strip()
        if line == 'END':
            break
        code_input.append(line)

    print("\nEnter the macro definition line by line. Enter 'END' on a new line when finished.")
    macro_input = []
    while True:
        line = input().strip()
        if line == 'END':
            break
        macro_input.append(line)

    expanded_code, macro_call_count, arg_list, macro_instruction_count = expand_macro(code_input, macro_input)

    print("\nEvaluated Program:")
    for line in expanded_code:
        print(line)

    print("\nStatistical Output:")
    code_instruction_count = len(code_input) - macro_call_count
    print("Number of instructions in input source code (excluding Macro calls) =", code_instruction_count)
    print("Number of Macro calls =", macro_call_count)
    print("Number of instructions defined in the Macro call =", macro_instruction_count)
    for i, arg in enumerate(arg_list):
        print(f"Actual argument during Macro call {i + 1} =", arg)
    print("Total number of instructions in the expanded source code =", len(expanded_code))


if __name__ == "__main__":
    main()

# Input -
# Enter the input code line by line. Enter 'END' on a new line when finished.
# MOV R
# RAHUL 30
# DCR R
# AND R
# RAHUL 55
# MUL 88
# HALT
# END

# Enter the macro definition line by line. Enter 'END' on a new line when finished.
# MACRO
# RAHUL &ARG
# ADD &ARG
# SUB &ARG
# OR &ARG
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
