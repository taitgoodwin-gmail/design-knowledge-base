import fs from 'node:fs/promises';import sharp from 'sharp';
const dir='design-study/presentation/assets'; for(const name of await fs.readdir(dir)){if(name.endsWith('.svg')){await sharp(await fs.readFile(dir+'/'+name),{density:160}).png().toFile(dir+'/'+name+'.png');console.log(name);}}
