// Renderiza páginas em JavaScript (Sebrae-SP "Vagas Efetivas") e imprime texto + links de PDF.
// Uso: NODE_PATH=$(npm root -g) node sebrae.js https://sebrae.com.br/sp/sobre-nos/trabalhe-conosco/vagas-efetivas-2026
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const u of process.argv.slice(2)) {
    try {
      await p.goto(u, { waitUntil: 'networkidle', timeout: 60000 });
      await p.waitForTimeout(4000);
      const txt = (await p.innerText('body')).replace(/\s+\n/g, '\n');
      console.log('=== ' + u + '\n' + txt.slice(0, 6000));
      const links = await p.$$eval('a', as => as.map(a => (a.innerText.trim().slice(0,90) + ' | ' + a.href)).filter(s => /pdf|comunicado|rbo|inscri|edital|processo/i.test(s)));
      console.log('--- links\n' + [...new Set(links)].slice(0, 60).join('\n'));
    } catch (e) { console.log('!! ' + u + ' ' + e.message); }
  }
  await b.close();
})();
