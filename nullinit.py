import argparse
import os
import subprocess

def create_directory_structure(base_path, structure):
    """Creates the directory structure for the project."""
    for path in structure:
        os.makedirs(os.path.join(base_path, path), exist_ok=True)
    print("Directory structure created.")

def create_boilerplate_files(base_path, files):
    """Creates boilerplate files for the project."""
    for file_path, content in files.items():
        with open(os.path.join(base_path, file_path), 'w') as f:
            f.write(content)
    print("Boilerplate files created.")

def initialize_git(base_path):
    """Initializes a git repository in the project directory."""
    try:
        subprocess.run(['git', 'init'], cwd=base_path, check=True, capture_output=True)
        print("Git repository initialized.")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Could not initialize Git repository: {e}")

def scaffold_project(name, project_type):
    """Scaffolds a new project based on the given name and type."""
    print(f"Scaffolding project: {name}")
    print(f"Project type: {project_type}")

    base_path = os.path.join(os.getcwd(), name)
    if os.path.exists(base_path):
        print(f"Error: Directory '{name}' already exists.")
        return

    os.makedirs(base_path)
    print(f"Created project directory: {base_path}")

    # --- Define Project Structures ---
    common_files = {
        'README.md': f'# {name}\n\nA new project.\n',
        '.gitignore': '# Ignore Python artifacts\n__pycache__/\n*.pyc\n\n# Ignore OS-specific files\n.DS_Store\n\n# Ignore temporary files\ncommit_message.txt\n\n# Ignore environment variables\n.env\n'
    }

    # Python Template
    python_structure = ['src', 'tests']
    python_files = {
        'src/main.py': 'def main():\n    print("Hello, World!")\n\nif __name__ == "__main__":\n    main()\n',
        'tests/test_main.py': 'import unittest\n\nclass TestMain(unittest.TestCase):\n    def test_example(self):\n        self.assertEqual(1, 1)\n\nif __name__ == "__main__":\n    unittest.main()\n',
        'pyproject.toml': f'[project]\nname = "{name}"\nversion = "0.1.0"\n'
    }
    python_files.update(common_files)

    # FastAPI Template
    fastapi_structure = ['src', 'tests']
    fastapi_files = {
        'src/main.py': 'from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/")\ndef read_root():\n    return {"Hello": "World"}\n',
        'requirements.txt': 'fastapi\nuvicorn[standard]\n',
    }
    fastapi_files.update(common_files)

    # LLM Finetune Template
    llm_finetune_structure = ['data', 'models', 'notebooks', 'src']
    llm_finetune_files = {
        'src/train.py': 'import torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nprint("Ready to train!")\n',
        'src/evaluate.py': 'import torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nprint("Ready to evaluate!")\n',
        'notebooks/01_data_exploration.ipynb': '{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 2\n}',
        'data/.gitkeep': '',
        'models/.gitkeep': '',
        'requirements.txt': 'torch\ntransformers\ndatasets\naccelerate\n',
        '.gitignore': common_files['.gitignore'] + '\n# Ignore large data and model files\ndata/*\nmodels/*\n'
    }
    llm_finetune_files.update(common_files)


    # Compiler Template
    compiler_structure = ['src/lexer', 'src/parser', 'src/codegen', 'tests']
    compiler_files = {
        'src/main.py': 'def main():\n    print("Compiler entry point.")\n\nif __name__ == "__main__":\n    main()\n',
        'src/lexer/lexer.py': '# Lexer implementation\n',
        'src/parser/parser.py': '# Parser implementation\n',
        'src/codegen/codegen.py': '# Code generator implementation\n',
        'pyproject.toml': f'[project]\nname = "{name}"\nversion = "0.1.0"\n'
    }
    compiler_files.update(common_files)

    # OS Template
    os_structure = ['src/boot', 'src/kernel', 'build']
    os_files = {
        'src/boot/boot.asm': "; A simple bootloader\n\norg 0x7c00\nbits 16\n\nstart:\n    mov si, msg\n    call print_string\n\njmp $\n\nprint_string:\n    mov ah, 0x0e ; tty mode\n.loop:\n    lodsb\n    cmp al, 0\n    je .done\n    int 0x10\n    jmp .loop\n.done:\n    ret\n\nmsg db 'Hello, World!', 0\n\ntimes 510 - ($ - $$) db 0\ndw 0xaa55\n",
        'src/kernel/kernel.c': '// A simple C kernel\n\nvoid main() {\n    // Your kernel code here\n    while(1);\n}',
        'build.bat': 'nasm -f bin src/boot/boot.asm -o build/boot.bin\nrem Add commands to compile C kernel and link here\necho "Build complete. (Kernel not included in image yet)"\ncopy build\\boot.bin build\\os.img\n',
        '.gitignore': '*.bin\n*.img\nbuild/*\n'
    }
    os_files.update(common_files)


    # --- Scaffolding Logic ---
    if project_type == 'python':
        create_directory_structure(base_path, python_structure)
        create_boilerplate_files(base_path, python_files)
    elif project_type == 'fastapi':
        create_directory_structure(base_path, fastapi_structure)
        create_boilerplate_files(base_path, fastapi_files)
    elif project_type == 'llm-finetune':
        create_directory_structure(base_path, llm_finetune_structure)
        create_boilerplate_files(base_path, llm_finetune_files)
    elif project_type == 'compiler':
        create_directory_structure(base_path, compiler_structure)
        create_boilerplate_files(base_path, compiler_files)
    elif project_type == 'os':
        create_directory_structure(base_path, os_structure)
        create_boilerplate_files(base_path, os_files)
    else:
        print(f"Project type '{project_type}' is not yet supported.")
        # For now, just create common files for unsupported types
        create_boilerplate_files(base_path, common_files)


    initialize_git(base_path)
    print(f"\nProject '{name}' scaffolded successfully at: {base_path}")
    print("You can start by running: cd " + name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project Scaffolder Tool')
    parser.add_argument('-n', '--name', type=str, required=True, help='The name of the project.')
    parser.add_argument('-t', '--type', type=str, default='python', help='The type of the project (e.g., python, fastapi, react).')

    args = parser.parse_args()
    scaffold_project(args.name, args.type)