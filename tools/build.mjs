// Bundles src/ + assets/ + questions into one self-contained docs/index.html
import { build } from 'esbuild';
import fs from 'fs';
import path from 'path';

const mime = { '.fbx': 'application/octet-stream', '.obj': 'text/plain', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp3': 'audio/mpeg' };
const assets = {};
for (const dir of ['chars', 'cars', 'sfx', 'music']) {
  for (const f of fs.readdirSync(`assets/${dir}`)) {
    const ext = path.extname(f);
    assets[`${dir}/${f}`] = `data:${mime[ext]};base64,${fs.readFileSync(`assets/${dir}/${f}`).toString('base64')}`;
  }
}
fs.mkdirSync('build', { recursive: true });
fs.writeFileSync('build/assets.js', `export default ${JSON.stringify(assets)};`);

const out = await build({
  entryPoints: ['src/main.js'], bundle: true, minify: true, format: 'iife',
  write: false, loader: { '.json': 'json' }, target: 'es2020', legalComments: 'none',
});
const js = out.outputFiles[0].text.replace(/<\/script/gi, '<\\/script');
const css = fs.readFileSync('src/style.css', 'utf8');
const html = fs.readFileSync('src/index.html', 'utf8')
  .replace('/*CSS*/', () => css).replace('/*JS*/', () => js);
fs.mkdirSync('docs', { recursive: true });
fs.writeFileSync('docs/index.html', html);
console.log('docs/index.html', (html.length / 1e6).toFixed(2), 'MB');
