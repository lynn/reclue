# reclue.py

A Python command-line tool for editing the clues of `.puz` format crosswords.

Requires [puzpy](https://github.com/alexdej/puzpy) by Alex Dejarnatt. (`pip install puzpy`)

## Usage

```bash
# Extract clues from a puzzle:
./reclue.py extract my.puz > clues.txt

# Edit them:
nano clues.txt

# Inject the edited clues:
./reclue.py inject my.puz clues.txt > reclued.puz
```
