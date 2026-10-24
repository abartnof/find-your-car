# Find Your Car

🎮 **Play live**: [https://abartnof.github.io/find-your-car/](https://abartnof.github.io/find-your-car/)

A trivia game: answer 10 questions, each right answer walks you closer to your car in a dusk parking lot. 10/10 and you drive home.

## Features & Tech
- Three.js (PSX-style low-res render) + hand-rolled Material 3 components, built into one self-contained `docs/index.html`.
- `npm install && npm run build` regenerates the bundle. Questions live in `src/questions.json`.

## Credits & Asset Attributions

- **3D Car Models & Textures**: PSX Low-Poly Car pack by [GGBot](https://ggbot.net/) ([ggbot.itch.io](https://ggbot.itch.io/)).
- **3D Characters & Rigging**: Low-poly PSX character models rigged and animated with [Adobe Mixamo](https://www.mixamo.com/).
- **Sound Effects**: Vehicle Foley effects (`assets/sfx/` — car door open/close, engine startup, engine idle loop, acceleration, parking brake, and horn) from royalty-free sound effect archives.
- **Background Music**: Ambient 36-second loops (`assets/music/*.mp3`) rendered from pop and TV-theme MIDI files sourced from [FreeMidi.org](https://freemidi.org/). Arrangements belong to their respective community uploaders; original compositions remain copyright of their respective songwriters and publishers. Regenerated via `python3 tools/render_music.py DIR_OF_MIDIS 36` using numpy, scipy, and ffmpeg. Toggle and next-song controls live in the game menu; the top-bar mute button mutes all audio.

