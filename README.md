# Introduction
This Python package allows users to code Python in their native language. The package then translates the syntax and keywords into English, allowing the code to be run as normal. 

**Supported Python Features:** 
- Keywords: Control flow (`if`, `else`, `for`, `while`, etc.), function definitions, class definitions, etc.
- Basic Libraries: `math`, `random`, `os`, `time`.
- Basic Syntax: Variables, loops, conditionals, functions, classes, and imports.

# Purpose and Scope
The goal of this project is to enable beginners to learn Python programming in their native language. By being able to use Python syntax and keywords in a more familiar language, learners can focus on understanding programming concepts without being hindered by unfamiliar English terms. This approach ensures that learners can build foundational programming skills before transitioning to English-based Python coding.

**Key Objectives:**

1. Provide a tool to translate Python code from a native language syntax to standard English-based Python.
2. Simplify the learning curve for beginners by removing the language barrier.
3. Support a gradual transition to English-based programming, preparing learners for real-world coding environments.

**This project is designed for:**
1. **Absolute beginners:** By removing the language barrier, we aim to introduce Python as a language, and coding in general, to a wider, non-English speaking population. 
2. **Educational Settings:** We can enable instructors to teach Python in their native language, perhaps in a bootcamp setting.


# Using the CLI tool
The pre_processor.py script includes a command-line interface (CLI) that allows users to translate Python files or directories written in a native language to English-based Python syntax. Below are the available commands and their usage.

## 1. Command syntax:
```
python pre_process.py <command> <input_path> [options]
```
- `<command>`: The action to perform (e.g., translate, run, etc.).
- `<input_path>`: The file or directory to process.
- `[options]`: Additional arguments (e.g., output path, language file, main file).

## 2. Available commands:
a. `translate `: Translates a single Python file from the source language to English and saves it to an output file.
- Usage:
```
python pre_process.py translate <input_file> -o <output_file> -l <language_file>
```
- Example:
```
python pre_process.py translate my_script.py -o translated_script.py -l hindi_to_english.json
```
**Options**:
- `-o`: Path to the output file (default: translated.py).
- `-l`: Path to the language mapping JSON file (default: hindi_to_english.json).
---
b. `run`: Translates a single Python file, saves it to an output file and then executes the translated code.
- Usage:
```
python pre_process.py run <input_file> -o <output_file> -l <language_file>
```
- Example:
```
python pre_process.py run my_script.py -o translated_script.py -l hindi_to_english.json
```
---
c.  `run_direct`: Translates and executes a Python file **without** saving the translated file. 
- Usage:
```
python pre_process.py run_direct <input_file> -l <language_file>
```
- Example:
```
python pre_process.py run_direct my_script.py -l hindi_to_english.json
```
---
d.  `translate_dir`: Translates all Python files in a directory and its subdirectories, saving the results in a new output directory.
- Usage:
```
python pre_process.py translate_dir <input_dir> -o <output_dir> -l <language_file> -m <main_file>
```
- Example:
```
python pre_process.py translate_dir my_project -o translate_project -l hindi_to_english.json -m main.py
```
- Options:
- `-o`: Path to the output directory (default: translated_dir).
- `-l`: Path to the language mapping JSON file (default: hindi_to_english.json).
---
e. `run_dir`: Translates all Python files in a directory and then executes a specified main file from the translated directory. Note: Does not save a translated directory. 
- Usage:
```
python pre_process.py run_dir <input_dir> -l <language_file> -m <main_file>
```
- Example:
```
python pre_process.py run_dir my_project -l hindi_to_english.json -m main.py
```
- Options:

- `-l`: Path to the language mapping JSON file (default: hindi_to_english.json).
- `-m`: Name of the main file to execute after translation (required).

# Documentation for `pre_process.py` 

# Limitations and how you can help


