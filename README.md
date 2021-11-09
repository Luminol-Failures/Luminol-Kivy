# Luminol
Luminol is a family of editors designed to open source RPG Maker XP's editor. You are currently looking at Luminol-Kivy, the main version of Luminol, written in Python and made with Kivy. [Luminol-FXRuby](https://github.com/Speak2Erase/Luminol-FXRuby), the secondary version of Luminol, is a "fork" of Luminol written in ruby and made with FXRuby.

## Why kivy?
Kivy is fairly simple to use, however it has a good looking aand smooth GUI and allows you to perform more complex operations using it. We heavily rely on these to render maps properly.
#

Luminol is intended to be used with **mkxp**. It may not work with the standard game.exe.
(You really should if you're trying to push RPG Maker XP to its limits!)
If you are modding OneShot, you do NOT need to worry about this as OneShot uses mkxp.

## Dependencies

Luminol uses:

- [Kivy](https://pypi.org/project/Kivy/) for its GUI.
- [Pillow](https://pypi.org/project/Pillow/) for rendering maps and sprites.
- [Ruby Marshal Module](https://pypi.org/project/rubymarshal/) for loading .rxdata. *(integrated into Luminol)*
- [NumPy](https://pypi.org/project/numpy/) for speedy array manipulation.
- [Cython](https://pypi.org/project/cython) for compiling code into C extensions.

## Installation

The installation process *mostly* follows the [Kivy installation docs](https://kivy.org/doc/stable/gettingstarted/installation.html).

For starters, you will need to have Python (3.7-3.9) and pip installed.

1. In a new terminal, ensure you have the latest versions of pip, setuptools & virtualenv.  
`python -m pip install --upgrade pip setuptools virtualenv`

2. Clone Luminol (somewhere.)  
`git clone https://github.com/Speak2Erase/Luminol/` (https)  
or  
`git clone git@github.com:Speak2Erase/Luminol` (ssh)  

3. CD into wherever you cloned Luminol and setup the virtual environment.  
`python -m virtualenv kivy_venv`

4. Activate virtual enviornment. You will also need to do this every time you run Luminol.  
`.\kivy_venv\Scripts\activate`  (Windows)  
`source kivy_venv/bin/activate` (Linux)

5. Install requirements.  
`python -m pip install -r requirements.txt`

To Launch Luminol, make sure you have first activated the virtual enviornment using  
`.\kivy_venv\Scripts\activate`  (Windows)  
`source kivy_venv/bin/activate` (Linux)

Then, run `python main.py`

## Usage

There are 2 ways to load mkxp projects in Luminol: Locally or Externally.  
### Locally

This mode requires you to have the `Data` and `Graphics` folders inside the root folder of Luminol.  

### Externally 
This mode allows you to open mkxp projects from folders other than the root folder of Luminol.  
To use this mode, you must specify the directory as an arguement when running `main.py`  
`python main.py "C:/Games/OneShot"` for example.
