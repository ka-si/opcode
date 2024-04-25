def expand_macro(source_code, macro_definitions):
    expanded_code = []
    macro_calls = 0
    total_instructions = 0

    for line in source_code:
        if line.strip() in macro_definitions:
            macro_calls += 1
            macro_body = macro_definitions[line.strip()]
            expanded_code.extend(macro_body)
            total_instructions += len(macro_body)
        else:
            expanded_code.append(line)
            total_instructions += 1

    return expanded_code, macro_calls, total_instructions

def main():
    # Input source code with Macro calls
    input_source_code = [
        "MOV R",
        "RAHUL",
        "DCR R",
        "AND R",
        "RAHUL",
        "MUL 88",
        "HALT"
    ]

    # Macro definitions
    macro_definitions = {
        "RAHUL": [
            "ADD 30",
            "SUB 25",
            "OR R"
        ]
    }

    # Expansion
    expanded_source_code, macro_calls, total_instructions = expand_macro(input_source_code, macro_definitions)

    # Output expanded source code
    print("Output source code after Macro expansion:")
    for line in expanded_source_code:
        print(line)

    # Output statistical information
    print("\nStatistical output:")
    print("Number of instructions in input source code (excluding Macro calls):", len(input_source_code) - macro_calls)
    print("Number of Macro calls:", macro_calls)
    print("Number of instructions defined in the Macro call:", len(macro_definitions["RAHUL"]))
    print("Total number of instructions in the expanded source code =", total_instructions)

if __name__ == "__main__":
    main()

