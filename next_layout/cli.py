""" Module for switching keyboard layout
"""
import click
from xkbgroup import XKeyboard


def next_layout(xkb):
    """Switch to the next keyboard layout found by xkbgroup
    """
    if xkb.groups_count < 2:
        return  # nothing to do
    number = xkb.group_num
    new_number = (number + 1) % len(xkb.groups_data)
    xkb.group_num = new_number




@click.command()
def main():
    """Switch to the next keyboard layout"""
    xkb = XKeyboard()
    next_layout(xkb)
    print(xkb.group_name)
