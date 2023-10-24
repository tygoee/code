from os import get_terminal_size
from typing import Collection, Generator, Any


def bar(iterator: Collection[Any],
        bar_length: int | None = None
        ) -> Generator[Any, Any, None]:
    """
    Displays a simple progress bar. Example usage:

    ```python
    my_list = list(range(10))
    for i in bar(my_list)
        do_something()
    ```

    :param iterator: The iterator used by the for loop
    :param bar_length: The bar length (default: terminal width)
    """

    # Assign or correct bar_length
    max_terminal_width = get_terminal_size().columns - 8

    if bar_length == None:
        bar_length = max_terminal_width
    elif bar_length >= max_terminal_width:
        bar_length = max_terminal_width

    for idx, item in enumerate(iterator):
        # Calculate progress
        progress, status = round(idx / len(iterator) * 100, 0), ''
        if progress >= 100:
            progress, status = 100, '\r\n'

        block = int(round(bar_length / 100 * progress))

        # Print the loading bar
        print("\r{:3.0f}% [{}]{}".format(
            progress, '#' * block + ' ' * (bar_length - block), status
        ), end='')

        yield item
