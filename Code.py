#STEP 1: Created dictionaries to store the corresponding 6 digit opcode or func code for the different operations

#dictionary for R type triadic instructions
dict_R_Tri = {
  'ADD': 0b000000,
  'SUB': 0b000001,
  'AND': 0b000010,
  'OR': 0b000011,
  'XOR': 0b000100,
  'SLL': 0b000101,
  'SRL': 0b000110,
  'SRA': 0b000111,
  'ROL': 0b001000,
  'ROR': 0b001001,
  'SLT': 0b001010,
  'SGT': 0b001011,
  'SLE': 0b001100,
  'SGE': 0b001101,
  'UGT': 0b001110,
  'ULT': 0b001111,
  'ULE': 0b010000,
  'UGE': 0b010001
}

#dictionary for RI type tryadic instructions except load and store
dict_RI_Tri = {
  'ADDI': 0b100000,
  'SUBI': 0b100001,
  'ANDI': 0b100010,
  'ORI': 0b100011,
  'XORI': 0b100100,
  'SLLI': 0b100101,
  'SRLI': 0b100110,
  'SRAI': 0b100111,
  'SLTI': 0b101010,
  'SGTI': 0b101011,
  'SLEI': 0b101100,
  'SGEI': 0b101101,
  'UGTI': 0b101110,
  'ULTI': 0b101111,
  'ULEI': 0b110000,
  'UGEI': 0b110001,
  'LHI': 0b110010
}

#dictionary for RI type (load and store) instructions
dict_RI_Tri_LS = {
  'LB': 0b110011,
  'LBU': 0b110100,
  'LH': 0b110101,
  'LHU': 0b110110,
  'LW': 0b110111,
  'SB': 0b111000,
  'SH': 0b111001,
  'SW': 0b111010
}

#dictionary for R type diadic instructions
dict_R_Di = {
  'BNE': 0b111100,
  'BEQ': 0b111101,
  'JR': 0b111110,
  'JALR': 0b111111
}

#dictionary for J type instructions
dict_J = {'J': 0b010100, 'JAL': 0b010111}

#STEP 2: To take the inputs(assembly code) in different lines, storing them in a list, and storing the corresponding line number of each code

inputlist = []
inputdict = {}
n = 1
while True:
  try:
    line = input().split()
    if ":" in line[0]:
      inputdict[line[0][:len(line[0]) - 1]] = n
    n += 1
  except EOFError:
    break
  inputlist.append(line)

#General Instruction Format: ADD R1 R2 R3 --> R3 = R1 + R2
#STEP 3: To convert the assembly code into binary code

