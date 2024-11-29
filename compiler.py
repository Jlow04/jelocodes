'''
Compiler for Our Litle Language (.huh)
'''
import sys
program_filepath = sys.argv[1]

print("[CDM] Parsing")
###############################################
# tokenize program
###############################################

# Read file lines
program_lines = []
with open(program_filepath, 'r') as program_file:
    program_lines = [
        line.strip() 
            for line in program_file.readlines()]
    
program = []
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check for empty lines
    if opcode == "":
        continue

    #store the opcode tokens
    program.append(opcode)

    # handle each opcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
    elif opcode == "PRINT":
        #parse string literal
        string_literal = '  '.join(parts[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0":
        #read label
        label = parts[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        #read label
        label = parts[1]
        program.append(label)

'''
Compile to assembly
'''

asm_filepath = program_filepath[:-4] + ".asm"
out = open(asm_filepath, 'w')

out.write("""; -- header --
          bits 64
          deafult rel
          """)

out.write("""; -- variables --
          section.bss
          """)

out.write("""; -- contants --
          section.data
          """)

out.write("""; -- Entry Point --
          section.text
          global main
          extern ExitProcess
          extern printf
          extern scanf


          main:
          \tPUSH rbp
          \tMOV rbp,rsp
          \tSUB rsp,32
          """)

ip = 0
while ip < len(program):
    opcode = program[ip]
    ip += 1

    if opcode.endswith(":"):
        out.write(f"; -- Label ---\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip += 1

        out.write(f"; -- PUSH {number} --\n")
        out.write(f"\tPUSH {number}\n")
    elif opcode == "POP":
        out.write(f"; -- POP --\n")
        out.write(f"\tPOP\n")
    elif opcode == "ADD":
        out.write(f"; -- ADD --\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tADD qword[rsp], rax\n")
    elif opcode == "SUB":
        out.write(f"; -- SUB --\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tSUB qword [rsp], rax\n")

out.close()


          