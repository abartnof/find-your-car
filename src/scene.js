import * as THREE from 'three';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { clone as skClone } from 'three/examples/jsm/utils/SkeletonUtils.js';
import ASSETS from '../build/assets.js';

// ---------- catalogue ----------
export const CHARACTERS = [
  { id: 'f05', name: 'Dana' }, { id: 'f09', name: 'Priya' },
  { id: 'f12', name: 'Marcy' }, { id: 'f02', name: 'Jo' },
];
export const CARS = [
  { id: 1, name: 'Hatchback', tex: 4 }, { id: 2, name: 'Coupe', tex: 3 },
  { id: 3, name: 'Roadster', tex: 3 }, { id: 4, name: 'Wagon', tex: 4 },
  { id: 5, name: 'Sedan', tex: 3 }, { id: 7, name: 'Vintage', tex: 6 }, { id: 8, name: 'Pickup', tex: 3 },
];

export const STEPS = 10;
const LOT_END = 68;             // z distance from start to goal car
const STOP_GAP = 4.7;           // she stops this far from the car's origin on win
export const stepLen = () => (LOT_END - STOP_GAP) / STEPS;

// ---------- loaders / caches ----------
const texLoader = new THREE.TextureLoader();
const texCache = {};
function tex(key) {
  if (texCache[key]) return texCache[key];
  const t = texLoader.load(ASSETS[key]);
  t.magFilter = t.minFilter = THREE.NearestFilter;
  t.colorSpace = THREE.SRGBColorSpace;
  t.generateMipmaps = false;
  return (texCache[key] = t);
}
function b64buf(uri) {
  const s = atob(uri.split(',')[1]);
  const a = new Uint8Array(s.length);
  for (let i = 0; i < s.length; i++) a[i] = s.charCodeAt(i);
  return a.buffer;
}
const objSrc = (id) => atob(ASSETS[`cars/car${id}.obj`].split(',')[1]);
const objLoader = new OBJLoader();
const carProto = {};
function buildCar(id, texIdx) {
  carProto[id] ||= objLoader.parse(objSrc(id));
  const g = carProto[id].clone(true);
  const mat = new THREE.MeshLambertMaterial({ map: tex(`cars/car${id}_${texIdx}.png`), side: THREE.DoubleSide, transparent: false });
  g.traverse((o) => { if (o.isMesh) o.material = mat; });
  g.scale.setScalar(0.78);
  const wrap = new THREE.Group();
  wrap.add(g);
  return wrap;
}

const fbxLoader = new FBXLoader();
const fbxProto = {};
function buildPerson(id) {
  fbxProto[id] ||= fbxLoader.parse(b64buf(ASSETS[`chars/${id}.fbx`]), '');
  const src = fbxProto[id];
  const clone = skClone(src);
  const m = new THREE.MeshLambertMaterial({ map: tex(`chars/${id}.jpg`), side: THREE.DoubleSide });
  clone.traverse((o) => { if (o.isMesh) { o.material = m; o.frustumCulled = false; } });
  clone.scale.setScalar(0.0041);
  return clone;
}

