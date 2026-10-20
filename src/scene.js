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
  { id: 5, name: 'Sedan', tex: 3 }, { id: 6, name: 'Van', tex: 1 },
  { id: 7, name: 'Compact', tex: 6 }, { id: 8, name: 'Pickup', tex: 3 },
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
    this.phase = 0; this.moving = 0; this.shrug = 0; this.cheer = 0;
    this.hipsY = this.bones.Hips.position.y;
  }
  // rotate bone by a world-space axis/angle relative to its rest pose
  rot(name, ax, ay, az, ang) {
    const b = this.bones[name]; if (!b) return;
    const r = this.rest[name];
    const R = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(ax, ay, az), ang);
    b.quaternion.copy(r.pqi).multiply(R).multiply(r.pq).multiply(r.q0);
  }
  update(dt, speed) {
    const target = Math.min(speed / 3, 1);
    this.moving += (target - this.moving) * Math.min(1, dt * 8);
    this.phase += dt * speed * 2.6;
    const m = this.moving, s = Math.sin(this.phase), c = Math.cos(this.phase);
    this.shrug = Math.max(0, this.shrug - dt); this.cheer = Math.max(0, this.cheer - dt);
    const sh = this.shrug > 0 ? Math.sin((1 - this.shrug / 1.2) * Math.PI) : 0;
    const ch = this.cheer > 0 ? Math.sin((1 - this.cheer / 1.0) * Math.PI) : 0;
    const A = 0.55 * m;
    // legs swing about world X
    this.rot('LeftUpLeg', 1, 0, 0, s * A);
    this.rot('RightUpLeg', 1, 0, 0, -s * A);
    this.rot('LeftLeg', 1, 0, 0, Math.max(0, -s) * 0.9 * m);
    this.rot('RightLeg', 1, 0, 0, Math.max(0, s) * 0.9 * m);
    // arms: down from T-pose about Z, then swing about X; shrug/cheer lift them
    const down = 1.28 - sh * 0.5 - ch * 1.8;
    this.rot('LeftArm', 0, 0, 1, down);
    this.rot('RightArm', 0, 0, 1, -down);
    this.rot('LeftForeArm', 0, 1, 0, 0.0);
    this.rot('RightForeArm', 0, 1, 0, 0.0);
    const sw = 0.35 * m;
    this.bones.LeftArm.quaternion.premultiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(1, 0, 0), -s * sw * 0.0));
    this.rot('Spine1', 0, 1, 0, s * 0.08 * m);
    this.rot('Head', 0, 1, 0, sh * Math.sin(this.phase * 0.0 + performance.now() / 70) * 0.5);
    // bounce
    this.bones.Hips.position.y = this.hipsY + Math.abs(c) * 3.2 * m - ch * 0 + (ch > 0 ? Math.abs(Math.sin(performance.now() / 90)) * 6 : 0);
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
      const w = new Walker(id); w.pivot.position.set(x, 0, z); w.pivot.rotation.y = ry; w.update(0, 0); this.extras.add(w.pivot); this.extraWalkers.push(w);
    }
  }

  setCharacter(id) {
    while (this.walkerHolder.children.length) this.walkerHolder.remove(this.walkerHolder.children[0]);
    this.walker = new Walker(id);
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
    this.camLook.set(0, 1.4, -8);
  }
  advance() { this.stepZ -= stepLen(); }
  get remaining() { return Math.abs(this.z - this.stepZ); }
  stumble() { this.walker.shrug = 1.2; this.shake = 0.35; }
  cheer() { this.walker.cheer = 1.0; }
  progress() { return -this.stepZ / stepLen(); }
  async drive(audio) {
    // she hops in, the car pulls away
    this.mode = 'drive';
    this.stepZ = -LOT_END + 1.3;                 // walk alongside to the driver's door
    for (let i = 0; i < 80 && this.z - this.stepZ > 0.05; i++) await wait(100);
    await wait(300);
    audio.play('Car_Door_Open'); await wait(700);
    this.walkerHolder.visible = false;
    await wait(300); audio.play('Car_Door_Close'); await wait(500);
    audio.play('Car_Engine_Start_Up'); await wait(1400);
    audio.play('Car_Acceleration'); this.driveSpeed = 0.01;
    await wait(2600);
  }

  loop() {
    requestAnimationFrame(this.loop);
    const dt = Math.min(0.05, this.clock.getDelta());
    this.time += dt;
    // walk toward step target
    let spd = 0;
    if (this.mode !== 'drive' || this.walkerHolder.visible) {
      const d = this.z - this.stepZ;
      if (d > 0.02) { spd = Math.min(3.4, 0.6 + d * 2.5); this.z -= Math.min(d, spd * dt); }
    }
    if (this.walker) {
      this.walker.update(dt, spd);
      this.walkerHolder.position.z = this.z;
      if (this.mode === 'menu') { this.walker.moving *= 0.9; }
      if (this.mode === 'drive' && this.walkerHolder.visible) { this.walkerHolder.position.x += (-1.7 - this.walkerHolder.position.x) * dt * 2; this.walker.pivot.rotation.y = Math.PI * 1.5; }
      if (this.mode === 'play' && this.remaining < 0.05 && this.winWalkAside) { /* noop */ }
    }
    for (const w of this.extraWalkers) w.update(dt, 0);
    // goal car + hazards
    const blink = Math.sin(this.time * 7) > 0 ? 1 : 0.15;
    for (const h of this.goalHaz) h.material.opacity = blink;
    const near = Math.max(0, Math.min(1, (this.z + LOT_END - 8) / 40));
    this.beam.material.opacity = 0.05 + 0.2 * near;
    if (this.mode === 'drive' && this.driveSpeed > 0) {
      this.driveSpeed = Math.min(14, this.driveSpeed + dt * 6);
      this.goal.position.z -= this.driveSpeed * dt;
      this.beam.visible = false;
    } else this.beam.visible = true;

    // camera
    const cam = this.camera;
    let tp, tl;
    if (this.mode === 'menu') {
      const a = this.time * 0.35;
      tp = new THREE.Vector3(Math.sin(a) * 3.4, 1.7, this.z + Math.cos(a) * 3.4);
      tl = new THREE.Vector3(0, 1.1, this.z - 1.5);
    } else if (this.mode === 'drive') {
      tp = new THREE.Vector3(-2.6, 1.9, Math.max(this.goal.position.z + 11, this.z + 7));
      tl = new THREE.Vector3(0, 1, this.goal.position.z - 3);
      if (!this.walkerHolder.visible && !this.goalCar.userData.driving) this.goalCar.userData.driving = 1;
    } else {
      tp = new THREE.Vector3(1.1, 2.0, this.z + 4.4);
      tl = new THREE.Vector3(0, 1.35, this.z - 7);
    }
    const k = this.snap ? 1 : 1 - Math.exp(-dt * (this.mode === 'menu' ? 3 : 4));
    this.camPos.lerp(tp, this.camPos.lengthSq() ? k : 1);
    this.camLook.lerp(tl, k);
    cam.position.copy(this.camPos);
    if (this.shake > 0) { this.shake -= dt; cam.position.x += (Math.random() - 0.5) * 0.12; cam.position.y += (Math.random() - 0.5) * 0.1; }
    cam.lookAt(this.camLook);
    this.sky.position.copy(cam.position);
    this.renderer.render(this.scene, cam);
  }
  start() { this.camPos.set(3, 1.7, 3.4); this.loop(); }
}
export const wait = (ms) => new Promise((r) => setTimeout(r, ms));
