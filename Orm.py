import argparse
import re
import os
import sys
import importlib
import types

class KeywordTranslator:
    translations = {
        'och': 'and',
        'som': 'as',
        'kontrollera': 'assert',
        'asynk': 'async',
        'vänta': 'await',
        'bryt': 'break',
        'Klass': 'class',
        'fortsätt': 'continue',
        'def': 'def',
        'radera': 'del',
        'ifall': 'elif',
        'annars': 'else',
        'men': 'except',
        'Falskt': 'False',
        'slutligen': 'finally',
        'för': 'for',
        'från': 'from',
        'global': 'global',
        'om': 'if',
        'importera': 'import',
        'innuti': 'in',
        'är': 'is',
        'lambda': 'lambda',
        'Inget': 'None',
        'ickelokal': 'nonlocal',
        'inte': 'not',
        'eller': 'or',
        'passera': 'pass',
        'res': 'raise',
        'returera': 'return',
        'Sant': 'True',
        'försök': 'try',
        'sålänge': 'while',
        'med': 'with',
        'ge': 'yield',
        "själv": "self"
    }

    translation_exceptions = {
        'Undantag': 'Exception',
        'TypFel': 'TypeError',
        'VärdeFel': 'ValueError',
        'NamnFel': 'NameError',
        'IndexFel': 'IndexError',
        'NyckelFel': 'KeyError',
        'SyntaxFel': 'SyntaxError',
        'FramskutningsFel': 'IndentationError',
        'FilEjFunnenFel': 'FileNotFoundError',
        'NollDivitionsFel': 'ZeroDivisionError',
        'ÖverflödsFel': 'OverflowError',
        'ImporteringsFel': 'ImportError',
        'ModulenEjFunnenFel': 'ModuleNotFoundError',
        'AttributFel': 'AttributeError',
        'KontrolleringsFel': 'AssertionError',
        'ExekveringsFel': 'RuntimeError',
        'IterationsAvslut': 'StopIteration',
        'TangentbordsAvbrott': 'KeyboardInterrupt',
    }

    translation_functions = {
        "alla": "all",
        "vadsom": "any",
        "brytpunkt": "breakpoint",
        "anropningsbar": "callable",
        "kompilera": "compile",
        "komplex": "complex",
        "raderaattr": "delattr",
        "uppräkning": "enumerate",
        "fåattr": "getattr",
        "globala": "globals",
        "harattr": "hasattr",
        "hjälp": "help",
        "inmatning": "input",
        "ärinstans": "isinstance",
        "ärsubklass": "issubclass",
        "längd": "len",
        "lista": "list",
        "lokala": "locals",
        "karta": "map",
        "nästa": "next",
        'objekt': 'object',
        "öppna": "open",
        "egenskap": "property",
        "räckvidd": "range",
        "bakvänt": "reversed",
        "runda": "round",
        "sättattr": "setattr",
        "sorterad": "sorted",
        "statiskmetod": "staticmethod",
        "dela": "slice",
        "tupel": "tuple",
        "typ": "type",
        "printa": "print",
        "matte": "math",
        "kvadratröttera": "sqrt"
    }

    exception_translations = dict((val, key) for key, val in translation_exceptions.items())
    
    errors_with_placeholders = {
        'unsupported operand type': 'icke stödd operandtyp',
        'division by zero': 'division med noll',
        'name \'{}\' is not defined': 'namnet \'{}\' är inte definierat',
        'list index out of range': 'listindex utanför giltigt område',
        'tuple index out of range': 'tupelindex utanför giltigt område',
        'invalid syntax': 'ogiltig syntax',
        'indentation error': 'indenteringsfel',
        'file not found': 'filen ej funnen',
        'attribute \'{}\' not found': 'attributet \'{}\' ej funnen',
        'module \'{}\' not found': 'modulen \'{}\' ej funnen',
        'division or modulo by zero': 'division eller modulo med noll',
        'key error': 'nyckelfel',
        'invalid literal for int() with base {}: \'{}\'': 'ogiltigt värde för int() med bas {}: \'{}\'',
        'unexpected indent': 'oväntad indentering',
        'not a valid identifier': 'inte ett giltigt identifierare',
        'invalid syntax, unexpected {}: \'{}\'': 'ogiltig syntax, oväntad {}: \'{}\'',
        'unsupported operand type(s) for {}: \'{}\' and \'{}\'': 'icke stödda operandtyper för {}: \'{}\' och \'{}\'',
        'No module named \'{}\' ' : 'ingen modul med namnet \'{}\'' 
    }

    errors_without_placeholders = {
        'unsupported operand type': 'icke stödd operandtyp',
        'division by zero': 'division med noll',
        'name \'\' is not defined': 'namnet \'\' är inte definierat',
        'list index out of range': 'listindex utanför giltigt område',
        'tuple index out of range': 'tupelindex utanför giltigt område',
        'invalid syntax': 'ogiltig syntax',
        'indentation error': 'indenteringsfel',
        'file not found': 'filen ej funnen',
        'attribute \'\' not found': 'attributet \'\' ej funnen',
        'module \'\' not found': 'modulen \'\' ej funnen',
        'division or modulo by zero': 'division eller modulo med noll',
        'key error': 'nyckelfel',
        'invalid literal for int() with base {}: \'\'': 'ogiltigt värde för int() med bas {}: \'\'',
        'unexpected indent': 'oväntad indentering',
        'not a valid identifier': 'inte ett giltigt identifierare',
        'invalid syntax, unexpected {}: \'\'': 'ogiltig syntax, oväntad {}: \'\'',
        'unsupported operand type(s) for {}: \'\' and \'\'': 'icke stödda operandtyper för {}: \'\' och \'\'',
        'No module named \'{}\' ' : 'ingen modul med namnet \'{}\'' 
    }

    def extract_operators(self, error_message):
        pattern = r'\'(.*?)\'|//?|/'
        operators = re.findall(pattern, error_message)
        operators = [op for op in operators if op != '']
        return operators

    def remove_operators(self, string, operators):
        for operator in operators:
            pattern = re.escape(operator)
            string = re.sub(pattern, '', string)
        return string

    def translate_exception(self, exception):
        exception_type = type(exception).__name__
        translated_type = self.exception_translations.get(str(exception_type), str(exception_type))
        translated_output = None
        for trans in self.errors_with_placeholders:
            try:
                operators = self.extract_operators(str(exception))
                t = trans.format(*self.extract_operators(str(exception)))
                if t == str(exception):
                    e = self.remove_operators(t, operators)
                    translated_output = self.errors_without_placeholders.get(e)
                    for op in operators:
                        translated_output = translated_output.replace("''", op)
                    break
            except Exception:
                translated_output = self.errors_with_placeholders.get(str(exception))
        
        if translated_output is None:
            translated_output = str(exception)
        return translated_output

    def __init__(self, file_path):
        self.file_path = file_path
        self.module_registry = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            self.code = f.read()

    def split_formmated(self, code: str) -> str:
        string_pattern = re.compile(r'(f)(\"(.*?)\"|\'(.*?)\')')
        any_formatted_pattern = re.compile(r'{(.*?)}')

        strings = string_pattern.findall(code)
        original_strings = [string[1] for string in strings]

        for i, string in enumerate(strings):
            content = string[1]
            format_indicator = string[0]
            quark_type = content[0]

            if format_indicator:
                formatted = any_formatted_pattern.findall(content)
                formatted_fitted = [
                    f'{quark_type} + str({i}) + {quark_type}' for i in formatted]
                
                for original, fitted in zip(formatted, formatted_fitted):
                    content = content.replace(f"{{{original}}}", fitted)

            strings[i] = content

        for original, replaced in zip(original_strings, strings):
            code = code.replace(original, replaced)

        return code

    def convert(self):
        """ Översätt koden till Python """
        pattern = re.compile(r'\b(' + '|'.join(self.translations.keys()) + r')\b')
        pattern_exc = re.compile(r'\b(' + '|'.join(self.translation_exceptions.keys()) + r')\b')
        pattern_func = re.compile(r'\b(' + '|'.join(self.translation_functions.keys()) + r')\b')
        self.code = self.split_formmated(self.code)
        self.code = pattern.sub(lambda x: self.translations[x.group()], self.code)
        self.code = pattern_exc.sub(lambda x: self.translation_exceptions[x.group()], self.code)
        self.code = pattern_func.sub(lambda x: self.translation_functions[x.group()], self.code)

    def write_output(self):
        """ Skriv ut den översatta koden till en ny fil """
        new_file_path = self.file_path.replace(".py", "_translated.py")
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(self.code)
        print(f"Den översatta koden är sparad till: {new_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Översätt Python-kod med svenska nyckelord till standard Python.")
    parser.add_argument('fil', help="Sökväg till Python-filen att översätta.")
    args = parser.parse_args()

    translator = KeywordTranslator(args.fil)
    translator.convert()
    translator.write_output()

    try:
        with open(args.fil, 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code, globals())
    except Exception as e:
        translator = KeywordTranslator(args.fil)
        print(f"Fel upptäckt: {translator.translate_exception(e)}")
