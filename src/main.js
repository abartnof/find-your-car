import { Lot, CHARACTERS, CARS, STEPS, wait } from './scene.js';
import ASSETS from '../build/assets.js';
import QUESTIONS from './questions.json';

const $ = (id) => document.getElementById(id);
const sheet = $('sheet');
const store = {
  get(k, d) { try { const v = localStorage.getItem('fyc.' + k); return v == null ? d : JSON.parse(v); } catch { return d; } },
  set(k, v) { try { localStorage.setItem('fyc.' + k, JSON.stringify(v)); } catch {} },
};

// ---------- audio: soft, reverberant, mostly synthesised ----------
const audio = {
  ctx: null, buffers: {}, muted: store.get('muted', false), master: null, verb: null,
  async unlock() {
    if (this.ctx) { if (this.ctx.state === 'suspended') this.ctx.resume(); return; }
    const AC = window.AudioContext || window.webkitAudioContext; if (!AC) return;
    const ctx = (this.ctx = new AC());
    this.master = ctx.createGain(); this.master.gain.value = this.muted ? 0 : 0.8;
    const comp = ctx.createDynamicsCompressor(); this.master.connect(comp).connect(ctx.destination);
    // cheap reverb: decaying noise impulse
    const len = ctx.sampleRate * 2.8, imp = ctx.createBuffer(2, len, ctx.sampleRate);
    for (let c = 0; c < 2; c++) { const d = imp.getChannelData(c); for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 2.6); }
    const conv = ctx.createConvolver(); conv.buffer = imp;
    this.verb = ctx.createGain(); this.verb.gain.value = 0.5; this.verb.connect(conv).connect(this.master);
    this.ambience();
    for (const k of Object.keys(ASSETS).filter((k) => k.startsWith('sfx/'))) {
      try {
        const bin = atob(ASSETS[k].split(',')[1]); const u = new Uint8Array(bin.length);
        for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
        this.buffers[k.slice(4, -4)] = await new Promise((res, rej) => ctx.decodeAudioData(u.buffer, res, rej));
      } catch {}
    }
  },
  setMuted(m) { this.muted = m; if (this.master) this.master.gain.setTargetAtTime(m ? 0 : 0.8, this.ctx.currentTime, 0.15); },
  // a warm drone, a breath of wind and the odd far-off cricket
  ambience() {
    const ctx = this.ctx, out = ctx.createGain(); out.gain.value = 0; out.connect(this.master); out.connect(this.verb);
    out.gain.setTargetAtTime(1, ctx.currentTime, 3);
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 520; lp.connect(out);
    [130.81, 196.0, 261.63, 329.63].forEach((f, i) => {
      for (const det of [-3, 3]) {
        const o = ctx.createOscillator(), g = ctx.createGain(); o.type = 'sine'; o.frequency.value = f; o.detune.value = det;
        g.gain.value = 0.014; const lfo = ctx.createOscillator(), lg = ctx.createGain(); lfo.frequency.value = 0.05 + i * 0.031; lg.gain.value = 0.008;
        lfo.connect(lg).connect(g.gain); o.connect(g).connect(lp); o.start(); lfo.start();
      }
    });
    const nb = ctx.createBuffer(1, ctx.sampleRate * 4, ctx.sampleRate), nd = nb.getChannelData(0); let b0 = 0;
    for (let i = 0; i < nd.length; i++) { b0 = b0 * 0.985 + (Math.random() * 2 - 1) * 0.1; nd[i] = b0; }
    const ns = ctx.createBufferSource(); ns.buffer = nb; ns.loop = true;
    const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 380; bp.Q.value = 0.4;
    const wg = ctx.createGain(); wg.gain.value = 0.35; const wl = ctx.createOscillator(), wlg = ctx.createGain(); wl.frequency.value = 0.07; wlg.gain.value = 0.2;
    wl.connect(wlg).connect(wg.gain); ns.connect(bp).connect(wg).connect(out); ns.start(); wl.start();
    const cricket = () => {
      if (!this.muted && ctx.state === 'running') {
        const t = ctx.currentTime, f = 4200 + Math.random() * 500;
        for (let i = 0; i < 3; i++) { const o = ctx.createOscillator(), g = ctx.createGain(); o.frequency.value = f; o.connect(g).connect(out); g.gain.setValueAtTime(0, t + i * 0.09); g.gain.linearRampToValueAtTime(0.006, t + i * 0.09 + 0.02); g.gain.linearRampToValueAtTime(0, t + i * 0.09 + 0.07); o.start(t + i * 0.09); o.stop(t + i * 0.09 + 0.1); }
      }
      setTimeout(cricket, 2500 + Math.random() * 5000);
    };
    cricket();
  },
  play(name, vol = 0.4) {
    if (this.muted || !this.ctx || !this.buffers[name]) return;
    const s = this.ctx.createBufferSource(), g = this.ctx.createGain();
    s.buffer = this.buffers[name]; g.gain.value = vol; s.connect(g); g.connect(this.master); g.connect(this.verb); s.start();
  },
  // one soft bell note: sine + quiet octave, slow bloom, long tail
  bell(freq, when = 0, vol = 0.12, dur = 2.2) {
    if (this.muted || !this.ctx) return;
    const ctx = this.ctx, t = ctx.currentTime + when;
    for (const [m, v] of [[1, 1], [2, 0.18], [3, 0.05]]) {
      const o = ctx.createOscillator(), g = ctx.createGain(); o.type = 'sine'; o.frequency.value = freq * m;
      o.connect(g); g.connect(this.master); g.connect(this.verb);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol * v, t + 0.015); g.gain.exponentialRampToValueAtTime(0.0008, t + dur / m);
      o.start(t); o.stop(t + dur + 0.1);
    }
  },
  // each right answer rises one step up a pentatonic scale
  correct(n) {
    const sc = [523.25, 587.33, 659.25, 783.99, 880, 1046.5, 1174.7, 1318.5, 1568, 1760];
    const f = sc[Math.min(n, sc.length - 1)]; this.bell(f, 0, 0.12); this.bell(f * 1.5, 0.12, 0.05, 1.6);
  },
  // a soft, distant thump with a little sparkle
  boom() {
    if (this.muted || !this.ctx) return;
    const ctx = this.ctx, t = ctx.currentTime + 0.05, len = ctx.sampleRate * 0.5, b = ctx.createBuffer(1, len, ctx.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 2.5);
    const s = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain(); s.buffer = b; f.type = 'lowpass'; f.frequency.value = 260 + Math.random() * 120; g.gain.value = 0.22;
    s.connect(f).connect(g); g.connect(this.master); g.connect(this.verb); s.start(t);
    for (let k = 0; k < 3; k++) this.bell(1800 + Math.random() * 1800, 0.12 + k * 0.09, 0.018, 0.9);
  },
  wrong() { this.bell(329.63, 0, 0.08, 1.8); this.bell(293.66, 0.22, 0.07, 2.2); },
  win() { [523.25, 659.25, 783.99, 1046.5, 1318.5].forEach((f, i) => this.bell(f, i * 0.28, 0.1, 3.2)); },
  step(alt) {
    if (this.muted || !this.ctx) return;
    const ctx = this.ctx, len = ctx.sampleRate * 0.07, b = ctx.createBuffer(1, len, ctx.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
    const s = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain(); s.buffer = b; f.type = 'lowpass'; f.frequency.value = alt ? 420 : 520; g.gain.value = 0.07;
    s.connect(f).connect(g).connect(this.master); s.start();
  },
};
// ---------- background music: MIDI-derived clips (assets/music), decoded lazily by an <audio> element ----------
const TITLES = { AddamsFamily: 'The Addams Family', Alf: 'ALF', BadMoonRising: 'Bad Moon Rising', BlackMagicWoman: 'Black Magic Woman', CanYouFeelTheLoveTonight: 'Can You Feel the Love Tonight', FreshPrinceOfBelAir: 'The Fresh Prince of Bel-Air', Friends: "I'll Be There for You", GangnamStyle: 'Gangnam Style', HeyJude: 'Hey Jude', HotelCalifornia: 'Hotel California', MyHumps: 'My Humps', NoWomanNoCry: 'No Woman, No Cry', PianoMan: 'Piano Man', PokerFace: 'Poker Face', Rollinginthedeep: 'Rolling in the Deep', TearsInHeaven: 'Tears in Heaven', YoureBeautiful: "You're Beautiful" };
const music = {
  tracks: Object.keys(ASSETS).filter((k) => k.startsWith('music/')).map((k) => ({ key: k, title: TITLES[k.slice(6, -4)] || k.slice(6, -4) })),
  on: store.get('music', true), at: -1, el: null,
  get title() { return this.at >= 0 ? this.tracks[this.at].title : ''; },
  load() {
    if (!this.tracks.length) return null;
    if (!this.el) {
      this.at = Math.floor(Math.random() * this.tracks.length);
      const el = (this.el = new Audio()); el.preload = 'none';
      el.addEventListener('ended', () => this.next());
      try { // through the master gain so the mute button applies (iOS ignores element.volume)
        this.gain = audio.ctx.createGain(); this.gain.gain.value = 0.22;
        audio.ctx.createMediaElementSource(el).connect(this.gain); this.gain.connect(audio.master);
      } catch { el.volume = 0.22; }
      el.src = ASSETS[this.tracks[this.at].key];
    }
    return this.el;
  },
  // call after a user gesture (audio.ctx exists): play if on and not muted, else pause
  sync() {
    const want = this.on && !audio.muted && audio.ctx && document.visibilityState !== 'hidden';
    if (!want) { this.el?.pause(); return; }
    const el = this.load(); if (!el) return;
    const r = el.play(); r?.catch?.(() => {});
  },
  next() {
    if (!this.tracks.length) return;
    if (!this.el) { this.sync(); if (!this.el) return; }
    this.at = (this.at + 1) % this.tracks.length;
    this.el.src = ASSETS[this.tracks[this.at].key]; this.sync();
  },
  set(on) { this.on = on; store.set('music', on); audio.unlock(); this.sync(); },
};
document.addEventListener('visibilitychange', () => music.sync());

