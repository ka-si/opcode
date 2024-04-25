def main():
    input_source = "MOV RIA\nRAHUL 30, 40, 50\nIOCR R\nAND RAHUL 33, 44, 55\nMUL 88\nHALT"
    macro_definition = "MACRO RAHUL &ARG1, &ARG2, &ARG3\nADD &ARG1\nSUB &ARG2\nOR &ARG3\nMEND"

    # Parse input source code and macro definition
    source_code_instructions = input_source.split("\n")
    macro_instructions = macro_definition.split("\n")

    # Extract macro name and arguments from macro definition
    macro_name = macro_instructions[0].split()[1]
    macro_arguments = macro_instructions[1].split()[1:]

    # Perform macro expansion
    expanded_source_code = []
    macro_calls = 0
    macro_instructions_count = 0
    actual_arguments = []

    for instruction in source_code_instructions:
        if instruction.startswith(macro_name):
            # Macro call found
            macro_calls += 1
            arguments = instruction[instruction.index(" ") + 1:].split(", ")
            actual_arguments.append(arguments)

            # Expand macro
            for macro_instruction in macro_instructions[2:]:
                for i, arg in enumerate(macro_arguments):
                    macro_instruction = macro_instruction.replace("&" + arg, arguments[i])
                expanded_source_code.append(macro_instruction)
                macro_instructions_count += 1
        else:
            # Non-macro instruction, add as it is
            expanded_source_code.append(instruction)

    # Calculate statistics
    total_instructions = len(source_code_instructions) - macro_calls * macro_instructions_count

    # Output expanded source code
    print("Output source code after Macro expansion:")
    for instruction in expanded_source_code:
        print(instruction)

    # Output statistics
    print("\nStatistical output:")
    print("Number of instructions in input source code (excluding Macro calls):", total_instructions)
    print("Number of Macro calls:", macro_calls)
    print("Number of instructions defined in the Macro call:", macro_instructions_count)
    for i in range(macro_calls):
        print("Actual argument during Macro call \"" + macro_name + "\":", actual_arguments[i])
    print("Total number of instructions in the expanded source code:", total_instructions)


if __name__ == "__main__":
    main()