// ---------- walker rig (procedural animation on Mixamo skeleton) ----------
class Walker {
  constructor(id) {
    this.model = buildPerson(id);
    this.pivot = new THREE.Group();
    this.pivot.rotation.y = Math.PI;            // Mixamo faces +Z; we walk toward -Z
    this.pivot.add(this.model);
    this.bones = {};
    this.model.traverse((o) => { if (o.isBone) this.bones[o.name.replace('mixamorig', '')] = o; });
    this.model.updateMatrixWorld(true);
    this.rest = {};
    for (const [n, b] of Object.entries(this.bones)) {
      const pq = new THREE.Quaternion();
      if (b.parent) b.parent.getWorldQuaternion(pq);
      this.rest[n] = { q0: b.quaternion.clone(), pq, pqi: pq.clone().invert() };
    }
    // how far each upper arm already hangs below horizontal in the rest pose (rigs differ: T vs A pose)
    const wp = (n) => this.bones[n].getWorldPosition(new THREE.Vector3());
    const hang = (a, f, sx) => { const v = wp(f).sub(wp(a)); return Math.atan2(-v.y, v.x * sx); };
    this.armRest = { L: hang('LeftArm', 'LeftForeArm', -1), R: hang('RightArm', 'RightForeArm', 1) };
    this.phase = 0; this.moving = 0; this.shrug = 0; this.cheer = 0;
    this.hipsY = this.bones.Hips.position.y;
  }
  // rotate bone by world-space axis/angle pairs [[ax,ay,az,ang],...] relative to its rest pose
  rot(name, ...rs) {
    const b = this.bones[name]; if (!b) return;
    const r = this.rest[name];
    const R = new THREE.Quaternion(), t = new THREE.Quaternion();
    for (const [ax, ay, az, ang] of rs) R.multiply(t.setFromAxisAngle(new THREE.Vector3(ax, ay, az), ang));
    b.quaternion.copy(r.pqi).multiply(R).multiply(r.pq).multiply(r.q0);
  }
  update(dt, speed) {
    // everything eases: no snapping between idle, walking and gestures
    const target = Math.min(speed / 2.2, 1);
    this.moving += (target - this.moving) * Math.min(1, dt * 3);
    this.t = (this.t || 0) + dt;
    const prev = this.phase;
    this.phase += dt * (0.6 + speed) * 2.0 * (this.moving > 0.02 ? 1 : 0);
    if (this.onStep && Math.floor(prev / Math.PI) !== Math.floor(this.phase / Math.PI)) this.onStep();
    const m = this.moving, s = Math.sin(this.phase), c = Math.cos(this.phase), T = this.t;
    this.shrug = Math.max(0, this.shrug - dt); this.cheer = Math.max(0, this.cheer - dt);
    const ease = (x) => Math.sin(Math.max(0, Math.min(1, x)) * Math.PI);   // 0 → 1 → 0
    const sh = this.shrug > 0 ? ease(1 - this.shrug / 2.4) : 0;
    const ch = this.cheer > 0 ? ease(1 - this.cheer / 2.0) : 0;
    const breathe = Math.sin(T * 1.4) * (1 - m);
    const A = 0.36 * m;
    this.rot('LeftUpLeg', [1, 0, 0, s * A]);
    this.rot('RightUpLeg', [1, 0, 0, -s * A]);
    this.rot('LeftLeg', [1, 0, 0, Math.max(0, -s) * 0.45 * m]);
    this.rot('RightLeg', [1, 0, 0, Math.max(0, s) * 0.45 * m]);
    // arms hang with a loose swing opposite the legs; a gentle lift for gestures
    const down = 1.38 - ch * 0.7 - sh * 0.25 + breathe * 0.015;   // target angle below horizontal
    this.rot('LeftArm', [0, 0, 1, down - this.armRest.L], [1, 0, 0, -s * 0.3 * m]);
    this.rot('RightArm', [0, 0, 1, -(down - this.armRest.R)], [1, 0, 0, s * 0.3 * m]);
    this.rot('LeftForeArm', [1, 0, 0, -0.25 - 0.15 * m - ch * 0.3]);
    this.rot('RightForeArm', [1, 0, 0, -0.25 - 0.15 * m - ch * 0.3]);
    this.rot('Spine1', [0, 1, 0, s * 0.07 * m], [1, 0, 0, breathe * 0.012]);
    this.rot('Spine2', [0, 1, 0, -s * 0.05 * m]);
    // a slow, curious head tilt when she gets one wrong; otherwise a drifting look
    this.rot('Head', [0, 0, 1, sh * 0.22], [0, 1, 0, Math.sin(T * 0.5) * 0.06 * (1 - m) - sh * 0.25]);
    // soft vertical bob + hip sway
    this.bones.Hips.position.y = this.hipsY + (1 - Math.cos(2 * this.phase)) * 0.5 * 1.1 * m;
    this.rot('Hips', [0, 1, 0, -s * 0.06 * m], [0, 0, 1, s * 0.025 * m]);
  }
}


