A simple command to toggle a panel. By default it toggles the build panel. Also known as `output.exec`.

Add something like this to your keybindings:

    // Well, that's ctrl+ä on german keyboards
    { "keys": ["ctrl+'"], "command": "toggle_panel",
                          "args": {"panel": "output.exec"}
    },