function renderMute() {
  $('muteIcon').setAttribute('d', audio.muted
    ? 'M16.5 12A4.5 4.5 0 0 0 14 8v2.2l2.5 2.5v-.7zM19 12c0 .9-.2 1.8-.5 2.6l1.5 1.5A8.9 8.9 0 0 0 21 12c0-4.3-3-7.9-7-8.8v2.1c2.9.9 5 3.5 5 6.7zM4.3 3 3 4.3 7.7 9H3v6h4l5 5v-6.7l4.3 4.3c-.7.5-1.4.9-2.3 1.2v2.1a9 9 0 0 0 3.6-1.8l2.1 2.1 1.3-1.3L4.3 3zM12 4 9.9 6.1 12 8.2V4z'
    : 'M3 9v6h4l5 5V4L7 9H3zm13.5 3A4.5 4.5 0 0 0 14 8v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1c2.9.9 5 3.5 5 6.7s-2.1 5.8-5 6.7v2.1c4-.9 7-4.5 7-8.8s-3-7.9-7-8.8z');
}
$('muteBtn').addEventListener('click', () => { audio.unlock(); audio.setMuted(!audio.muted); store.set('muted', audio.muted); renderMute(); music.sync(); });
renderMute();

// ---------- ripple on any .btn / .fchip / .icon-btn ----------
document.addEventListener('pointerdown', (e) => {
  audio.unlock(); music.sync();
  const el = e.target.closest('.btn,.fchip,.icon-btn'); if (!el) return;
  const r = el.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2;
  const s = document.createElement('span'); s.className = 'ripple';
  s.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
  el.appendChild(s); setTimeout(() => s.remove(), 600);
});

