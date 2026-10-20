// 2D overlay effects drawn over the 3D stage: win fireworks and lose rain. Low-res canvases (chunky, PSX-ish).
const reduced = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const rnd = (a, b) => a + Math.random() * (b - a);
const PASTELS = [[255, 170, 200], [170, 210, 255], [200, 255, 210], [255, 235, 160], [210, 180, 255], [255, 200, 150]];

class Overlay {
  constructor(cls, scale) {
    this.scale = scale; this.on = false; this.raf = 0; this.last = 0;
    this.cv = document.createElement('canvas'); this.cv.className = 'fx ' + cls; this.cv.setAttribute('aria-hidden', 'true');
    this.g = this.cv.getContext('2d');
    this.stage = document.querySelector('.stage'); this.stage.appendChild(this.cv);
    this.tick = (t) => {
      if (!this.on) return;
      this.raf = requestAnimationFrame(this.tick);
      const dt = Math.min(0.05, (t - this.last) / 1000 || 0.016); this.last = t;
      this.step(dt);
    };
    new ResizeObserver(() => this.fit()).observe(this.stage);
    document.addEventListener('visibilitychange', () => { if (document.hidden) this.halt(); else if (this.on) this.run(); });
  }
  fit() {
    const r = this.stage.getBoundingClientRect();
    this.w = Math.max(8, Math.round(r.width / this.scale)); this.h = Math.max(8, Math.round(r.height / this.scale));
    this.cv.width = this.w; this.cv.height = this.h;
  }
  run() { cancelAnimationFrame(this.raf); this.last = performance.now(); this.raf = requestAnimationFrame(this.tick); }
  halt() { cancelAnimationFrame(this.raf); this.raf = 0; }
  begin() { this.fit(); this.on = true; this.cv.classList.add('on'); if (!document.hidden) this.run(); }
  end() { this.on = false; this.halt(); this.cv.classList.remove('on'); this.g.clearRect(0, 0, this.w || 1, this.h || 1); }
}

