from typing import List
from typing_extensions import Annotated

from rich.console import Console
import typer

import fruit_stand

app = typer.Typer()
console = Console()


@app.command()
def add_to_cart(fruits: Annotated[List[str], typer.Argument(help="'fruits:qty' to add to cart")]):
    """
    Description:
    Remove fruit from the inventory. Return the total cost of the order in USD.

    Example:
    $ python cli.py apples:2 oranges:3

    Note:
    Users should still be able to order the other fruits that are in stock.
    If there is not enough fruit in the inventory, the user will see an error message.
    """

    # Use the `fruit_stand.take_fruit` module to remove fruit from inventory.
    total = 0.00
    for fruit in fruits:
        try:
            fruit_name, qty = fruit.split(":")
            qty = int(qty)
            total += fruit_stand.take_fruit(fruit=fruit_name, qty=qty)
        except ValueError as ve:
            print(ve)
        except KeyError:
            print(f"I'm sorry. We don't have  {fruit_name} in stock.")
            # console.print(f"Invalid fruit format: {fruit}. Expected 'fruit:qty' where qty is a number.", style="red")

    # Print the total cost of the order in USD.
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    app()
