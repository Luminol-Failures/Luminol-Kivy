# Luminol
Luminol is an open sourced version of the RPG Maker XP editor created in Python.
Luminol's goal is to fully unlock RPG Maker XP by no longer limiting you with the editor.

Luminol is intended to be used with **mkxp**. It may not work with the standard game.exe.
(You really should if you're trying to push RPG Maker XP to its limits!)
If you are modding OneShot, you do NOT need to worry about this as OneShot uses mkxp.

# Dependencies
Luminol uses:
- [Kivy](https://pypi.org/project/Kivy/) for its GUI.
- [Python Imaging Library](https://pypi.org/project/Pillow/) for rendering maps and sprites.
- [Ruby Marshal Module](https://pypi.org/project/rubymarshal/) for loading .rxdata. *(integrated into Luminol)*
- [NumPy](https://pypi.org/project/numpy/) for speedy array manipulation.

# Installation
The installation process *mostly* follows the kivy installation docs. (https://kivy.org/doc/stable/gettingstarted/installation.html)

For starters, you will need to have Python (3.7-3.9) and pip installed. 

1. In a new terminal, update pip.

`pip install pip --upgrade`

2. Clone Luminol (somewhere.)

`git clone git@github.com:Speak2Erase/Luminol` (ssh) `git clone https://github.com/Speak2Erase/Luminol/` (normal)

3. CD into wherever you cloned Luminol and setup the virtual environment.

`python -m virtualenv kivy_venv`

Every time you want to launch Luminol you will need to activate the virtual environment.

4. `.\kivy_venv\Scripts\activate` (windows) `source kivy_venv/bin/activate` (linux)

5. Install kivy.

`python -m pip install kivy[full]`

6. Launch Luminol!

`python main.py`
