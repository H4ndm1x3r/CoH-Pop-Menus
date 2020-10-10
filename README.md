# Semi-Customizable Pop-Menus

So you find yourself interested in some Pop-Menus for City of Heroes. Well, you've come to the right place! Enjoy using existing, well-functioning pop-menus customized to fit your needs with personalized details.

**@Handmixer** presents:  **Semi-Customizable Pop-Menus!**

Currently supports (Reunion) Hamidon Raids, planned to be extended to Itrials and Mothership Raids in the near future.
<br>

## Installation

1) Download the **[latest release](https://github.com/H4ndm1x3r/CoH-Popmenus/releases)**

2) Navigate to your City of Heroes installation folder.

3) Extract or drag the contents of the downloaded zip-file into your City of Heroes installation folder.

4) Verify that the files have been correctly installed by locating your Menus folder `data -> Texts -> English -> Menus`
<br>

### External

1) Ensure that you have **[Python installed](https://www.python.org/downloads/)**
<br>

### First Time Use

1) The first time you use a pop-menu will be manually by typing `/popmenu [TITLE]` in-game.

2) From the list you can select "Make Macro", which will bind the pop-menu to your configured button when pressed.
    * NOTE: Currently all pop-menus will be bound to the same button, so you will need to use the macros to switch active pop-menu.
<br>

## Configuration
Before you are able to properly use these Pop-Menus you need to configure your settings.
To do this, locate **config.json** file inside the templates folder.

1) Open **config.json** in your preferred text editor.

2) Modify the available variables to fit you.

3) Save the file once finished.

4) Finally, return to the Menus folder and run **apply-config.py**. Several new files should appear in the folder.
<br>

## Configurable Variables
Currently all variables will be used. Future changes will include implementation for optional variables.
```
 ### GLOBAL_NAME ----- Your ingame global name (without the @)
 ### DISCORD_LINK ---- Provide a permanent invitation link to your Discord Server
 ### DISCORD_SERVER -- The name of your Discord server (e.g. Hounds of Love)
 ### BIND_BUTTON ----- Add the button you would like the pop-menus to be bound to
```