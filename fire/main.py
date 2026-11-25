from rich import print as rprint
from rich.console import Console, OverflowMethod
from time import sleep as s
from typing import List
from rich.theme import Theme
import sys


custom_theme = Theme({
    "fuel": "white"
})

console = Console(theme=custom_theme)

y = False
x = 0
while y == True:
    if x == 0:
        replacer = "white"
    else:
        replacer = "red"
    console.print(
        f"[{replacer}]{str(x) * console.width}[/{replacer}]"
        )





o = False
def calc ():
    max_x = 40
    max_y = 20
    max_z = 10
    x = 0
    y = 0
    z = 0
    while o == False:
        while x <= y and x <= max_x:
            x += 1
        while y < z and y < max_y:
            y += 1
        
        if z < max_z:
            z += 1
        print(x, y, z)

print(1 + 1)

heat_theme = Theme({
    "fuel": "white",
    "high_heat": "bright_yellow",
    "medium_heat": "sandy_brown",
    "strong_heat": "dark_orange",
    "weak_heat": "red",
    "fade_heat": "bright_red"
})

console = Console(theme=heat_theme, highlight=False)
max_x = 6
x = 0
Style = ""
while True:
    if x < max_x:

        x += 1
        s(0.05)

        if x >= max_x:
            x = 0
    if x <= 0:
        Style = "fuel"
    if x >= 1:
        Style = "high_heat"
    if x >= 2:
        Style = "medium_heat"
    if x >= 3:
        Style = "strong_heat"
    if x >= 4:
        Style = "weak_heat"
    if x >= 5:
        Style = "fade_heat"  
    
    console.print(f"{x} "* console.width,style=f"{(Style)}")
    