let snackT;
function snack(msg) { const s = $('snack'); s.textContent = msg; s.classList.add('show'); clearTimeout(snackT); snackT = setTimeout(() => s.classList.remove('show'), 2200); }

// ---------- state ----------
const shows = [...new Set(QUESTIONS.map((q) => q.show))];
const showGroups = (() => { // chips: the three big shows, movie/TV comedies by decade, and the long tail of 90s sitcoms
  const main = ['Friends', 'Will & Grace', 'Frasier'];
  const isComedy = (s) => s.startsWith('Comedy');
  const other = shows.filter((s) => !main.includes(s) && !isComedy(s));
  const comedy = shows.filter(isComedy);
  return [...main.filter((m) => shows.includes(m)).map((m) => ({ label: m, shows: [m] })),
    ...(comedy.length ? [{ label: 'Comedy Classics', shows: comedy }] : []),
    ...(other.length ? [{ label: '90s Sitcoms', shows: other }] : [])];
})();
const S = {
  char: Math.min(store.get('char', 0), CHARACTERS.length - 1),
  car: Math.min(store.get('car', 0), CARS.length - 1),
  tex: store.get('tex', 0),
  groups: new Set(store.get('groups', []).filter((l) => showGroups.some((g) => g.label === l))),
  qs: [], i: 0, score: 0, answered: false, seen: new Set(),
};
let lot;
if (!S.groups.size) showGroups.forEach((g) => S.groups.add(g.label));

