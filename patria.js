// Lista as vagas e bolsas abertas no portal da Fundação PATRIA (site em Blazor, só abre com navegador).
// Uso: NODE_PATH=$(npm root -g) node patria.js
// Edital de cada vaga: https://sistemas.patria.org.br/repository//tmp/EDITAL<NN><PROJETO><ANO>ass.pdf
// (ex.: EDITAL12FORNIT2026ass.pdf). Se o padrão mudar, abra "Anexos" > expandir no portal.
const { chromium } = require('playwright');
const fs = require('fs');
const chrome = fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium-')).map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`)[0];
(async () => {
  const b = await chromium.launch({ executablePath: chrome, args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('http://sistemas.patria.org.br/portalvagas/', { waitUntil: 'networkidle', timeout: 60000 });
  await p.waitForTimeout(5000);
  const texto = await p.innerText('body');
  console.log(texto.split('Portal de Vagas')[1] || texto);
  await b.close();
})();