for i in inputlist:
  o = inputlist.index(i) + 1

  if i[0].upper() in dict_R_Tri.keys():  #R triadic
    opcode = format(dict_R_Tri[i[0].upper()], '06b')
    rs1 = format(int(i[1][1:]), '05b')
    rs2 = format(int(i[2][1:]), '05b')
    rd = format(int(i[3][1:]), '05b')
    IR = '000000' + str(rs1) + str(rs2) + str(rd) + '00000' + str(opcode)
    print(IR, i[0])

  elif i[0].upper() in dict_RI_Tri.keys():  #RI Triadic
    opcode = format(dict_RI_Tri[i[0].upper()], '06b')
    rs1 = format(int(i[1][1:]), '05b')
    imm = format(int(i[2][1:]), '016b')
    if (int(i[2][1:])) < 0:
      imm = format(2**16 + int(i[2][1:]), '016b')
    else:
      imm = format(int(i[2][1:]), '016b')
    rd = format(int(i[3][1:]), '05b')
    IR = str(opcode) + str(rs1) + str(rd) + str(imm)
    print(IR, i[0])

  elif i[0].upper() in dict_RI_Tri_LS.keys():  # RI Triadic Load Store
    opcode = format(dict_RI_Tri_LS[i[0].upper()], '06b')
    n1 = i[1].rindex("(")
    n2 = i[1].rindex(")")
    rs1 = format(int(i[1][n1 + 2:n2]), '05b')
    if (int(i[1][:n1])) < 0:
      imm = format(2**16 + int(i[1][:n1]), '016b')
    else:
      imm = format(int(i[1][:n1]), '016b')
    rd = format(int(i[2][1:]), '05b')
    IR = str(opcode) + str(rs1) + str(rd) + str(imm)
    print(IR, i[0])

  elif i[0].upper() in dict_R_Di.keys():  #RI Diadic
    opcode = format(dict_R_Di[i[0].upper()], '06b')
    rs1 = format(int(i[1][1:]), '05b')
    rs2 = format(int(i[2][1:]), '05b')
    if (inputdict[i[3]] - o - 1) < 0:
      offset = format(2**16 + (inputdict[i[3]] - o - 1), '016b')
    else:
      offset = format(inputdict[i[3]] - o - 1, '016b')
    IR = str(opcode) + str(rs1) + str(rs2) + str(offset)
    print(IR, i[0])

  elif i[0].upper() in dict_J.keys():  #Jump Instruction
    opcode = format(dict_J[i[0].upper()], '06b')
    if (inputdict[i[1]] - o - 1) < 0:
      offset = format(2**26 + (inputdict[i[1]] - o - 1), '026b')
    else:
      offset = format(inputdict[i[1]] - o - 1, '026b')
    IR = str(opcode) + str(offset)
    print(IR, i[0])

  else:
    inputdict[i[0][:len(i[0]) - 1]] = o

    if i[1].upper() in dict_R_Tri.keys():  #R triadic
      opcode = format(dict_R_Tri[i[1].upper()], '06b')
      rs1 = format(int(i[2][1:]), '05b')
      rs2 = format(int(i[3][1:]), '05b')
      rd = format(int(i[4][1:]), '05b')
      IR = '000000'+ str(rs1) + str(rs2) + str(rd) + '00000' + str(opcode)
      print(IR, i[0][:len(i[0]) - 1])

    elif i[1].upper() in dict_RI_Tri.keys():  #RI Triadic
      opcode = format(dict_RI_Tri[i[1].upper()], '06b')
      rs1 = format(int(i[2][1:]), '05b')
      if (int(i[3][1:])) < 0:
        imm = format(2**16 + int(i[3][1:]), '016b')
      else:
        imm = format(int(i[3][1:]), '016b')
      rd = format(int(i[4][1:]), '05b')
      IR = str(opcode) + str(rs1) + str(rd) + str(imm)
      print(IR, i[0][:len(i[0]) - 1])

    elif i[1].upper() in dict_RI_Tri_LS.keys():  # RI Triadic Load Store
      opcode = format(dict_RI_Tri_LS[i[1].upper()], '06b')
      n1 = i[2].rindex("(")
      n2 = i[2].rindex(")")
      rs1 = format(int(i[2][n1 + 2:n2]), '05b')
      if (int(i[1][:n1])) < 0:
        imm = format(2**16 + int(i[1][:n1]), '016b')
      else:
        imm = format(int(i[1][:n1]), '016b')
      rd = format(int(i[3][1:]), '05b')
      IR = str(opcode) + str(rs1) + str(rd) + str(imm)
      print(IR, i[0][:len(i[0]) - 1])

    elif i[1].upper() in dict_R_Di.keys():  #RI Diadic
      opcode = format(dict_R_Di[i[1].upper()], '06b')
      rs1 = format(int(i[2][1:]), '05b')
      rs2 = format(int(i[3][1:]), '05b')
      if inputdict[i[4]] - o - 1 < 0:
        offset = format(2**16 + (inputdict[i[4]] - o - 1), '016b')
      else:
        offset = format(inputdict[i[4]] - o - 1, '016b')
      IR = str(opcode) + str(rs1) + str(rs2) + str(offset)
      print(IR, i[0][:len(i[0]) - 1])

    elif i[1].upper() in dict_J.keys():  #Jump Instruction
      opcode = format(dict_J[i[1].upper()], '06b')
      if (inputdict[i[2]] - o - 1) < 0:
        offset = format(2**26 + (inputdict[i[2]] - o - 1), '026b')
      else:
        offset = format(inputdict[i[2]] - o - 1, '026b')
      IR = str(opcode) + str(offset)
      print(IR, i[0][:len(i[0]) - 1])
