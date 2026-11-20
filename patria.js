// Lista as vagas e bolsas abertas no portal da Fundação PATRIA (site em Blazor, só abre com navegador).
// Uso: NODE_PATH=$(npm root -g) node patria.js
// Edital de cada vaga: https://sistemas.patria.org.br/repository//tmp/EDITAL<NN><PROJETO><ANO>ass.pdf
// (ex.: EDITAL12FORNIT2026ass.pdf). Se o padrão mudar, abra "Anexos" > expandir no portal.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('http://sistemas.patria.org.br/portalvagas/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  // Blazor demora a montar a lista: espera sair o "Aguarde..." (até 60 s).
  await p.waitForFunction(() => !/Aguarde\.\.\./.test(document.body.innerText), null, { timeout: 60000 }).catch(() => {});
  await p.waitForTimeout(3000);
  const texto = await p.innerText('body');
  console.log(texto.split('Portal de Vagas')[1] || texto);
  await b.close();
})();
