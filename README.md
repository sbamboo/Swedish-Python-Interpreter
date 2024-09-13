# Orm, an interpreter for swedish python
An alternative python interpreter that accepts swedish keywords
## Usage
    python Orm.py test.orm
or

    ./Orm test.orm
    
## Example
![grafik](https://github.com/actopozipc/German-Python-Interpreter/assets/48481041/93bd66c2-1b2d-477d-8943-dc95d7ecc92f)

## Supported keywords and functions
### Keywords

| Englisch     | Swedish      |
| ------------ | ------------ |
| `and`        | `och` |
| `as`         | `som` |
| `assert`     | `kontrollera` |
| `async`      | `asynk` |
| `await`      | `vänta` |
| `break`      | `bryt` |
| `class`      | `Klass` |
| `continue`   | `fortsätt` |
| `def`        | `def` |
| `del`        | `radera` |
| `elif`       | `ifall` |
| `else`       | `annars` |
| `except`     | `men` |
| `False`      | `Falskt` |
| `finally`    | `slutligen` |
| `for`        | `för` |
| `from`       | `från` |
| `global`     | `global` |
| `if`         | `om` |
| `import`     | `importera` |
| `in`         | `innuti` |
| `is`         | `är` |
| `lambda`     | `lambda` |
| `None`       | `Inget` |
| `nonlocal`   | `ickelokal` |
| `not`        | `inte` |
| `or`         | `eller` |
| `pass`       | `passera` |
| `raise`      | `res` |
| `return`     | `returera` |
| `True`       | `Sant` |
| `try`        | `försök` |
| `while`      | `sålänge` |
| `with`       | `med` |
| `yield`      | `ge` |

### Exceptions
| Englisch | Swedish |
| --- | --- |
| `Exception` | `Undantag` |
| `TypeError` | `TypFel` |
| `ValueError` | `VärdeFel` |
| `NameError` | `NamnFel` |
| `IndexError` | `IndexFel` |
| `KeyError` | `NyckelFel` |
| `FileNotFoundError` | `FilEjFunnenFel` |
| `SyntaxError` | `SyntaxFel` |
| `IndentationError` | `FramskutningsFel` |
| `ImportError` | `ImporteringsFel` |
| `ModuleNotFoundError` | `ModulenEjFunnenFel` |
| `ZeroDivisionError` | `NollDivitionsFel` |
| `ArithmeticError` | `AritmetisktFel` |
| `OverflowError` | `ÖverflödsFel` |
| `AssertionError` | `KontrolleringsFel` |
| `AttributeError` | `AttributFel` |
| `RuntimeError` | `ExekveringsFel` |
| `KeyboardInterrupt` | `TangentbordsAvbrott` |
| `StopIteration` | `IterationsAvslut` |
| `PermissionError` | `TillståndsFel` |

### Built-in Functions
| Englisch      | Swedish      |
|--------------|--------------|
| all          | alla         |
| any          | vadsom    |
| breakpoint   | brytpunkt   |
| callable     | anropningsbar    |
| compile      | kompilera   |
| complex      | komplex      |
| delattr      | raderaattr    |
| enumerate    | uppräkning (missing)   |
| getattr      | fåattr  |
| globals      | globala      |
| hasattr      | harattr      |
| help         | hjälp        |
| input        | inmatning      |
| isinstance   | ärinstans   |
| issubclass   | ärsubklass |
| len          | längd          |
| list         | lista        |
| locals       | lokala       |
| map          | karta        |
| next         | nästa     |
| object       | objekt       |
| open         | öppna        |
| property     | egenskap  |
| range        | räckvidd   |
| reversed     | bakvänt    |
| round        | runda        |
| setattr      | sättattr     |
| sorted       | sorterad     |
| staticmethod | statiskmetod |
| slice        | dela (missing)        |
| tuple        | tupel        |
| type         | typ          |
| print        | printa       |
| math         | matte        |
| sqrt         | kvadratröttera       |



## TODO
* Intellisense support
* More function names (numpy, matplotlib)
* Adding missing translations (enumerate, slice)
* More swedish keywords (see original project discussions for german version)
