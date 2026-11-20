// Renderiza a página de vagas do Sesc-SP (Reachr, carregada por JavaScript) e imprime as vagas ou "Nenhuma vaga".
// Uso: NODE_PATH=$(npm root -g) node sesc.js
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  try {
    await p.goto('https://www.reachr.com.br/sesc-sp/', { waitUntil: 'domcontentloaded', timeout: 90000 });
    await p.waitForTimeout(12000);
    const txt = await p.innerText('body');
    const linhas = txt.split('\n').map(s => s.trim()).filter(Boolean);
    const nenhuma = linhas.find(l => /nenhuma vaga/i.test(l));
    if (nenhuma) console.log(nenhuma);
    const links = await p.$$eval('a', as => as.map(a => a.innerText.trim().replace(/\s+/g, ' ').slice(0, 100) + ' | ' + a.href).filter(s => /vaga|job|processo/i.test(s)));
    console.log([...new Set(links)].join('\n'));
  } catch (e) { console.log('!! ' + e.message); }
  await b.close();
})();