// ---------- fireworks ----------
class Fireworks extends Overlay {
  constructor() { super('fx-fw', 3); this.parts = []; this.rockets = []; this.timer = 0; this.onBurst = null; this.count = 0; }
  start(onBurst) {
    this.onBurst = onBurst; this.parts.length = 0; this.rockets.length = 0; this.count = 0;
    this.timer = 0.2; this.slow = reduced(); this.begin();
  }
  stop() { this.end(); this.parts.length = 0; this.rockets.length = 0; }
  launch() {
    const c = PASTELS[(Math.random() * PASTELS.length) | 0];
    this.rockets.push({ x: rnd(0.15, 0.85) * this.w, y: this.h * 0.9, vx: rnd(-4, 4), vy: -rnd(0.95, 1.2) * this.h * 0.55, top: rnd(0.12, 0.42) * this.h, c, tr: [] });
  }
  burst(x, y, c) {
    const n = this.slow ? 32 : 60, sp = rnd(30, 44), two = Math.random() < 0.4, c2 = PASTELS[(Math.random() * PASTELS.length) | 0];
    for (let i = 0; i < n && this.parts.length < 420; i++) {
      const a = (i / n) * Math.PI * 2 + rnd(-0.1, 0.1), s = sp * (two && i % 2 ? 0.6 : 1) * rnd(0.9, 1.05);
      this.parts.push({ x, y, vx: Math.cos(a) * s, vy: Math.sin(a) * s, life: 0, max: rnd(1.6, 2.6), c: two && i % 2 ? c2 : c, k: 0 });
    }
    for (let i = 0; i < 8 && this.parts.length < 420; i++) { // sparkly crackle
      const a = rnd(0, 6.28), s = rnd(3, 12);
      this.parts.push({ x, y, vx: Math.cos(a) * s, vy: Math.sin(a) * s, life: 0, max: rnd(1.6, 2.6), c: [255, 255, 235], k: 1 });
    }
    this.count++; if (this.onBurst) this.onBurst();
  }
  step(dt) {
    const g = this.g, w = this.w, h = this.h;
    this.timer -= dt;
    if (this.timer <= 0) {
      this.launch(); if (!this.slow && Math.random() < 0.35) this.launch();
      this.timer = this.slow ? rnd(2.8, 4) : rnd(0.7, 1.5);
    }
    g.globalCompositeOperation = 'source-over'; g.clearRect(0, 0, w, h);
    if (!this.dusk || this.dusk.h !== h) { this.dusk = g.createLinearGradient(0, 0, 0, h * 0.75); this.dusk.addColorStop(0, 'rgba(28,18,70,.45)'); this.dusk.addColorStop(1, 'rgba(28,18,70,0)'); this.dusk.h = h; }
    g.fillStyle = this.dusk; g.fillRect(0, 0, w, h * 0.75);   // dim the sky a touch so the sparks glow
    g.globalCompositeOperation = 'lighter';
    for (let i = this.rockets.length - 1; i >= 0; i--) {
      const r = this.rockets[i];
      r.x += r.vx * dt; r.y += r.vy * dt; r.vy *= 1 - 0.8 * dt;
      r.tr.push(r.x, r.y); if (r.tr.length > 16) r.tr.splice(0, 2);
      for (let k = 0; k < r.tr.length; k += 2) { g.fillStyle = `rgba(255,235,200,${(k / r.tr.length) * 0.35})`; g.fillRect(r.tr[k] | 0, r.tr[k + 1] | 0, 1, 1); }
      g.fillStyle = 'rgba(255,245,220,.8)'; g.fillRect(r.x | 0, r.y | 0, 1, 1);
      if (r.y <= r.top || r.vy > -6) { this.burst(r.x, r.y, r.c); this.rockets.splice(i, 1); }
    }
    for (let i = this.parts.length - 1; i >= 0; i--) {
      const p = this.parts[i]; p.life += dt;
      if (p.life >= p.max) { this.parts.splice(i, 1); continue; }
      const drag = Math.exp(-1.6 * dt); p.vx *= drag; p.vy = p.vy * drag + 9 * dt; p.x += p.vx * dt; p.y += p.vy * dt;
      const t = 1 - p.life / p.max; let a = t * t;
      if (p.k) a *= Math.random() < 0.5 ? 1 : 0.15;     // twinkle
      const [r, gr, b] = p.c, x = p.x | 0, y = p.y | 0;
      g.fillStyle = `rgba(${r},${gr},${b},${a * 0.3})`; g.fillRect(x - 1, y - 1, 4, 4);   // soft halo
      g.fillStyle = `rgba(${r},${gr},${b},${Math.min(1, a * 1.3)})`; g.fillRect(x, y, 2, 2);
    }
  }
}

