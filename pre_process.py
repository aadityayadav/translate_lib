# import ast
# import json
# from typing import Any

# class KeywordTranslator(ast.NodeTransformer):
#     def __init__(self, language_map):
#         self.language_map = language_map

#     def translate_keyword(self, value):
#         """Translate a single keyword if it's in the language map."""
#         return self.language_map.get(value, value)

#     def visit_Name(self, node: ast.Name) -> Any:
#         """Translate variable and function names if they match a keyword."""
#         if node.id in self.language_map:
#             return ast.copy_location(ast.Name(id=self.translate_keyword(node.id), ctx=node.ctx), node)
#         return node

#     def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
#         """Translate function names and their arguments."""
#         node.name = self.translate_keyword(node.name)
#         node.args.args = [ast.copy_location(ast.arg(arg=self.translate_keyword(arg.arg), annotation=arg.annotation), arg)
#                           for arg in node.args.args]
#         self.generic_visit(node)
#         return node

#     def visit_arg(self, node: ast.arg) -> Any:
#         """Translate function argument names."""
#         node.arg = self.translate_keyword(node.arg)
#         return node

#     def visit_Attribute(self, node: ast.Attribute) -> Any:
#         """Translate attributes if they match a keyword."""
#         node.attr = self.translate_keyword(node.attr)
#         return self.generic_visit(node)

#     def visit_Constant(self, node: ast.Constant) -> Any:
#         """Ensure constants, including strings, are not translated."""
#         if isinstance(node.value, str):
#             return node  # Skip string literals
#         return self.generic_visit(node)

#     def visit_Str(self, node: ast.Str) -> Any:  # For compatibility with older Python versions
#         """Ensure strings are not translated."""
#         return node

#     def visit_Call(self, node: ast.Call) -> Any:
#         """Translate function calls."""
#         node.func = self.visit(node.func)
#         node.args = [self.visit(arg) for arg in node.args]
#         node.keywords = [self.visit(kw) for kw in node.keywords]
#         return node

#     def visit_For(self, node: ast.For) -> Any:
#         """Translate for-loops with proper context."""
#         node.target = self.visit(node.target)
#         node.iter = self.visit(node.iter)
#         node.body = [self.visit(stmt) for stmt in node.body]
#         node.orelse = [self.visit(stmt) for stmt in node.orelse]
#         return node



# class PreProcessor:
#     def __init__(self, language_file):
#         self.language_map = self.load_language_map(language_file)

#     def load_language_map(self, language_file):
#         """Load the keyword mapping for the target language."""
#         try:
#             with open(language_file, 'r', encoding='utf-8') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             raise FileNotFoundError(f"Language file '{language_file}' not found.")

#     def preliminary_translate(self, code):
#         """Perform preliminary keyword translation to make the code parsable."""
#         for hindi_keyword, english_keyword in self.language_map.items():
#             code = code.replace(hindi_keyword, english_keyword)
#         return code

#     def translate_code(self, code):
#         """Translate the code using AST transformations."""
#         code = self.preliminary_translate(code)
#         tree = ast.parse(code)
#         translator = KeywordTranslator(self.language_map)
#         translated_tree = translator.visit(tree)
#         return ast.unparse(translated_tree)

#     def translate_file(self, input_file, output_file):
#         """Translate an entire file."""
#         with open(input_file, 'r', encoding='utf-8') as infile, \
#              open(output_file, 'w', encoding='utf-8') as outfile:
#             code = infile.read()
#             translated_code = self.translate_code(code)
#             outfile.write(translated_code)

#     def execute_translated_file(self, translated_file):
#         """Execute the translated Python file."""
#         with open(translated_file, 'r', encoding='utf-8') as file:
#             code = file.read()
#         exec(code, {})

# if __name__ == '__main__':
#     import argparse

#     parser = argparse.ArgumentParser(description="Multilingual Python Preprocessor")
#     parser.add_argument('command', choices=['translate', 'run'], help="Action to perform.")
#     parser.add_argument('input_file', help="Input file to process.")
#     parser.add_argument('-o', '--output', default='translated.py', help="Output file for the translated Python code.")
#     parser.add_argument('-l', '--language', default='hindi_to_english.json', help="Language mapping file (JSON).")

#     args = parser.parse_args()

#     preprocessor = PreProcessor(args.language)

#     if args.command == 'translate':
#         preprocessor.translate_file(args.input_file, args.output)
#         print(f"Translated file saved to {args.output}")

#     elif args.command == 'run':
#         preprocessor.translate_file(args.input_file, args.output)
#         print(f"Running translated code from {args.output}...")
#         preprocessor.execute_translated_file(args.output)



