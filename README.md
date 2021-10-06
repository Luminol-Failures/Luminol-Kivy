# Luminol
Luminol is an open sourced version of the RPG Maker XP editor created in Python.
Luminol's goal is to fully unlock RPG Maker XP by no longer limiting you with the editor.

Luminol is intended to be used with **mkxp**. It may not work with the standard game.exe.
(You really should if you're trying to push RPG Maker XP to its limits!)
If you are modding OneShot, you do NOT need to worry about this as OneShot uses mkxp.

## Dependencies
Luminol is using:
- [Kivy](https://pypi.org/project/Kivy/) for Innovative User Interface.
- [Python Imaging Library](https://pypi.org/project/Pillow/) for render Tilesets, Event sprites and more.
- [Ruby Marshal Module](https://pypi.org/project/rubymarshal/) for parsing Ruby Marshalled objects and more. *(integrated into Luminol)*
- [NumPy](https://pypi.org/project/numpy/) for array computing.

## Installation
For install Python dependencies:
```
$ pip install -Ur requirements.txt
```