// ---------- 2D parallax sky: drifting pixel clouds, birds, a plane, stars and a moon ----------
function pixelCanvas(w, h, draw, threshold = 90) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const x = c.getContext('2d'); draw(x, w, h);
  const im = x.getImageData(0, 0, w, h), d = im.data;      // crisp PSX-style alpha edges
  for (let i = 3; i < d.length; i += 4) d[i] = d[i] > threshold ? 255 : 0;
  x.putImageData(im, 0, 0);
  const t = new THREE.CanvasTexture(c); t.magFilter = t.minFilter = THREE.NearestFilter; t.generateMipmaps = false; t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
function cloudTexture(seed) {
  let r = seed * 9301 + 49297; const rnd = () => ((r = (r * 9301 + 49297) % 233280) / 233280);
  return pixelCanvas(64, 20, (x, w, h) => {
    const blobs = 5 + (rnd() * 4 | 0);
    const spots = [];
    for (let i = 0; i < blobs; i++) spots.push([10 + rnd() * (w - 20), 9 + rnd() * 4, 6 + rnd() * 8, 3 + rnd() * 4]);
    for (const [col, dy, shrink] of [['#8a5a8f', 2, 0], ['#ffffff', 0, 0], ['#ffe9f0', -1.5, 1]]) {
      x.fillStyle = col;
      for (const [cx, cy, rx, ry] of spots) { x.beginPath(); x.ellipse(cx, cy + dy, rx - shrink, ry - shrink * 0.5, 0, 0, 7); x.fill(); }
    }
  });
}
const birdFrame = (flap) => pixelCanvas(14, 8, (x) => {
  x.strokeStyle = '#2a1a3a'; x.lineWidth = 1.6; x.beginPath();
  x.moveTo(1, flap ? 1 : 3); x.lineTo(5, flap ? 4 : 5); x.lineTo(7, 4); x.lineTo(9, flap ? 4 : 5); x.lineTo(13, flap ? 1 : 3); x.stroke();
}, 70);
const planeTex = () => pixelCanvas(32, 10, (x) => {
  x.fillStyle = '#e9d7e6'; x.fillRect(4, 4, 24, 2); x.fillRect(26, 3, 3, 1); x.fillRect(12, 2, 4, 1); x.fillRect(12, 7, 4, 1);
  x.fillStyle = '#b79ab8'; x.fillRect(24, 1, 3, 3);
});
const dotTex = (rgb) => { const c = document.createElement('canvas'); c.width = c.height = 16; const x = c.getContext('2d'); const g = x.createRadialGradient(8, 8, 0, 8, 8, 8); g.addColorStop(0, `rgba(${rgb},1)`); g.addColorStop(1, `rgba(${rgb},0)`); x.fillStyle = g; x.fillRect(0, 0, 16, 16); return new THREE.CanvasTexture(c); };
const moonTex = () => pixelCanvas(24, 24, (x) => {
  x.fillStyle = '#fff3d0'; x.beginPath(); x.arc(12, 12, 8, 0, 7); x.fill();
  x.globalCompositeOperation = 'destination-out'; x.beginPath(); x.arc(16, 9, 7.5, 0, 7); x.fill();
});