# the above solution is not working for strings properly, i believe creating a placeholder like the solution below might be the fix
# however, the solution below doesn't work either :')
import ast
import json
import re
import sys
import os
from typing import Dict, Tuple, List

class CodeTranslator:
    def __init__(self, language_map_file: str):
        self.language_map = self.load_language_map(language_map_file)
        # Create pattern for matching all keywords at once
        keywords_pattern = '|'.join(map(re.escape, sorted(self.language_map.keys(), key=len, reverse=True)))
        self.keywords_regex = re.compile(fr'\b({keywords_pattern})\b')

    def load_language_map(self, language_file: str) -> Dict[str, str]:
        """Load and validate the language mapping."""
        with open(language_file, 'r', encoding='utf-8') as file:
            mapping = json.load(file)
        return mapping

    def get_output_path(self, input_path: str) -> str:
        """Generate output path with _translated suffix."""
        base, ext = os.path.splitext(input_path)
        return f"{base}_translated{ext}"

    def extract_strings(self, code: str) -> Tuple[str, Dict[str, str]]:
        """Extract string literals and replace with placeholders."""
        strings = {}
        counter = 0

        def replace_string(match):
            nonlocal counter
            placeholder = f"__STRING_{counter}__"
            strings[placeholder] = match.group(0)
            counter += 1
            return placeholder

        # Match single/double quoted strings and triple quoted strings
        pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\''
        processed_code = re.sub(pattern, replace_string, code)
        return processed_code, strings

    def translate_tokens(self, line: str) -> str:
        """Translate all tokens in a line that match the language map."""
        def replace_keyword(match):
            keyword = match.group(0)
            return self.language_map.get(keyword, keyword)
            
        return self.keywords_regex.sub(replace_keyword, line)

    def translate_code(self, source_code: str, debug: bool = False) -> str:
        """Translate the code while preserving structure and string literals."""
        if debug:
            print("\nOriginal source code:")
            print(source_code)

        # Extract strings
        code_without_strings, string_map = self.extract_strings(source_code)
        
        if debug:
            print("\nCode with string placeholders:")
            print(code_without_strings)

        # Translate line by line
        lines = code_without_strings.split('\n')
        translated_lines = []
        
        for line in lines:
            # Preserve indentation
            indent = len(line) - len(line.lstrip())
            indentation = ' ' * indent
            content = line[indent:]
            
            # Translate the line content
            translated_content = self.translate_tokens(content)
            translated_lines.append(indentation + translated_content)

        # Join lines back together
        translated_code = '\n'.join(translated_lines)
        
        if debug:
            print("\nTranslated code with placeholders:")
            print(translated_code)

        # Restore string literals
        for placeholder, string in string_map.items():
            translated_code = translated_code.replace(placeholder, string)

        if debug:
            print("\nFinal translated code:")
            print(translated_code)

        # Verify the translation produces valid Python syntax
        try:
            ast.parse(translated_code)
        except SyntaxError as e:
            print(f"\nSyntax error in translated code:")
            print(translated_code)
            raise

        return translated_code

    def translate_file(self, input_file: str, output_file: str = None, debug: bool = False) -> str:
        """Translate a file and save the result."""
        try:
            # Read input file
            with open(input_file, 'r', encoding='utf-8') as f:
                source_code = f.read()

            # Translate the code
            translated_code = self.translate_code(source_code, debug)

            # Determine output path
            output_path = output_file or self.get_output_path(input_file)

            # Ensure output directory exists
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

            # Write translated code
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(translated_code)

            return translated_code

        except Exception as e:
            print(f"Error translating file: {str(e)}")
            raise

    def execute_translated_code(self, code: str) -> None:
        """Execute the translated Python code."""
        try:
            exec(code, {'__name__': '__main__'})
        except Exception as e:
            print(f"Error executing code: {str(e)}")
            raise

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Multilingual Python Translator")
    parser.add_argument('command', choices=['translate', 'run'], help="Action to perform")
    parser.add_argument('input_file', help="Input file to process")
    parser.add_argument('-o', '--output', help="Output file path (default: input_translated.py)")
    parser.add_argument('-m', '--mapping', required=True, help="Language mapping JSON file")
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug output")
    
    args = parser.parse_args()
    
    try:
        translator = CodeTranslator(args.mapping)
        
        if args.command == 'translate':
            output_path = args.output or translator.get_output_path(args.input_file)
            translated_code = translator.translate_file(args.input_file, output_path, args.debug)
            print(f"Successfully translated {args.input_file} to {output_path}")
            
        elif args.command == 'run':
            output_path = args.output or translator.get_output_path(args.input_file)
            translated_code = translator.translate_file(args.input_file, output_path, args.debug)
            print(f"Running translated code from {output_path}...")
            translator.execute_translated_code(translated_code)
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()