const ESC = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const ICON = {
  next: '<svg viewBox="0 0 24 24"><path d="M12 4l-1.4 1.4 5.6 5.6H4v2h12.2l-5.6 5.6L12 20l8-8z"/></svg>',
  prev: '<svg viewBox="0 0 24 24"><path d="M15.4 7.4 14 6l-6 6 6 6 1.4-1.4L10.8 12z"/></svg>',
  nxt: '<svg viewBox="0 0 24 24"><path d="M8.6 16.6 13.2 12 8.6 7.4 10 6l6 6-6 6z"/></svg>',
};

function pickQuestions() {
  const allowed = new Set(showGroups.filter((g) => S.groups.has(g.label)).flatMap((g) => g.shows));
  let pool = QUESTIONS.filter((q) => allowed.has(q.show));
  let fresh = pool.filter((q) => !S.seen.has(q.q));
  if (fresh.length < STEPS) { fresh = pool; S.seen.clear(); }
  const shuf = (a) => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0;[a[i], a[j]] = [a[j], a[i]]; } return a; };
  const take = [];
  for (const [d, n] of [[1, 3], [2, 4], [3, 3]]) take.push(...shuf(fresh.filter((q) => q.d === d)).slice(0, n));
  const ids = new Set(take.map((q) => q.q));
  for (const q of shuf(fresh)) { if (take.length >= STEPS) break; if (!ids.has(q.q)) { take.push(q); ids.add(q.q); } }
  take.sort((a, b) => a.d - b.d || Math.random() - 0.5);
  return take.slice(0, STEPS).map((q) => {
    const opts = q.options.map((t, i) => ({ t, ok: i === q.answer })); const o = shuf(opts);
    return { show: q.show, q: q.q, opts: o };
  });
}

