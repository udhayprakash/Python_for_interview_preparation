ADD = 1
SUB = 2
JMP = 5
END = 86

"""
  Executes a program, which modifies a VALUE. The program is an array of bytes,
  representing a series of instructions. Each instruction is composed of consecutive
  two-byte pairs. In each instruction, the first byte is the COMMAND, and the second
  byte is the OPERAND. Instructions are executed in order until an END instruction
  runs.  At that point, the updated VALUE is returned.

  The following byte values represent supported COMMANDs:
  1 (ADD).  Add the OPERAND to the current VALUE.
  2 (SUB).  Subtract the OPERAND from the current VALUE.
  5 (JMP).  Skip execution of the next N instructions, based on the OPERAND.
  86 (END).  Terminate the program; return the current VALUE.

  Example:
  runProgram(3, bytes([ 1, 8, 2, 4, 5, 1, 2, 95, 86, 0 ]));
  Walking through the logic...
  The starting value is 3.
  The first instruction is ADD 8. 3+8=11.  The value is now 11.
  The second instruction is SUB 4.  11-4, the value is 7.
  The third instruction is JMP 1.  The next instruction is skipped.
  The final instruction is END.  The function returns 7.

  startingValue: Initial VALUE
  program: Program data
  returns The value after the program has run<
"""


def runProgram(startingValue: int, program: bytes) -> int:
    if not (isinstance(startingValue, int) and isinstance(program, bytes)):
        raise Exception(f"Invalid input data")
    if len(program) % 2 != 0:
        raise Exception(f"Invalid program instructions: {program}")
    if not program:
        return startingValue
    if program[-2] != 86:
        raise Exception(f"Missing  END instruction: {program}")
    value = startingValue
    i, skipCount = 0, 0
    while i < len(program) - 2:
        op, val = program[i], program[i + 1]
        i += 2
        if skipCount != 0:
            skipCount -= 1
            continue
        if op == 1:
            value += val
        elif op == 2:
            value -= val
        elif op == 5:
            if val < 0:
                raise Exception(f"Invalid skipCount: {skipCount}")
            skipCount = val if val > 0 else 0
            continue
        elif op == 86:
            return value
        else:
            raise Exception(f"Invalid operand: {op}")
    if skipCount != 0:
        raise Exception(f"Pending SkipCounts")
    return value


if __name__ == "__main__":
    result = runProgram(3, bytes([1, 8, 2, 4, 5, 1, 2, 95, 86, 0]))
    print(f"Result: {result}, Expected 7")
