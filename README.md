# Cinema Management

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A command-line cinema management system written in pure Python. The program reads a script of commands from an input file, simulates hall creation, ticket sales, cancellations, seat-layout rendering, and a per-hall revenue report.

Built as a file-manipulation exercise using only the Python standard library — no external dependencies.

## Features

- **Multiple halls** with arbitrary `rows × columns` dimensions
- **Ticket sales** for two customer types (`student`, `full`) at different prices
- **Single-seat and range purchases** — `B3` or `C2-10`
- **Seat cancellation** with validation (cannot cancel an already-free seat)
- **ASCII hall layout** rendering — rows labelled `A`, `B`, `C` … from bottom up
- **Revenue report** per hall (`student × 5 + full × 10`)
- **Robust error handling** for unknown halls, duplicate hall names, out-of-range seats, double-bookings

## Tech Stack

- **Language**: Python 3.6+
- **Modules used**: `sys`, `string` (stdlib only)

## Command Reference

| Command | Syntax | Effect |
|---------|--------|--------|
| `CREATEHALL` | `CREATEHALL <name> <rows>x<cols>` | Create a new hall of given dimensions |
| `SELLTICKET` | `SELLTICKET <customer> <student\|full> <hall> <seat...>` | Sell one or more seats to a customer |
| `CANCELTICKET` | `CANCELTICKET <hall> <seat...>` | Free up one or more seats in a hall |
| `SHOWHALL` | `SHOWHALL <hall>` | Print the ASCII seat layout |
| `BALANCE` | `BALANCE <hall>` | Print the revenue report for a hall |

Seat notation: row letter + column number (`B3`) or a range (`C2-10` = columns 2–9 on row C).

Pricing: `student` = 5, `full` = 10.

## Project Structure

```
.
├── main.py                  # CLI entry point — parses commands and dispatches
├── Commands.py              # Command implementations (createHall, sellTicket, ...)
├── input.txt                # Sample command script
├── out.txt                  # Expected output for input.txt
├── Cinema-Management.pdf    # Original assignment specification
├── requirements.txt
├── LICENSE
└── README.md
```

## Installation

```bash
git clone https://github.com/Msubasi1/Cinema-Management.git
cd Cinema-Management
```

No external dependencies are required. A Python 3.6+ interpreter is sufficient.

## Usage

```bash
python main.py input.txt
```

To compare against the bundled expected output:

```bash
python main.py input.txt > my_out.txt
diff out.txt my_out.txt
```

### Example input

```
CREATEHALL bluehall 15x15
CREATEHALL redhall 20x20
SELLTICKET ayse student bluehall B3 B4 C2-10
SELLTICKET nermin full bluehall C9-12
SHOWHALL bluehall
BALANCE bluehall
```

### Example output

```
Hall 'bluehall' having 225 seats has been created
Hall 'redhall' having 400 seats has been created
Success: ayse has bought B3 at bluehall
Success: ayse has bought B4 at bluehall
Success: ayse has bought C2-10 at bluehall
Warning: The seats C9-12 cannot be sold to nermin due some of them have already been sold
Printing hall layout of bluehall
... (15×15 seat map)
Hall report of 'bluehall'
-------------------------
Sum of students = 50, Sum of full fares = 0, Overall = 50
```

## Author

**Muhammet Subaşı** ([@Msubasi1](https://github.com/Msubasi1))

## License

Released under the [MIT License](LICENSE).