// ---------- screens ----------
function renderMenu() {
  lot.reset(); lot.mode = 'menu';
  $('title').textContent = 'Find Your Car'; $('scoreChip').hidden = true; $('progress').hidden = true;
  const car = CARS[S.car];
  sheet.innerHTML = `
    <p class="overline">Sitcom trivia</p>
    <h1 class="headline">Where did you park?</h1>
    <p class="body">Ten questions. Every right answer gets you one step closer to your car. Get all ten and you're driving home.</p>
    <div class="label">YOU</div>
    <div class="picker"><button class="icon-btn" data-a="char-" aria-label="Previous character">${ICON.prev}</button><div class="name">${CHARACTERS[S.char].name}</div><button class="icon-btn" data-a="char+" aria-label="Next character">${ICON.nxt}</button></div>
    <div class="label">YOUR CAR</div>
    <div class="picker"><button class="icon-btn" data-a="car-" aria-label="Previous car">${ICON.prev}</button><div class="name">${car.name}</div><button class="icon-btn" data-a="car+" aria-label="Next car">${ICON.nxt}</button></div>
    <div class="swatches" aria-label="Paint">${Array.from({ length: car.tex }, (_, i) => `<button class="sw ${i === S.tex ? 'sel' : ''}" data-a="tex${i}" aria-label="Paint ${i + 1}" data-sw="${car.id}_${i}" style="background:${SWC[car.id + '_' + i] || '#888'}"></button>`).join('')}</div>
    <div class="label">TOPICS</div>
    <div class="chips">${showGroups.map((g) => `<button class="fchip ${S.groups.has(g.label) ? 'sel' : ''}" data-g="${ESC(g.label)}">${ESC(g.label)}</button>`).join('')}</div>
    ${music.tracks.length ? `<div class="label">MUSIC</div>
    <div class="musicrow"><button class="switch ${music.on ? 'on' : ''}" role="switch" aria-checked="${music.on}" data-m="toggle" aria-label="Background music"><span class="knob"></span></button>
      <div class="mtitle">${music.on ? (music.title ? '♪ ' + ESC(music.title) : 'Background music') : 'Music off'}</div>
      <button class="icon-btn" data-m="next" aria-label="Next song" ${music.on ? '' : 'disabled'}>${ICON.nxt}</button></div>` : ''}
    <div class="sticky"><button class="btn btn-filled btn-block" id="go">Start</button></div>`;
  sheet.scrollTop = 0;
}
const SWC = {};
function loadSwatches() {
  for (const car of CARS) for (let i = 0; i < car.tex; i++) {
    const img = new Image(); img.onload = () => {
      const c = document.createElement('canvas'); c.width = c.height = 16; const x = c.getContext('2d'); x.drawImage(img, 0, 0, 16, 16);
      const d = x.getImageData(0, 0, 16, 16).data; let r = 0, g = 0, b = 0, n = 0;
      for (let k = 0; k < d.length; k += 4) if (d[k + 3] > 200) { r += d[k]; g += d[k + 1]; b += d[k + 2]; n++; }
      SWC[`${car.id}_${i}`] = `rgb(${r / n | 0},${g / n | 0},${b / n | 0})`;
      document.querySelectorAll(`[data-sw="${car.id}_${i}"]`).forEach((e) => (e.style.background = SWC[`${car.id}_${i}`]));
    }; img.src = ASSETS[`cars/car${car.id}_${i}.png`];
  }
}

sheet.addEventListener('click', (e) => {
  const b = e.target.closest('[data-m],[data-a],[data-g],#go,[data-opt],#next,#again'); if (!b) return;
  if (b.dataset.m) { if (b.dataset.m === 'toggle') music.set(!music.on); else music.next(); renderMenu(); }
  else if (b.dataset.a) {
    const a = b.dataset.a;
    if (a.startsWith('char')) { S.char = (S.char + (a.endsWith('+') ? 1 : -1) + CHARACTERS.length) % CHARACTERS.length; lot.setCharacter(CHARACTERS[S.char].id); }
    else if (a.startsWith('car')) { S.car = (S.car + (a.endsWith('+') ? 1 : -1) + CARS.length) % CARS.length; S.tex = 0; lot.setCar(S.car, S.tex); }
    else if (a.startsWith('tex')) { S.tex = +a.slice(3); lot.setCar(S.car, S.tex); }
    store.set('char', S.char); store.set('car', S.car); store.set('tex', S.tex); renderMenu();
  } else if (b.dataset.g) {
    const g = b.dataset.g;
    if (S.groups.has(g)) { if (S.groups.size > 1) S.groups.delete(g); else return snack('Keep at least one topic'); } else S.groups.add(g);
    store.set('groups', [...S.groups]); renderMenu();
  } else if (b.id === 'go') startGame();
  else if (b.dataset.opt != null) answer(+b.dataset.opt);
  else if (b.id === 'next') nextQ();
  else if (b.id === 'again') { renderMenu(); }
});

