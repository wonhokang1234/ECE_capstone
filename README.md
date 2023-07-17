# myflection
### 18-500 Project ###

- test.js has codes for 1) enabling text enabling, 2) retrieving the dominant color, 3) logging the result to output.txt
- test images: Solid_black.png, white.png, image-2.4461c1c0.jpg(from colorthief web example)
- fixed a bug from the original API of unable to determine white as a dominant color(./dist, ./src)
- need to operate within node_modules/colorthief directory


export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
