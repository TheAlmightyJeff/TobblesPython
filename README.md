# Tobbles Python Collection <img src="https://github.com/TheAlmightyJeff/TobblesPython/blob/main/logo.png?raw=true" width="32">
A collection of all mine and some friends python stuff - please dont change and redistribute as your own!

## Better console

### Functions:
---

write(text, speed)

writes text to the console. look at 'styles' for customisation.

ask(text, speed)

sends a message box to be used as an input. e.g var = ask(...)

customise(bgCol="colour", title="window title", pauseAfterWrite="speed", font="font")

cutomises the window. colour can take a name or a hex value. pauseAfterWrite is how long betterConsole will wait before continuing with the next line of text. takes time in seconds.

**NEW: Fonts! Fonts can be assigned in the fonts.toml file and its very easy to define them yourself! The fonts must be valid with turtle and all dat.**

hold()

prevents the screen from closing after everything else has finished running. you dont always need it for some reason.

reset()

resets the console.

byebye()

exits better console.

wait()

Pauses untill it detects an enter key input.

REQUIRES TOMLLIB. IF THE MODULE IS NOT INSTALLED, FONT CHANGES WILL NOT BE AVAILABLE.

---

### Styles:
---
To use colours and styles, use @colour- or @style-

Colours: @red-, @orange-, @yellow-, @green-, @blue-, @pink-, @purple-, @white-, @grey-. 

Styles: @bold-, @italic-, @underline-, @normal-.

More can be added if you wish to customise more.

---

