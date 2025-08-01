# NullInit: The Genesis Engine

**NullInit** is a powerful, opinionated project scaffolding tool designed for the discerning engineer. It eliminates the tedious boilerplate phase of development by instantly generating a complete, best-practice project structure from a set of curated templates.

With a single command, you can initialize a new project from "null"—a void of possibility—into a fully-formed, version-controlled foundation, ready for your next great innovation.

## Core Philosophy

- **Speed:** Move from idea to implementation in seconds.
- **Consistency:** Ensure every project starts with a standardized, logical, and clean structure.
- **Best Practices:** Embed industry-standard practices, such as `.gitignore` configurations and testing frameworks, from the very first commit.

## Usage

To scaffold a new project, execute the script from your terminal with the following command:

```bash
python nullinit.py --name <YourProjectName> --type <TemplateType>
```

### Arguments

-   `--name` (or `-n`): **Required.** The name of your new project directory.
-   `--type` (or `-t`): **Optional.** The type of template to use. Defaults to `python`.

## Available Templates

`NullInit` comes equipped with a suite of templates tailored for high-level development and research:

| Type | Description | Structure & Key Files |
| :--- | :--- | :--- |
| `python` | A standard, general-purpose Python application. | `src/main.py`, `tests/`, `pyproject.toml` |
| `fastapi` | A high-performance backend API using FastAPI. | `src/main.py`, `requirements.txt` (uvicorn, fastapi) |
| `llm-finetune` | A dedicated structure for fine-tuning Large Language Models. | `data/`, `models/`, `notebooks/`, `src/train.py` |
| `compiler` | A foundational structure for designing a new programming language. | `src/lexer/`, `src/parser/`, `src/codegen/` |
| `os` | A template for hobby operating system development. | `src/boot/boot.asm`, `src/kernel/kernel.c`, `build.bat` |

## Extending NullInit

The true power of `NullInit` lies in its potential for customization. The script is designed to be easily extended with new, user-defined project templates to perfectly match any workflow.

---

**By Coding NullInit , Setting Headlines for bigger project**