function startGame() {
  S.qs = pickQuestions(); S.qs.forEach((q) => S.seen.add(q.q)); S.i = 0; S.score = 0;
  lot.reset(); lot.mode = 'play';
  $('scoreChip').hidden = false; $('progress').hidden = false; updateHud();
  renderQ();
}
function updateHud() {
  $('scoreText').textContent = `${S.score} / ${STEPS}`;
  $('progressBar').style.width = `${(S.score / STEPS) * 100}%`;
  $('title').textContent = `Question ${Math.min(S.i + 1, STEPS)} of ${STEPS}`;
}
function renderQ() {
  const q = S.qs[S.i]; S.answered = false; updateHud();
  sheet.innerHTML = `
    <p class="overline">${ESC(q.show)}</p>
    <h2 class="question">${ESC(q.q)}</h2>
    <div class="options">${q.opts.map((o, i) => `<button class="btn btn-opt" data-opt="${i}"><span class="key">${'ABCD'[i]}</span><span>${ESC(o.t)}</span></button>`).join('')}</div>
    <div id="fb"></div>`;
  sheet.scrollTop = 0;
}
function answer(i) {
  if (S.answered) return; S.answered = true;
  const q = S.qs[S.i], ok = q.opts[i].ok;
  sheet.querySelectorAll('.btn-opt').forEach((el, k) => {
    if (q.opts[k].ok) el.classList.add('correct'); else if (k === i) el.classList.add('wrong'); else el.classList.add('dim');
  });
  const last = S.i === STEPS - 1, win = ok && S.score + 1 === STEPS;
  if (ok) {
    S.score++; lot.advance(); lot.cheer(); audio.correct(S.score - 1); updateHud();
    const left = STEPS - S.score; snack(left ? `Nice! ${left} more to go` : 'Your car is right there!');
  } else {
    lot.stumble(); audio.wrong();
    snack(`Nope — it's "${q.opts.find((o) => o.ok).t}"`);
  }
  $('fb').innerHTML = `<button class="btn fab-ext" id="next">${last ? (win ? 'Get in the car' : 'See results') : 'Next'}${ICON.next}</button>`;
  sheet.scrollTo({ top: sheet.scrollHeight, behavior: 'smooth' });
}
function nextQ() {
  if (!S.answered) return;
  if (S.i === STEPS - 1) return finish();
  S.i++; renderQ();
}
async function finish() {
  const win = S.score === STEPS;
  $('progress').hidden = true;
  sheet.innerHTML = '';
  if (win) {
    $('title').textContent = 'You made it!';
    await lot.drive(audio);
    sheet.innerHTML = `<div class="result"><p class="overline">10 / 10</p><h1 class="headline">You found your car!</h1><p class="body">Flawless. Keys in hand, engine running, and a very nice ${CARS[S.car].name.toLowerCase()} to take you home.</p><div class="row"><button class="btn btn-filled" id="again">Play again</button></div></div>`;
    audio.win();
  } else {
    $('title').textContent = 'Not quite…';
    const left = STEPS - S.score;
    sheet.innerHTML = `<div class="result"><p class="overline">Final score</p><p class="score-big">${S.score} / ${STEPS}</p><h1 class="headline">${S.score >= 7 ? 'So close!' : S.score >= 4 ? 'Still wandering the lot' : 'Where did you even park?'}</h1><p class="body">Your car is ${left} step${left > 1 ? 's' : ''} away. You need a perfect 10 to drive home.</p><div class="row"><button class="btn btn-filled" id="again">Try again</button></div></div>`;
  }
}

// ---------- boot ----------
(async function boot() {
  lot = new Lot($('gl'));
  lot.setCharacter(CHARACTERS[S.char].id);
  lot.setCar(S.car, S.tex);
  lot.start();
  window.__lot = lot;
  lot.onBurst = () => audio.boom();
  let alt = 0; lot.onStep = () => { if (lot.mode !== 'menu') audio.step(alt ^= 1); };
  loadSwatches();
  if (/probe/.test(location.hash)) {   // dev: report foot/hand z at the phase where sin = 1
    const w = lot.walker; w.moving = 1; w.phase = Math.PI / 2; w.update(0.0001, 2.2); lot.walkerHolder.updateMatrixWorld(true);
    const z = (n) => { const v = new w.model.position.constructor(); w.bones[n].getWorldPosition(v); return v.z.toFixed(3); };
    const d = document.createElement('div'); d.id = 'probe'; d.textContent = ['LeftFoot', 'RightFoot', 'LeftHand', 'RightHand', 'LeftLeg', 'LeftUpLeg'].map((n) => n + '=' + z(n)).join(' ');
    document.body.appendChild(d);
  }
  renderMenu();
  const demo = /demo=(\d+)/.exec(location.hash);
  if (demo) { lot.snap = true; startGame(); for (let i = 0; i < +demo[1]; i++) { lot.advance(); S.score++; } lot.z = lot.stepZ; updateHud(); if (/win/.test(location.hash)) { lot.z = lot.stepZ; finish(); } }
  if (/ans/.test(location.hash)) answer(0);
  await wait(300);
  $('loading').classList.add('done');
})();
