#!/usr/bin/env python3
import puz
import sys

def usage():
    sys.exit(f'''Usage:

    # Extract clues from a puzzle:
    ./reclue.py extract my.puz > clues.txt
    
    # Edit them:
    nano clues.txt
    
    # Inject the edited clues:
    ./reclue.py inject my.puz clues.txt > reclued.puz
''')

def clue_output(p):
    """
    Yield the lines of an editable clue file.
    """
    numbering = p.clue_numbering()
    yield 'Across:'
    for c in numbering.across:
        answer = ''.join(p.solution[c['cell']+i] for i in range(c['len']))
        print(f"{c['num']}. {answer} = {c['clue']}")
    yield ''
    yield 'Down:'
    w = numbering.width
    for c in numbering.down:
        answer = ''.join(p.solution[c['cell']+i*w] for i in range(c['len']))
        print(f"{c['num']}. {answer} = {c['clue']}")

def read_clues(f):
    """
    Read an editable clue file into (clue num, line num, clue) tuples.
    (Sorting the resulting sequence puts the clues in .puz order:
    ascending clue number, with Across before Down as a tie-breaker.)
    """
    for i, line in enumerate(f):
        if ' = ' in line:
            num = int(line.split('.')[0])
            clue = line.strip().split(' = ')[-1]
            yield (num, i, clue)

def main(argv):
    if len(argv) <= 2: usage()
    command = argv[1]
    if command == 'extract':
        if len(argv) != 3: usage()
        p = puz.read(argv[2])
        for line in clue_output(p):
            print(line)
    elif command == 'inject':
        if len(argv) != 4: usage()
        p = puz.read(argv[2])
        with open(argv[3]) as f:
            p.clues = [c for i, j, c in sorted(read_clues(f))]
        sys.stdout.buffer.write(p.tobytes())
    else: usage()

if __name__ == '__main__':
    main(sys.argv)
