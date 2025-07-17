import typer

app = typer.Typer()

def _add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@app.command()
def add(a: float, b: float):
    """Add two numbers."""
    typer.echo(f"Result: {_add(a, b)}")

def _subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@app.command()
def subtract(a: float, b: float):
    """Subtract b from a."""
    typer.echo(f"Result: {_subtract(a, b)}")

def _multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@app.command()
def multiply(a: float, b: float):
    """Multiply two numbers."""
    typer.echo(f"Result: {_multiply(a, b)}")

def _divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b

@app.command()
def divide(a: float, b: float):
    """Divide a by b."""
    typer.echo(f"Result: {_divide(a, b)}")

if __name__ == "__main__":
    app()

# TODO: Add exponentiation operation