class Sky {
  constructor(scene) {
    this.layers = [];
    const mk = (f, drift) => { const g = new THREE.Group(); g.renderOrder = 1; scene.add(g); const L = { g, f, drift, items: [] }; this.layers.push(L); return L; };
    const spr = (L, map, R, az, el, w, h, color = 0xffffff, op = 1) => {
      const m = new THREE.SpriteMaterial({ map, color, fog: false, transparent: true, opacity: op, depthWrite: false });
      const s = new THREE.Sprite(m); s.scale.set(w, h, 1); s.renderOrder = 1; L.g.add(s);
      const it = { s, R, az, el }; L.items.push(it); return it;
    };
    this.spr = spr;
    const clouds = [1, 2, 3, 4, 5].map(cloudTexture);
    let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    // stars + moon: nearly fixed (f ≈ 1) so they barely parallax
    const far = mk(0.995, 0.0004);
    const star = dotTex('255,240,220');
    for (let i = 0; i < 46; i++) { const it = spr(far, star, 290, (rnd() - 0.5) * 7, 0.3 + rnd() * 0.6, 2.2, 2.2, 0xffffff, 0.35 + rnd() * 0.5); it.tw = rnd() * 6; }
    this.stars = far.items.slice();
    spr(far, moonTex(), 285, -0.55, 0.5, 26, 26, 0xfff3d0, 0.95);
    // three cloud decks, nearer = faster + stronger parallax + warmer
    const decks = [[0.99, 0.0035, 270, 0.14, 0.42, 74, 0xb78ac4, 7], [0.95, 0.007, 190, 0.15, 0.45, 56, 0xe58fb0, 7], [0.86, 0.012, 120, 0.2, 0.5, 42, 0xffb09a, 6]];
    for (const [f, drift, R, e0, e1, w, tint, n] of decks) {
      const L = mk(f, drift);
      for (let i = 0; i < n; i++) spr(L, clouds[(rnd() * 5) | 0], R, (i / n) * 6.28 - 3.14 + rnd() * 0.4, e0 + rnd() * (e1 - e0), w * (0.7 + rnd() * 0.6), w * 0.31 * (0.7 + rnd() * 0.6), tint, 0.9);
    }
    // birds: a loose flock crossing in the mid-ground, gently flapping
    this.birdL = mk(0.9, 0);
    this.birdTex = [birdFrame(false), birdFrame(true)];
    this.birds = [];
    for (let i = 0; i < 6; i++) {
      const it = spr(this.birdL, this.birdTex[0], 95, -2.6 + i * 0.05, 0.2 + rnd() * 0.08 + (i % 2) * 0.04, 3.2, 1.8);
      it.ph = rnd() * 6; it.v = 0.045 + rnd() * 0.006; this.birds.push(it);
    }
    // a plane, high and far, with a soft contrail and slow blinking light
    this.planeL = mk(0.985, 0);
    this.plane = spr(this.planeL, planeTex(), 262, 1.6, 0.4, 13, 4);
    this.trail = [];
    for (let i = 1; i <= 9; i++) this.trail.push(spr(this.planeL, dotTex('255,225,235'), 262, 1.6 + i * 0.012, 0.4, 4.5, 2.2, 0xffffff, 0.5 - i * 0.045));
    this.light = spr(this.planeL, dotTex('255,70,70'), 262, 1.6, 0.4, 3.2, 3.2, 0xffffff, 1);
  }
  update(dt, t, camPos) {
    for (const L of this.layers) {
      L.g.position.copy(camPos).multiplyScalar(L.f);
      for (const it of L.items) {
        if (!it.own) it.az += L.drift * dt;
        if (it.az > 3.14159 * 1.0 && L.drift > 0.001) it.az -= 6.2832;
        const ce = Math.cos(it.el);
        it.s.position.set(Math.sin(it.az) * ce * it.R, Math.sin(it.el) * it.R, -Math.cos(it.az) * ce * it.R);
      }
    }
    for (const st of this.stars) st.s.material.opacity = 0.3 + 0.35 * (0.5 + 0.5 * Math.sin(t * 0.8 + st.tw));
    for (const b of this.birds) {
      b.own = true; b.az += b.v * dt; if (b.az > 3.0) b.az = -3.0;
      b.s.material.map = this.birdTex[Math.sin(t * 5 + b.ph) > 0.2 ? 1 : 0];
      b.el += Math.sin(t * 0.7 + b.ph) * 0.00008;
    }
    this.plane.own = true; this.plane.az += 0.0085 * dt; if (this.plane.az > 3.0) this.plane.az = -3.0;
    this.trail.forEach((p, i) => { p.own = true; p.az = this.plane.az - (i + 1) * 0.012 * 1.0; });
    this.light.own = true; this.light.az = this.plane.az + 0.012; this.light.s.material.opacity = Math.sin(t * 3) > 0.6 ? 1 : 0.05;
  }
}



