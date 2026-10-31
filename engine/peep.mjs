// usage: node peep.mjs out.png '{"seed":"x","head":["bun"],...}' height
import { createAvatar } from '@dicebear/core';
import { openPeeps } from '@dicebear/collection';
import { Resvg } from '@resvg/resvg-js';
import fs from 'fs';
const [out, opts, h] = process.argv.slice(2);
const o = JSON.parse(opts);
const svg = createAvatar(openPeeps, { ...o, backgroundColor: ['transparent'], facialHairProbability: o.facialHair ? 100 : 0, accessoriesProbability: o.accessories ? 100 : 0, maskProbability: 0 }).toString();
fs.writeFileSync(out, new Resvg(svg, { fitTo: { mode: 'height', value: parseInt(h || '700') } }).render().asPng());
