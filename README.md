# Find Your Car

🎮 **Play live**: [https://abartnof.github.io/find-your-car/](https://abartnof.github.io/find-your-car/)

A trivia game: answer 10 questions, each right answer walks you closer to your car in a dusk parking lot. 10/10 and you drive home.

- Three.js (PSX-style low-res render) + hand-rolled Material 3 components, built into one self-contained `docs/index.html`.
- `npm install && npm run build` regenerates it. Questions live in `src/questions.json`.
- Art/audio: PSX-style cars by GGBot, PSX characters pack (see original asset licenses).
- Background music: `assets/music/*.mp3` are soft, drum-less 36 s renders (22.05 kHz mono, 32 kbps) of pop/TV-theme MIDIs from freemidi.org (arrangements by their respective uploaders; the songs belong to their copyright holders). Regenerate with `python3 tools/render_music.py DIR_OF_MIDIS 36` (numpy, scipy, ffmpeg). Toggle and next-song live in the New game menu; the top-bar mute silences it too.
