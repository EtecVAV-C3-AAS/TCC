
function alternarContraste(){
  const corpo = document.documentElement;
  corpo.classList.toggle('alto-contraste');
  localStorage.setItem('alto_contraste', corpo.classList.contains('alto-contraste'));
}
function ajustarFonte(delta){
  const corpo = document.documentElement;
  let pct = parseInt(localStorage.getItem('tamanho_fonte') || '100');
  if(delta === 0){ pct = 100; }
  else { pct = Math.min(200, Math.max(70, pct + delta)); }
  corpo.style.fontSize = pct + '%';
  localStorage.setItem('tamanho_fonte', String(pct));
}
// Leitura (Web Speech API)
function lerConteudo(){
  if(!('speechSynthesis' in window)){ alert('Seu navegador não suporta leitura de voz.'); return; }
  window.speechSynthesis.cancel();
  const texto = document.getElementById('conteudo-principal').innerText;
  const fala = new SpeechSynthesisUtterance(texto);
  fala.lang = 'pt-BR'; fala.rate = 0.95;
  window.speechSynthesis.speak(fala);
}
// Feedback sonoro (Web Audio API)
function feedbackSonoro(correto){
  try{
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const o = ctx.createOscillator(); const g = ctx.createGain();
    o.connect(g); g.connect(ctx.destination);
    o.type = 'sine'; o.frequency.value = correto ? 880 : 220;
    g.gain.value = 0.1; o.start(); setTimeout(()=>{o.stop(); ctx.close();}, 200);
  }catch(e){}
}
// Atalhos: Enter ativa botão focado
document.addEventListener('keydown', (e)=>{
  if(e.key === 'Enter'){
    const alvo = document.activeElement;
    if(alvo && (alvo.tagName === 'BUTTON')){ alvo.click(); }
  }
});