// ---------- the lot ----------
export class Lot {
  constructor(canvas) {
    this.canvas = canvas;
    this.renderer = new THREE.WebGLRenderer({ canvas, antialias: false, powerPreference: 'high-performance' });
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    this.scene = new THREE.Scene();
    const fogCol = new THREE.Color(0x5a3f6e);
    this.scene.fog = new THREE.Fog(fogCol, 14, 95);
    this.camera = new THREE.PerspectiveCamera(58, 1, 0.1, 400);
    this.pixel = 2.4;
    this.clock = new THREE.Clock();
    this.stepZ = 0; this.z = 0; this.speed = 0;
    this.mode = 'menu';          // menu | play | drive
    this.time = 0; this.shake = 0;
    this.camPos = new THREE.Vector3(); this.camLook = new THREE.Vector3();
    this.buildWorld();
    this.resize();
    addEventListener('resize', () => this.resize());
    this.loop = this.loop.bind(this);
  }

  buildWorld() {
    const sc = this.scene;
    sc.add(new THREE.HemisphereLight(0xffe0c0, 0x6a5a88, 2.3));
    const sun = new THREE.DirectionalLight(0xffc08a, 2.2);
    sun.position.set(-30, 18, -60); sc.add(sun);

    // sky dome with vertex-coloured sunset
    const sky = new THREE.SphereGeometry(300, 24, 12);
    const cols = [], p = sky.attributes.position;
    const top = new THREE.Color(0x2b2058), mid = new THREE.Color(0xc4567a), hor = new THREE.Color(0xffa860);
    for (let i = 0; i < p.count; i++) {
      const h = Math.max(0, p.getY(i) / 300), c = new THREE.Color();
      if (h < 0.18) c.copy(hor).lerp(mid, h / 0.18); else c.copy(mid).lerp(top, Math.min(1, (h - 0.18) / 0.5));
      cols.push(c.r, c.g, c.b);
    }
    sky.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
    const skyMesh = new THREE.Mesh(sky, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide, fog: false }));
    sc.add(skyMesh); this.sky = skyMesh;
    this.skyLayers = new Sky(sc);
    sc.fog.color.set(0xb0658a);

    // ground: asphalt with noise
    const cv = document.createElement('canvas'); cv.width = cv.height = 128;
    const g = cv.getContext('2d');
    g.fillStyle = '#3c3a44'; g.fillRect(0, 0, 128, 128);
    for (let i = 0; i < 1800; i++) { const v = 40 + Math.random() * 40 | 0; g.fillStyle = `rgb(${v},${v - 2},${v + 8})`; g.fillRect(Math.random() * 128, Math.random() * 128, 2, 2); }
    const at = new THREE.CanvasTexture(cv); at.wrapS = at.wrapT = THREE.RepeatWrapping; at.repeat.set(30, 80);
    at.magFilter = at.minFilter = THREE.NearestFilter; at.colorSpace = THREE.SRGBColorSpace;
    const ground = new THREE.Mesh(new THREE.PlaneGeometry(120, 260), new THREE.MeshLambertMaterial({ map: at }));
    ground.rotation.x = -Math.PI / 2; ground.position.set(0, 0, -100); sc.add(ground);

    // stall lines + centre arrows
    const lineMat = new THREE.MeshBasicMaterial({ color: 0xd9d6c8 });
    const lineGeo = new THREE.PlaneGeometry(0.14, 5.2);
    const stalls = [];
    for (let z = 6; z > -LOT_END - 30; z -= 3.3) for (const side of [-1, 1]) stalls.push([side, z]);
    const inst = new THREE.InstancedMesh(lineGeo, lineMat, stalls.length);
    const mm = new THREE.Matrix4();
    stalls.forEach(([side, z], i) => { mm.makeRotationX(-Math.PI / 2); mm.setPosition(side * 7.2, 0.02, z); inst.setMatrixAt(i, mm); });
    sc.add(inst);
    const edgeGeo = new THREE.PlaneGeometry(0.14, 260);
    for (const side of [-1, 1]) { const e = new THREE.Mesh(edgeGeo, lineMat); e.rotation.x = -Math.PI / 2; e.position.set(side * 4.6, 0.02, -100); sc.add(e); }
    const dash = new THREE.PlaneGeometry(0.18, 1.6);
    const dashes = new THREE.InstancedMesh(dash, new THREE.MeshBasicMaterial({ color: 0xe8c14a }), 90);
    for (let i = 0; i < 90; i++) { mm.makeRotationX(-Math.PI / 2); mm.setPosition(0, 0.02, 6 - i * 3.4); dashes.setMatrixAt(i, mm); }
    sc.add(dashes);

    // parked cars (dummies)
    this.dummies = new THREE.Group(); sc.add(this.dummies);
    let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    for (let z = 2; z > -LOT_END - 24; z -= 3.3) {
      for (const side of [-1, 1]) {
        if (rnd() < 0.3) continue;
        if (z < -LOT_END + 8 && Math.abs(side) > 0 && z > -LOT_END - 8 && false) continue;
        const car = CARS[(rnd() * CARS.length) | 0];
        const c = buildCar(car.id, (rnd() * car.tex) | 0);
        c.scale.setScalar(0.96);
        c.position.set(side * 7.1, 0, z - 1.6);
        c.rotation.y = side > 0 ? -Math.PI / 2 : Math.PI / 2;   // nose toward the aisle? alternate for variety
        if (rnd() < 0.5) c.rotation.y += Math.PI;
        this.dummies.add(c);
      }
    }

    // lamp posts
    const poleMat = new THREE.MeshLambertMaterial({ color: 0x2b2b35 });
    const glowTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d'); const gr = x.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,230,160,1)'); gr.addColorStop(0.3, 'rgba(255,200,110,.5)'); gr.addColorStop(1, 'rgba(255,180,90,0)'); x.fillStyle = gr; x.fillRect(0, 0, 64, 64); return new THREE.CanvasTexture(c); })();
    this.glowTex = glowTex;
    for (let z = -4; z > -LOT_END - 30; z -= 16) for (const side of [-1, 1]) {
      const pole = new THREE.Mesh(new THREE.BoxGeometry(0.2, 7, 0.2), poleMat); pole.position.set(side * 10.6, 3.5, z); sc.add(pole);
      const arm = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.14, 0.14), poleMat); arm.position.set(side * 9.8, 7, z); sc.add(arm);
      const bulb = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, fog: false, blending: THREE.AdditiveBlending, depthWrite: false }));
      bulb.scale.setScalar(5); bulb.position.set(side * 9.1, 6.8, z); sc.add(bulb);
    }

    // backdrop: store at the end + skyline blocks
    const bd = new THREE.Group(); bd.position.set(0, 0, -LOT_END - 22); sc.add(bd);
    const wallMat = new THREE.MeshLambertMaterial({ color: 0x6d5a80 });
    const store = new THREE.Mesh(new THREE.BoxGeometry(60, 9, 8), wallMat); store.position.y = 4.5; bd.add(store);
    const winCv = document.createElement('canvas'); winCv.width = 64; winCv.height = 16;
    const wg = winCv.getContext('2d'); wg.fillStyle = '#ffd98a'; wg.fillRect(0, 0, 64, 16); wg.fillStyle = '#a8704a'; for (let i = 0; i < 64; i += 8) wg.fillRect(i, 0, 1, 16);
    const wt = new THREE.CanvasTexture(winCv); wt.magFilter = THREE.NearestFilter; wt.colorSpace = THREE.SRGBColorSpace;
    const glass = new THREE.Mesh(new THREE.PlaneGeometry(50, 4), new THREE.MeshBasicMaterial({ map: wt })); glass.position.set(0, 3, 4.05); bd.add(glass);
    const sign = new THREE.Mesh(new THREE.BoxGeometry(14, 2.2, 0.4), new THREE.MeshBasicMaterial({ color: 0xff5a7a })); sign.position.set(0, 7.2, 4.1); bd.add(sign);
    for (let i = -6; i <= 6; i++) { if (Math.abs(i) < 2) continue; const h = 8 + rnd() * 22; const b = new THREE.Mesh(new THREE.BoxGeometry(7, h, 7), new THREE.MeshLambertMaterial({ color: new THREE.Color().setHSL(0.75, 0.25, 0.22 + rnd() * 0.1) })); b.position.set(i * 14, h / 2, -24); bd.add(b); }
    // trees / hedges along the sides
    const hedge = new THREE.MeshLambertMaterial({ color: 0x2f5a3a });
    for (let z = 4; z > -LOT_END - 30; z -= 9) for (const side of [-1, 1]) {
      const b = new THREE.Mesh(new THREE.BoxGeometry(2.6, 1.6, 2.6), hedge); b.position.set(side * 13.5, 0.8, z); sc.add(b);
    }

    // the goal car
    this.goal = new THREE.Group();
    this.goal.position.set(0, 0, -LOT_END);
    this.goal.rotation.y = Math.PI;   // OBJ nose is +Z -> face away (-Z) ... set in setCar
    sc.add(this.goal);
    this.hazard = [];
    for (const sx of [-1.0, 1.0]) {
      const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, color: 0xffa020, fog: false, blending: THREE.AdditiveBlending, depthWrite: false }));
      s.scale.setScalar(2.4); s.position.set(sx * 0.85, 1.0, 2.4); this.goalHaz = this.goalHaz || []; this.goalHaz.push(s); this.goal.add(s);
    }
    const beam = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 1.4, 60, 12, 1, true), new THREE.MeshBasicMaterial({ color: 0xffd27a, transparent: true, opacity: 0.22, fog: false, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide }));
    beam.position.set(0, 30, 0); this.beam = beam; this.goal.add(beam);

    // woman
    this.walkerHolder = new THREE.Group(); sc.add(this.walkerHolder);

    // a couple of bystanders
    this.extras = new THREE.Group(); sc.add(this.extras);
    const ex = [['m04', 5.4, -22, 0.6], ['m11', -5.6, -38, -0.8], ['m04', 5.0, -52, 2.4]];
    this.extraWalkers = [];
    for (const [id, x, z, ry] of ex) {
      const w = new Walker(id); w.pivot.position.set(x, 0, z); w.pivot.rotation.y = ry; w.t = Math.random() * 20; w.update(0, 0); this.extras.add(w.pivot); this.extraWalkers.push(w);
    }
  }

  setCharacter(id) {
    while (this.walkerHolder.children.length) this.walkerHolder.remove(this.walkerHolder.children[0]);
    this.walker = new Walker(id);
    this.walker.onStep = () => this.onStep && this.onStep();
    this.walkerHolder.add(this.walker.pivot);
    this.walker.pivot.rotation.y = Math.PI;
    this.walkerHolder.position.set(0, 0, this.z);
  }
  setCar(carIdx, texIdx) {
    while (this.goal.children.length > 3) this.goal.remove(this.goal.children[this.goal.children.length - 1]);
    for (const c of [...this.goal.children]) if (c.userData.isCar) this.goal.remove(c);
    const c = buildCar(CARS[carIdx].id, texIdx); c.userData.isCar = true; c.scale.setScalar(1.12);
    this.goal.add(c); this.goalCar = c;
  }

  resize() {
    const w = this.canvas.clientWidth || 360, h = this.canvas.clientHeight || 240;
    this.renderer.setPixelRatio(1);
    this.renderer.setSize(Math.max(80, Math.round(w / this.pixel)), Math.max(60, Math.round(h / this.pixel)), false);
    this.camera.aspect = w / h;
    this.camera.fov = w / h < 1 ? 66 : 54;
    this.camera.updateProjectionMatrix();
  }

  // game hooks
  reset() {
    this.z = 0; this.stepZ = 0; this.mode = 'menu';
    this.walkerHolder.visible = true;
    this.walkerHolder.position.set(0, 0, 0);
    this.walkerHolder.rotation.set(0, 0, 0);
    this.goal.position.set(0, 0, -LOT_END); this.driveSpeed = 0;
    this.camLook.set(0, 11, -10);
  }
  advance() { this.stepZ -= stepLen(); }
  get remaining() { return Math.abs(this.z - this.stepZ); }
  stumble() { this.walker.shrug = 2.4; }
  cheer() { this.walker.cheer = 2.0; }
  progress() { return -this.stepZ / stepLen(); }
  async drive(audio) {
    // she hops in, the car pulls away
    this.mode = 'drive';
    this.stepZ = -LOT_END + 1.3;                 // walk alongside to the driver's door
    for (let i = 0; i < 80 && this.z - this.stepZ > 0.05; i++) await wait(100);
    if (this.onArrive) this.onArrive();   // she is at the car: celebrate
    await wait(300);
    audio.play('Car_Door_Open', 0.35); await wait(900);
    this.walkerHolder.visible = false;
    await wait(300); audio.play('Car_Door_Close', 0.35); await wait(700);
    audio.play('Car_Engine_Start_Up', 0.3); await wait(1800);
    audio.play('Car_Acceleration', 0.25); this.driveSpeed = 0.01;
    await wait(3600);
  }

  loop() {
    requestAnimationFrame(this.loop);
    const dt = Math.min(0.05, this.clock.getDelta());
    this.time += dt;
    // walk toward step target
    let spd = 0;
    if (this.mode !== 'drive' || this.walkerHolder.visible) {
      const d = this.z - this.stepZ;
      if (d > 0.02) { spd = Math.min(1.9, 0.5 + d * 0.6); this.z -= Math.min(d, spd * dt); }
    }
    if (this.walker) {
      this.walker.update(dt, spd);
      this.walkerHolder.position.z = this.z;
      
      if (this.mode === 'drive' && this.walkerHolder.visible) { this.walkerHolder.position.x += (-1.7 - this.walkerHolder.position.x) * dt * 2;
        // keep facing the way she walks, then ease round to face the driver's door (car is at +x of her)
        const want = this.z - this.stepZ > 0.25 ? Math.PI : Math.PI / 2;
        this.walker.pivot.rotation.y += (want - this.walker.pivot.rotation.y) * Math.min(1, dt * 2.5); }
      if (this.mode === 'play' && this.remaining < 0.05 && this.winWalkAside) { /* noop */ }
    }
    for (const w of this.extraWalkers) w.update(dt, 0);
    // goal car + hazards
    const blink = 0.55 + 0.45 * Math.sin(this.time * 2.2);
    for (const h of this.goalHaz) h.material.opacity = blink;
    const near = Math.max(0, Math.min(1, (this.z + LOT_END - 8) / 40));
    this.beam.material.opacity = (0.05 + 0.16 * near) * (0.8 + 0.2 * Math.sin(this.time * 0.9));
    if (this.mode === 'drive' && this.driveSpeed > 0) {
      this.driveSpeed = Math.min(9, this.driveSpeed + dt * 1.6);
      this.goal.position.z -= this.driveSpeed * dt;
      this.beam.visible = false;
    } else this.beam.visible = true;

    // camera
    const cam = this.camera;
    let tp, tl;
    if (this.mode === 'menu') {
      // menu: a still camera tilted up at the sky (clouds, birds, plane drift past); it settles on her when the game starts
      tp = new THREE.Vector3(1.1, 2.0, this.z + 4.6);
      tl = new THREE.Vector3(0, 11, this.z - 10);
    } else if (this.mode === 'drive') {
      tp = new THREE.Vector3(-2.6, 1.9, Math.max(this.goal.position.z + 11, this.z + 7));
      tl = new THREE.Vector3(0, 4.2, this.goal.position.z - 5);
      if (!this.walkerHolder.visible && !this.goalCar.userData.driving) this.goalCar.userData.driving = 1;
    } else {
      tp = new THREE.Vector3(1.1 + Math.sin(this.time * 0.4) * 0.25, 2.0 + Math.sin(this.time * 0.31) * 0.06, this.z + 4.6);
      tl = new THREE.Vector3(0, 1.35, this.z - 7);
    }
    const k = this.snap ? 1 : 1 - Math.exp(-dt * (this.mode === 'menu' ? 2.2 : 1.6));
    this.camPos.lerp(tp, this.camPos.lengthSq() ? k : 1);
    this.camLook.lerp(tl, k);
    cam.position.copy(this.camPos);
    if (this.shake > 0) { this.shake -= dt; cam.position.x += (Math.random() - 0.5) * 0.12; cam.position.y += (Math.random() - 0.5) * 0.1; }
    cam.lookAt(this.camLook);
    this.sky.position.copy(cam.position);
    this.skyLayers.update(dt, this.time, cam.position);
    this.renderer.render(this.scene, cam);
  }
  start() { this.camPos.set(1.1, 2.0, 4.6); this.camLook.set(0, 11, -10); this.loop(); }
}
export const wait = (ms) => new Promise((r) => setTimeout(r, ms));
