import { Lot, CHARACTERS, CARS, STEPS, wait } from './scene.js';
import { initEffects, clearEffects } from './effects.js';
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
  ctx: null, buffers: {}, muted: false, master: null, verb: null,
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
    // (no ambient bed: the soundtrack carries the mood)
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
const TITLES = {
  AddamsFamily: "The Addams Family",
  Alf: "ALF",
  AllThatSheWants: "All That She Wants",
  AngryYoungMan: "Prelude / Angry Young Man",
  AsLongAsYouLoveMe: "As Long as You Love Me",
  BadGirls: "Bad Girls",
  BadMoonRising: "Bad Moon Rising",
  BeingForTheBenefitOfMrKite: "Being for the Benefit of Mr. Kite!",
  Believe: "Believe",
  BigShot: "Big Shot",
  BlackMagicWoman: "Black Magic Woman",
  CanYouFeelTheLoveTonight: "Can You Feel the Love Tonight",
  CantGetEnoughOfYourLove: "Can't Get Enough of Your Love, Babe",
  CrazyInLove: "Crazy in Love",
  CruelSummer: "Cruel Summer",
  CutTheCake: "Cut the Cake",
  DancingQueen: "Dancing Queen",
  DoesYourMotherKnow: "Does Your Mother Know",
  DontLeaveMeThisWay: "Don't Leave Me This Way",
  DontTurnAround: "Don't Turn Around",
  EverybodysGotSomethingToHide: "Everybody's Got Something to Hide Except Me and My Monkey",
  EveryonesAWinner: "Everyone's a Winner",
  Fernando: "Fernando",
  FreshPrinceOfBelAir: "The Fresh Prince of Bel-Air",
  Friends: "I'll Be There for You",
  GangnamStyle: "Gangnam Style",
  GimmeGimmeGimme: "Gimme! Gimme! Gimme! (A Man After Midnight)",
  GypsiesTrampsAndThieves: "Gypsies, Tramps & Thieves",
  HazyShadeOfWinter: "A Hazy Shade of Winter",
  HeyJude: "Hey Jude",
  HotStuff: "Hot Stuff",
  HotelCalifornia: "Hotel California",
  HowCanYouMendABrokenHeart: "How Can You Mend a Broken Heart",
  HowDeepIsYourLove: "How Deep Is Your Love",
  IFeelLove: "I Feel Love",
  IGotYouBabe: "I Got You Babe",
  IRanSoFarAway: "I Ran (So Far Away)",
  IWantItThatWay: "I Want It That Way",
  IWillSurvive: "I Will Survive",
  IfICouldTurnBackTime: "If I Could Turn Back Time",
  IllNeverBreakYourHeart: "I'll Never Break Your Heart",
  IslandsInTheStream: "Islands in the Stream",
  ItsGottaBeYou: "It's Gotta Be You",
  ItsStillRockAndRollToMe: "It's Still Rock and Roll to Me",
  JustTheWayYouAre: "Just the Way You Are",
  KnowingMeKnowingYou: "Knowing Me, Knowing You",
  Kokomo: "Kokomo",
  LastDance: "Last Dance",
  LoveShack: "Love Shack",
  MamboSwing: "Mambo Swing",
  MammaMia: "Mamma Mia",
  ManicMonday: "Manic Monday",
  Massachusetts: "Massachusetts",
  MoreThanAWoman: "More Than a Woman",
  MovingOut: "Movin' Out (Anthony's Song)",
  MyHumps: "My Humps",
  NeverNeverGonnaGiveYouUp: "Never, Never Gonna Give Ya Up",
  NewYorkMiningDisaster1941: "New York Mining Disaster 1941",
  NewYorkStateOfMind: "New York State of Mind",
  NightFever: "Night Fever",
  NoWomanNoCry: "No Woman, No Cry",
  PianoMan: "Piano Man",
  PickUpThePieces: "Pick Up the Pieces",
  PokerFace: "Poker Face",
  QuitPlayingGamesWithMyHeart: "Quit Playing Games (with My Heart)",
  Rehab: "Rehab",
  RockLobster: "Rock Lobster",
  Rollinginthedeep: "Rolling in the Deep",
  SOS: "SOS",
  SingleLadies: "Single Ladies (Put a Ring on It)",
  StandByMe: "Stand by Me",
  StayinAlive: "Stayin' Alive",
  TearsInHeaven: "Tears in Heaven",
  TheBeatGoesOn: "The Beat Goes On",
  TheSign: "The Sign",
  Tiger: "Tiger",
  VoulezVous: "Voulez-Vous",
  WalkLikeAnEgyptian: "Walk Like an Egyptian",
  WalkingInMemphis: "Walking in Memphis",
  Waterloo: "Waterloo",
  WeDidntStartTheFire: "We Didn't Start the Fire",
  WorkItOut: "Work It Out",
  YouMayBeRight: "You May Be Right",
  YouSexyThing: "You Sexy Thing",
  YouShouldBeDancing: "You Should Be Dancing",
  YoureBeautiful: "You're Beautiful",
  YoureTheFirstTheLastMyEverything: "You're the First, the Last, My Everything",
};
const music = {
  tracks: Object.keys(ASSETS).filter((k) => k.startsWith('music/')).map((k) => ({ key: k, title: TITLES[k.slice(6, -4)] || k.slice(6, -4) })),
  on: store.get('music', true), at: -1, el: null,
  get title() { return this.at >= 0 ? this.tracks[this.at].title : ''; },
  load() {
    if (!this.tracks.length) return null;
    if (!this.el) {
      this.at = Math.floor(Math.random() * this.tracks.length);
      const el = (this.el = new Audio()); el.preload = 'none';
      el.addEventListener('ended', () => { this.next(); renderMusicDropdown(); if ($('sheet')?.querySelector('#go')) renderMenu(true); });
      try { // through the master gain so the mute button applies (iOS ignores element.volume)
        this.gain = audio.ctx.createGain(); this.gain.gain.value = 0.4;
        audio.ctx.createMediaElementSource(el).connect(this.gain); this.gain.connect(audio.master);
      } catch { el.volume = 0.4; }
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

function renderMusicDropdown() {
  const dd = $('musicDropdown');
  if (!dd) return;
  const title = $('musicDropdownTitle');
  if (title) title.textContent = music.title || 'Background music';
  const toggleIcon = $('musicToggleIcon');
  if (toggleIcon) {
    const path = toggleIcon.querySelector('path');
    if (path) path.setAttribute('d', music.on ? 'M6 19h4V5H6v14zm8-14v14h4V5h-4z' : 'M8 5v14l11-7z');
  }
  const toggleBtn = $('musicToggleBtn');
  if (toggleBtn) toggleBtn.setAttribute('aria-label', music.on ? 'Pause' : 'Play');
}
function renderMusicBtn() { $('musicBtn').classList.toggle('off', !music.on); }
$('musicBtn').addEventListener('click', () => {
  const dd = $('musicDropdown');
  if (!dd) return;
  const opening = dd.hasAttribute('hidden') || dd.hidden;
  if (opening) {
    dd.removeAttribute('hidden');
    dd.hidden = false;
    audio.unlock();
    if (!music.el) music.load();
    renderMusicDropdown();
  } else {
    dd.setAttribute('hidden', '');
    dd.hidden = true;
  }
});
$('musicToggleBtn')?.addEventListener('click', () => {
  music.set(!music.on);
  renderMusicDropdown();
  renderMusicBtn();
  if ($('sheet')?.querySelector('#go')) renderMenu(true);
});
$('musicSkipBtn')?.addEventListener('click', () => {
  music.next();
  if (!music.on) music.set(true);
  renderMusicDropdown();
  renderMusicBtn();
  if ($('sheet')?.querySelector('#go')) renderMenu(true);
});
document.addEventListener('pointerdown', (e) => {
  if (!e.target.closest('#musicDropdown') && !e.target.closest('#musicBtn')) {
    const dd = $('musicDropdown');
    if (dd) {
      dd.setAttribute('hidden', '');
      dd.hidden = true;
    }
  }
});
renderMusicBtn();
renderMusicDropdown();

// ---------- ripple on any .btn / .fchip / .icon-btn ----------
document.addEventListener('pointerdown', (e) => {
  audio.unlock(); music.sync();
  const el = e.target.closest('.btn,.fchip,.icon-btn'); if (!el) return;
  const r = el.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2;
  const s = document.createElement('span'); s.className = 'ripple';
  s.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
  el.appendChild(s); setTimeout(() => s.remove(), 600);
});


// ---------- leaderboard (stored on this device) ----------
const board = {
  all() { const a = store.get('scores', []); return Array.isArray(a) ? a : []; },
  add(e) { store.set('scores', [...this.all(), e].slice(-200)); },
  top(n = 25) { return this.all().slice().sort((a, b) => b.score - a.score || b.t - a.t).slice(0, n); },
};
const fmtWhen = (t) => { try { return new Date(t).toLocaleString(undefined, { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' }); } catch { return ''; } };
function showBoard(hiT) {
  closeBoard();
  const rows = board.top();
  const d = document.createElement('div'); d.className = 'scrim'; d.id = 'board';
  d.innerHTML = `<div class="dialog" role="dialog" aria-modal="true" aria-label="Leaderboard">
    <h2 class="dlg-title">Leaderboard</h2>
    ${rows.length ? `<ol class="lb">${rows.map((r, i) => `<li class="${r.t === hiT ? 'me' : ''}"><span class="rk">${i + 1}</span><span class="nm">${ESC(r.name || 'Player')}${r.score === STEPS ? ' <span class="win">🏆</span>' : ''}<small>${ESC(fmtWhen(r.t))}</small></span><span class="sc">${r.score}/${STEPS}</span></li>`).join('')}</ol>` : '<p class="body">No scores yet. Finish a game to get on the board.</p>'}
    <div class="dlg-actions">${rows.length ? '<button class="btn btn-text" id="lbClear">Clear</button>' : ''}<button class="btn btn-filled" id="lbClose">Close</button></div></div>`;
  d.addEventListener('click', (e) => {
    if (e.target === d || e.target.id === 'lbClose') closeBoard();
    else if (e.target.id === 'lbClear') { if (e.target.dataset.sure) { store.set('scores', []); showBoard(); } else { e.target.dataset.sure = 1; e.target.textContent = 'Tap again to clear'; } }
  });
  document.body.appendChild(d);
}
function closeBoard() { const d = document.getElementById('board'); if (d) d.remove(); }
$('lbBtn').addEventListener('click', () => showBoard());

let snackT;
function snack(msg) { const s = $('snack'); s.textContent = msg; s.classList.add('show'); clearTimeout(snackT); snackT = setTimeout(() => s.classList.remove('show'), 2200); }

// ---------- state ----------
const showGroups = (() => {
  const counts = {};
  for (const q of QUESTIONS) counts[q.show] = (counts[q.show] || 0) + 1;
  const comedyShows = [];
  const sitcomShows = [];
  const standaloneShows = [];
  for (const [show, count] of Object.entries(counts)) {
    if (show.startsWith('Comedy · ') || show === 'Comedy Classics') {
      comedyShows.push(show);
    } else if (count < 10) {
      sitcomShows.push(show);
    } else {
      standaloneShows.push(show);
    }
  }
  const groups = [
    ...(comedyShows.length ? [{ label: 'Comedy Classics', shows: comedyShows }] : []),
    ...(sitcomShows.length ? [{ label: '90s Sitcoms', shows: sitcomShows }] : []),
    ...standaloneShows.map((show) => ({ label: show, shows: [show] })),
  ];
  groups.sort((a, b) => a.label.localeCompare(b.label, undefined, { sensitivity: 'base' }));
  return groups;
})();
const topicWins = {
  all() { const w = store.get('topicWins', {}); return w && typeof w === 'object' ? w : {}; },
  get(label) { return this.all()[label] || 0; },
  record(labels) {
    const w = { ...this.all() };
    for (const l of labels) w[l] = (w[l] || 0) + 1;
    store.set('topicWins', w);
  },
};
const S = {
  name: store.get('name', ''),
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
    return { show: q.show, q: q.q, opts: o, fact: q.fact };
  });
}

// ---------- screens ----------
function renderMenu(keepScroll = false) {
  clearEffects();
  if (lot.mode !== 'menu') lot.reset();   // re-rendering the menu (picking a car/colour/topic) keeps the camera where it is
  lot.mode = 'menu';
  $('app').classList.add('menu-mode');
  $('title').textContent = 'Find Your Car'; $('scoreChip').hidden = true; $('progress').hidden = true;
  const car = CARS[S.car];
  const prevScroll = keepScroll ? sheet.scrollTop : 0;
  sheet.innerHTML = `
    <p class="overline">Trivia challenge</p>
    <h1 class="headline">Where did you park?</h1>
    <p class="body">Ten questions. Every right answer gets you one step closer to your car. Get all ten and you're driving home.</p>
    <label class="field"><input id="name" maxlength="16" placeholder=" " autocomplete="nickname" value="${ESC(S.name)}"><span>Your name (for the leaderboard)</span></label>
    <div class="picker-row">
      <div class="picker-col">
        <div class="label">YOU</div>
        <div class="picker"><button class="icon-btn" data-a="char-" aria-label="Previous character">${ICON.prev}</button><div class="name">${CHARACTERS[S.char].name}</div><button class="icon-btn" data-a="char+" aria-label="Next character">${ICON.nxt}</button></div>
      </div>
      <div class="picker-col">
        <div class="label">YOUR CAR</div>
        <div class="picker"><button class="icon-btn" data-a="car-" aria-label="Previous car">${ICON.prev}</button><div class="name">${car.name}</div><button class="icon-btn" data-a="car+" aria-label="Next car">${ICON.nxt}</button></div>
      </div>
    </div>
    <div class="swatches" aria-label="Paint">${Array.from({ length: car.tex }, (_, i) => `<button class="sw ${i === S.tex ? 'sel' : ''}" data-a="tex${i}" aria-label="Paint ${i + 1}" data-sw="${car.id}_${i}" style="background:${SWC[car.id + '_' + i] || '#888'}"></button>`).join('')}</div>
    <div class="label">TOPICS</div>
    <div class="chips">${showGroups.map((g) => {
      const wins = topicWins.get(g.label);
      const badge = wins > 0 ? `<span class="badge" aria-label="${wins} wins">${wins}</span>` : '';
      return `<button class="fchip ${S.groups.has(g.label) ? 'sel' : ''}" data-g="${ESC(g.label)}">${ESC(g.label)}${badge}</button>`;
    }).join('')}</div>
    ${music.tracks.length ? `<div class="label">MUSIC</div>
    <div class="musicrow"><button class="switch ${music.on ? 'on' : ''}" role="switch" aria-checked="${music.on}" data-m="toggle" aria-label="Background music"><span class="knob"></span></button>
      <div class="mtitle">${music.on ? (music.title ? '♪ ' + ESC(music.title) : 'Background music') : 'Music off'}</div>
      <button class="icon-btn" data-m="next" aria-label="Next song" ${music.on ? '' : 'disabled'}>${ICON.nxt}</button></div>` : ''}
    <div class="sticky"><button class="btn btn-filled btn-block" id="go">Start</button></div>`;

  // Dynamically size sheet so exactly 1.5 topic rows peek out above the Start button on initial view
  const allChips = Array.from(sheet.querySelectorAll('.chips .fchip'));
  const rowTops = [...new Set(allChips.map((c) => c.offsetTop))].sort((a, b) => a - b);
  if (rowTops.length >= 2) {
    const row2Chip = allChips.find((c) => c.offsetTop === rowTops[1]);
    const row2H = row2Chip ? row2Chip.offsetHeight : 32;
    const sticky = sheet.querySelector('.sticky');
    const stickyH = sticky ? sticky.offsetHeight : 76;
    const targetCutoff = rowTops[1] + Math.round(row2H / 2);
    sheet.style.height = `${targetCutoff + stickyH}px`;
  }
  sheet.scrollTop = prevScroll;
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
  const b = e.target.closest('[data-m],[data-a],[data-g],#go,[data-opt],#next,#again,#lb'); if (!b) return;
  if (b.dataset.m) { if (b.dataset.m === 'toggle') { music.set(!music.on); renderMusicBtn(); } else music.next(); renderMusicDropdown(); renderMenu(true); }
  else if (b.dataset.a) {
    const a = b.dataset.a;
    if (a.startsWith('char')) { S.char = (S.char + (a.endsWith('+') ? 1 : -1) + CHARACTERS.length) % CHARACTERS.length; lot.setCharacter(CHARACTERS[S.char].id); }
    else if (a.startsWith('car')) { S.car = (S.car + (a.endsWith('+') ? 1 : -1) + CARS.length) % CARS.length; S.tex = 0; lot.setCar(S.car, S.tex); }
    else if (a.startsWith('tex')) { S.tex = +a.slice(3); lot.setCar(S.car, S.tex); }
    store.set('char', S.char); store.set('car', S.car); store.set('tex', S.tex); renderMenu(true);
  } else if (b.dataset.g) {
    const g = b.dataset.g;
    if (S.groups.has(g)) { if (S.groups.size > 1) S.groups.delete(g); else return snack('Keep at least one topic'); } else S.groups.add(g);
    store.set('groups', [...S.groups]); renderMenu(true);
  } else if (b.id === 'go') startGame();
  else if (b.dataset.opt != null) answer(+b.dataset.opt);
  else if (b.id === 'next') nextQ();
  else if (b.id === 'again') { renderMenu(); }
  else if (b.id === 'lb') showBoard(S.lastT);
});

function startGame() {
  $('app').classList.remove('menu-mode');
  sheet.style.height = '';
  S.qs = pickQuestions(); S.qs.forEach((q) => S.seen.add(q.q)); S.i = 0; S.score = 0;
  clearEffects(); lot.reset(); lot.mode = 'play';
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
  } else {
    lot.stumble(); audio.wrong();
  }
  const action = last ? (win ? 'Get in the car' : 'See results') : 'Next';
  $('fb').innerHTML = `<button class="btn fab-ext" id="next"><span>${action}</span>${ICON.next}</button>`;
  const nextBtn = $('next');
  if (nextBtn) {
    const sRect = sheet.getBoundingClientRect();
    const bRect = nextBtn.getBoundingClientRect();
    if (bRect.bottom > sRect.bottom) {
      nextBtn.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
    nextBtn.focus();
  }
}
function nextQ() {
  if (!S.answered) return;
  if (S.i === STEPS - 1) return finish();
  S.i++; renderQ();
}
document.addEventListener('input', (e) => { if (e.target.id === 'name') { S.name = e.target.value; store.set('name', S.name); } });
let fx;
window.addEventListener('resize', () => { if (lot?.mode === 'menu') renderMenu(true); });
async function finish() {
  $('app').classList.remove('menu-mode');
  sheet.style.height = '';
  const win = S.score === STEPS;
  S.lastT = Date.now(); board.add({ name: S.name.trim() || 'Player', score: S.score, t: S.lastT });
  $('progress').hidden = true;
  sheet.innerHTML = '';
  if (win) {
    const wonGroups = showGroups
      .filter((g) => S.groups.has(g.label) && S.qs.some((q) => g.shows.includes(q.show)))
      .map((g) => g.label);
    topicWins.record(wonGroups.length ? wonGroups : [...S.groups]);
    $('title').textContent = 'You made it!';
    await lot.drive(audio);
    sheet.innerHTML = `<div class="result"><p class="overline">10 / 10</p><h1 class="headline">You found your car!</h1><p class="body">Flawless. Keys in hand, engine running, and a very nice ${CARS[S.car].name.toLowerCase()} to take you home.</p><div class="row"><button class="btn btn-tonal" id="lb">Leaderboard</button><button class="btn btn-filled" id="again">Play again</button></div></div>`;
    audio.win();
  } else {
    $('title').textContent = 'Not quite…'; fx.rain.start(audio);
    const left = STEPS - S.score;
    sheet.innerHTML = `<div class="result"><p class="overline">Final score</p><p class="score-big">${S.score} / ${STEPS}</p><h1 class="headline">${S.score >= 7 ? 'So close!' : S.score >= 4 ? 'Still wandering the lot' : 'Where did you even park?'}</h1><p class="body">Your car is ${left} step${left > 1 ? 's' : ''} away. You need a perfect 10 to drive home.</p><div class="row"><button class="btn btn-tonal" id="lb">Leaderboard</button><button class="btn btn-filled" id="again">Try again</button></div></div>`;
  }
}

// ---------- boot ----------
(async function boot() {
  lot = new Lot($('gl'));
  lot.setCharacter(CHARACTERS[S.char].id);
  lot.setCar(S.car, S.tex);
  lot.start();
  window.__lot = lot;
  fx = initEffects();
  lot.onArrive = () => fx.fireworks.start(() => audio.boom());
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
  if (demo) { lot.snap = true; startGame(); for (let i = 0; i < +demo[1]; i++) { lot.advance(); S.score++; } lot.z = lot.stepZ; updateHud(); if (/win/.test(location.hash)) { lot.z = lot.stepZ; finish(); } else if (/fail/.test(location.hash)) finish(); }
  if (/ans/.test(location.hash)) answer(0);
  if (/board/.test(location.hash)) { for (const sc of [10, 7, 3]) board.add({ name: 'Test ' + sc, score: sc, t: Date.now() - sc * 3.6e6 }); showBoard(); }
  await wait(300);
  $('loading').classList.add('done');
})();
