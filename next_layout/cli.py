""" Module for switching keyboard layout
"""
import click
from xkbgroup import XKeyboard


def next_layout():
    """Switch to the next keyboard layout found by xkbgroup
    """
    xkb = XKeyboard()
    if xkb.groups_count < 2:
        return  # nothing to do
    symbol_index = xkb.groups_symbols.index(xkb.group_symbol)
    xkb.group_symbol = xkb.groups_symbols[(symbol_index + 1) % len(
        xkb.groups_symbols)]


@click.command()
def main():
    """Switch to the next keyboard layout"""
    next_layout()
