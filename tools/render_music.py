"""Renders MIDI files to soft background-music clips in assets/music/*.mp3.

    python3 tools/render_music.py DIR_WITH_MIDIS [SECONDS=40]

Same idea as La Belle Lucie's research/soundtrack/render.py (own numpy synth ->
22.05 kHz mono -> ffmpeg), but with soft sine/triangle-ish voices instead of chip
voices, no drums, a gentle low-pass, and an MP3 (plays everywhere, incl. iOS).
Each song is cut to its first SECONDS seconds (from the first note) with a fade-out.
Needs numpy, scipy, ffmpeg (libmp3lame). Sources: freemidi.org (see README).
"""
import os, sys, glob, struct, subprocess, tempfile, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 22050
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "music")

def parse(path):
    b = open(path, "rb").read()
    ntr, ppq = struct.unpack(">HH", b[10:14]); i = 14
    notes, tempos = [], [(0, 500000)]
    for _ in range(ntr):
        if i + 8 > len(b): break
        n = struct.unpack(">I", b[i+4:i+8])[0]; d = b[i+8:i+8+n]; i += 8 + n
        j = t = 0; run = None; on = {}; prog = {}
        def vlq():
            nonlocal j
            v = 0
            while True:
                if j >= len(d): return v
                c = d[j]; j += 1; v = (v << 7) | (c & 0x7f)
                if not c & 0x80: return v
        while j < len(d):
            t += vlq()
            if j >= len(d): break
            s = d[j]
            if s == 0xff:
                if j + 2 >= len(d): break
                typ = d[j+1]; ln = d[j+2]
                if typ == 0x51 and j + 6 <= len(d):
                    tempos.append((t, int.from_bytes(d[j+3:j+6], "big")))
                j += 3 + ln; continue
            if s in (0xf0, 0xf7):
                j += 1; ln = vlq(); j += ln; continue
            if s & 0x80: run = s; j += 1
            if not run: continue
            hi, ch = run & 0xf0, run & 0xf
            if hi in (0x80, 0x90):
                if j + 1 >= len(d): break
                p, v = d[j], d[j+1]; j += 2
                if hi == 0x90 and v > 0: on[(ch, p)] = (t, v)
                elif (ch, p) in on:
                    t0, v0 = on.pop((ch, p)); notes.append((t0, t - t0, p, v0, ch, prog.get(ch, 0)))
            elif hi == 0xC0:
                if j >= len(d): break
                prog[ch] = d[j]; j += 1
            elif hi == 0xD0: j += 1
            else: j += 2
    tempos.sort()
    return notes, tempos, ppq

def to_sec(tempos, ppq):
    # piecewise-linear tick -> seconds
    ts, ss, cur, last_t, last_s = [], [], 500000, 0, 0.0
    for t, tp in tempos:
        last_s += (t - last_t) * cur / 1e6 / ppq; last_t = t; cur = tp
        ts.append(t); ss.append((last_s, cur))
    def f(tick):
        k = max(0, np.searchsorted(ts, tick, side="right") - 1)
        return ss[k][0] + (tick - ts[k]) * ss[k][1] / 1e6 / ppq
    return f

def render(path, secs):
    notes, tempos, ppq = parse(path)
    f = to_sec(tempos, ppq)
    ev = [(f(t), f(t + d) - f(t), p, v, p_) for t, d, p, v, ch, p_ in notes if ch != 9 and d > 0]
    ev.sort()
    t0 = ev[0][0]; L = int((secs + 3) * SR); mix = np.zeros(L)
    for s, d, pit, vel, prog in ev:
        s -= t0
        if s >= secs: continue
        d = min(max(d, 0.12), 4.0); n = int((d + 0.5) * SR); i0 = int(s * SR)
        if i0 + n > L: n = L - i0
        t = np.arange(n) / SR; fr = 440 * 2 ** ((pit - 69) / 12)
        if pit > 100: continue
        w = np.sin(2*np.pi*fr*t) + .28*np.sin(4*np.pi*fr*t) + .08*np.sin(6*np.pi*fr*t)
        decays = prog < 8 or 24 <= prog < 32 or 8 <= prog < 16 or 104 <= prog < 112
        if decays: env = np.exp(-t * (2.2 if pit > 60 else 1.4)) * np.minimum(1, t / .006)
        else: env = np.minimum(1, t / .05)
        env = env * np.minimum(1, np.maximum(0, d + .4 - t) / .3) if not decays else env * np.minimum(1, np.maximum(0, d + .4 - t) / .25)
        mix[i0:i0+n] += w * env * (vel / 127) ** .8 * 0.1
    mix = sosfilt(butter(2, 3800, "low", fs=SR, output="sos"), mix)
    # tiny reverb: a few soft echoes
    for dly, g in ((0.11, .22), (0.19, .15), (0.31, .1)):
        k = int(dly * SR); mix[k:] += mix[:-k] * g
    mix = np.tanh(mix * 1.2)
    fade = np.ones(L); a = int(0.6 * SR); fade[:a] = np.linspace(0, 1, a)
    o = int(secs * SR); fade[o:] = 0; fade[o-int(3*SR):o] = np.linspace(1, 0, int(3*SR))
    mix *= fade; mix = mix[:o]
    return mix / np.abs(mix).max() * 0.6

def main():
    src = sys.argv[1]; secs = float(sys.argv[2]) if len(sys.argv) > 2 else 40
    os.makedirs(OUT, exist_ok=True)
    for mid in sorted(glob.glob(os.path.join(src, "*.mid"))):
        stem = os.path.basename(mid)[:-4]
        try: mix = render(mid, secs)
        except Exception as e: print("skip", stem, e); continue
        with tempfile.TemporaryDirectory() as tmp:
            wav = os.path.join(tmp, "a.wav"); wavfile.write(wav, SR, (mix * 32767).astype(np.int16))
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-ac", "1", "-c:a", "libmp3lame", "-b:a", "32k", os.path.join(OUT, stem + ".mp3")], check=True)
        print(stem)

if __name__ == "__main__": main()