// ---------- rain ----------
class Rain extends Overlay {
  constructor() {
    super('fx-rain', 2);
    this.tint = document.createElement('div'); this.tint.className = 'fx-tint'; this.tint.setAttribute('aria-hidden', 'true'); this.stage.appendChild(this.tint);
    this.drops = []; this.runs = []; this.splash = []; this.snd = null; this.layers = [
      { n: 40, len: 6, sp: 70, a: 0.28 }, { n: 30, len: 10, sp: 110, a: 0.4 }, { n: 16, len: 15, sp: 160, a: 0.5 }];
  }
  start(audio) {
    this.begin(); this.t = 0; this.drops.length = 0; this.runs.length = 0; this.splash.length = 0;
    const f = reduced() ? 0.5 : 1;
    this.layers.forEach((L, li) => { for (let i = 0; i < L.n * f; i++) this.drops.push(this.spawn(li, true)); });
    this.tint.classList.add('on'); this.sound(audio);
  }
  stop() {
    this.end(); this.tint.classList.remove('on');
    if (this.snd) { const { g, src, ctx } = this.snd; this.snd = null; try { g.gain.setTargetAtTime(0, ctx.currentTime, 0.2); setTimeout(() => { try { src.stop(); } catch {} }, 1200); } catch {} }
  }
  spawn(li, anywhere) {
    const L = this.layers[li];
    return { li, x: rnd(-0.3, 1) * this.w, y: anywhere ? rnd(0, this.h) : rnd(-L.len, 0), v: L.sp * rnd(0.9, 1.1) };
  }
  sound(audio) {
    if (!audio || !audio.ctx || this.snd) return;
    try {
      const ctx = audio.ctx, len = ctx.sampleRate * 3, b = ctx.createBuffer(1, len, ctx.sampleRate), d = b.getChannelData(0);
      for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
      const src = ctx.createBufferSource(); src.buffer = b; src.loop = true;
      const hp = ctx.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 700;
      const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 3800;
      const g = ctx.createGain(); g.gain.value = 0; g.gain.setTargetAtTime(0.05, ctx.currentTime, 1.2);
      src.connect(hp).connect(lp).connect(g).connect(audio.master); src.start(); this.snd = { g, src, ctx };
    } catch {}
  }
  step(dt) {
    const g = this.g, w = this.w, h = this.h, slant = 0.32, ground = h - 1;
    this.t += dt; const fade = Math.min(1, this.t / 1.5);
    g.clearRect(0, 0, w, h);
    for (let i = 0; i < this.drops.length; i++) {
      const d = this.drops[i], L = this.layers[d.li];
      d.y += d.v * dt; d.x += d.v * slant * dt;
      if (d.y > h - (d.li + 1) * 3 - 2) {   // hit the ground: little splash, sometimes
        if (this.splash.length < 40 && Math.random() < 0.35) this.splash.push({ x: d.x, y: h - rnd(2, 10) , t: 0, li: d.li });
        this.drops[i] = this.spawn(d.li, false); continue;
      }
      g.strokeStyle = `rgba(175,195,225,${L.a * fade})`; g.lineWidth = 1;
      g.beginPath(); g.moveTo(d.x | 0, d.y | 0); g.lineTo((d.x - L.len * slant) | 0, (d.y - L.len) | 0); g.stroke();
    }
    for (let i = this.splash.length - 1; i >= 0; i--) {
      const s = this.splash[i]; s.t += dt;
      if (s.t > 0.3) { this.splash.splice(i, 1); continue; }
      const a = (1 - s.t / 0.3) * 0.35 * fade, k = (s.t * 22) | 0;
      g.fillStyle = `rgba(200,215,240,${a})`; g.fillRect((s.x - k) | 0, (s.y - k * 0.6) | 0, 1, 1); g.fillRect((s.x + k) | 0, (s.y - k * 0.6) | 0, 1, 1);
    }
    // droplets running down the "lens" at the edges
    if (this.runs.length < 5 && Math.random() < dt * 1.2) this.runs.push({ x: rnd(0.04, 0.96) * w, y: rnd(0, h * 0.5), v: rnd(5, 14), life: rnd(1.5, 3), t: 0, s: 0 });
    for (let i = this.runs.length - 1; i >= 0; i--) {
      const r = this.runs[i]; r.t += dt;
      if (r.t > r.life || r.y > h) { this.runs.splice(i, 1); continue; }
      r.s = (Math.random() < 0.05) ? 0 : r.s; r.y += r.v * dt * (0.5 + Math.random()); r.x += Math.sin(r.t * 3 + i) * 0.15;
      const a = Math.min(1, (1 - r.t / r.life) * 1.5) * 0.4 * fade;
      g.fillStyle = `rgba(190,205,230,${a * 0.5})`; g.fillRect(r.x | 0, (r.y - 4) | 0, 1, 4);
      g.fillStyle = `rgba(215,225,245,${a})`; g.fillRect(r.x | 0, r.y | 0, 2, 2);
    }
  }
}

export const effects = { fireworks: null, rain: null };
export function initEffects() {
  effects.fireworks = new Fireworks(); effects.rain = new Rain();
  return effects;
}
export function clearEffects() { effects.fireworks?.stop(); effects.rain?.stop(); }
