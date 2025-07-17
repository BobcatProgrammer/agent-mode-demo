# Agent Mode Demo - Calculator

This is a simple calculator app running in CLI. It supports basic arithmetic operations like addition, subtraction, multiplication, and division. It works by parsing user input and performing the requested operation.

## 🚀 Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division

## 🛠️ Usage

Each operation is now its own command. Run the application as follows:

```sh
python calculator.py add 5 3
# Result: 8
python calculator.py subtract 10 4
# Result: 6
python calculator.py multiply 2 3
# Result: 6
python calculator.py divide 8 2
# Result: 4.0
```

## 🧪 Running Tests

```sh
python -m unittest test_calculator.py
```

## 🧩 Technology Stack

- Python 3.x
- [Typer](https://typer.tiangolo.com/) for CLI
- Unit tests to verify
- Easy to use CLI interface

## 💡 Prompts to try

### Division by Zero Handling

```
I want to update our calculator.py so that the divide function handles division by zero gracefully (by returning None instead of raising an exception). Also, update the corresponding unit test in test_calculator.py to check this new behavior.
```

### Find all TODOs

```md
Check the codebase for any todos and get them done.
```

### Create a makefile

```md
I want to create a Makefile for this project that includes targets for running the application, running tests, and cleaning up temporary files.
```

### Add a new operation

```md
I want to add a new operation to our calculator.py that calculates the modulus of two numbers. Update the CLI to support this operation and add a corresponding unit test in test_calculator.py. Update docs```

### Updates

```md
Setup a github action workflow that runs the tests and linters on every pr. Enable Dependabot and pin the typer version to latest stable release. Update the README to reflect these changes.
```

## Local Development

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Create a virtual environment (recommended):

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:

   ```sh
   python calculator.py calculate add 5 3
   ```

5. Run tests:

   ```sh
   python -m unittest test_calculator.py
   ```  

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
