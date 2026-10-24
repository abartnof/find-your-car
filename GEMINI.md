# Repository Guidelines & Trivia Quality Standards

## Trivia Phrasing & Natural Language
- **Natural, authentic writing**: All trivia prompts, options, and distractors must read naturally to human players.
- **No synthetic distractor padding**: Never use mechanical boilerplate or robotic template suffixes (such as `(introduced during the storyline)`, `(as described in the episode)`, `(referenced by the characters)`, `(extended broadcast detail)`, `(documented extensively throughout contemporary regional archives)`, `(certified organic cultivar)`, `(regular prime-time television series ensemble cast member)`) to artificially manipulate option lengths.
- **Authentic length balancing**: When options need length calibration, enrich them with real, domain-accurate trivia details (e.g. real character full names, authentic setting descriptions, or lore-accurate context) rather than repetitive formulas.
- **Answerability in umbrella categories**: Questions in multi-show, multi-film, or multi-artist categories (such as *80s TV Shows*, *90s Sitcoms*, *Streaming TV Shows*, *Romantic Comedies*) must explicitly identify the specific work, show, or film being asked about so the player has complete context.
- **No giveaways or circular clues**: Question stems must never give away the answer, contain self-answering episode titles, or leak unique keywords found only in the correct option.

## Statistical Balance & Question Fairness
- **Option length neutrality**: With 4 options, the correct answer should be the longest option roughly 25% of the time (acceptable natural distribution: ~20%–26%). Length should provide zero predictive signal to the player—neither biased toward being the longest nor artificially suppressed so low that players can safely eliminate long options.
- **Uniform positional balance**: Correct answer keys (`0`, `1`, `2`, `3`) must be evenly distributed (~25% each) across every category to prevent positional bias (such as favoriting option "C").
- **Difficulty progression tiering**: Quizzes should follow a balanced 3-tier difficulty distribution: ~30% `d: 1` (accessible / common knowledge), ~40% `d: 2` (fan / enthusiast), and ~30% `d: 3` (deep cuts / trivia experts).

## Format & Codebase Integrity
- **No letter or number prefixes in option strings**: Options must never begin with `A.`, `B.`, `1.`, `a)`, etc., as the game UI dynamically renders option letters. Names with initials must be formatted to avoid prefix collision (e.g., `Riley 'B.B.' King` or `Arthur C. Moore`).
- **Exactly 4 unique options**: Every question must contain exactly 4 unique options (no duplicate or case-insensitive duplicate entries).
- **Build & staging synchronization**: Any changes made to `src/questions.json` must be synchronized with corresponding staging files in `tools/staging/` and compiled to `docs/index.html` via `npm run build` prior to committing and pushing.
