
function alternarContraste(){
  const corpo = document.documentElement;
  const ativo = corpo.classList.toggle('alto-contraste');
  localStorage.setItem('alto_contraste', ativo ? 'true' : 'false');
  // atualizar aria-pressed do botão
  const btn = document.getElementById('btn-contraste');
  if(btn) btn.setAttribute('aria-pressed', String(ativo));
}


function ajustarFonte(delta){
  const corpo = document.documentElement;
  let pct = parseInt(localStorage.getItem('tamanho_fonte') || '100', 10);
  if(delta === 0){ pct = 100; }
  else { pct = Math.min(200, Math.max(70, pct + delta)); }
  corpo.style.fontSize = pct + '%';
  localStorage.setItem('tamanho_fonte', String(pct));
}


function lerConteudo(){
  if(!('speechSynthesis' in window)){
    alert('Seu navegador não suporta leitura de voz.');
    return;
  }
  window.speechSynthesis.cancel();


  const conteudo = document.getElementById('conteudo-principal');
  if(!conteudo) return;
  const texto = conteudo.innerText.replace(/\\s+/g, ' ').trim();


  const fala = new SpeechSynthesisUtterance(texto);
  fala.lang = 'pt-BR';
  fala.rate = 0.95;
  fala.pitch = 1;
  fala.volume = 1;
  window.speechSynthesis.speak(fala);


  atualizarStatus('Leitura iniciada.');
}


function atualizarStatus(mensagem){
  let regiao = document.getElementById('regiao-status-acessibilidade');
  if(!regiao){
    regiao = document.createElement('div');
    regiao.id = 'regiao-status-acessibilidade';
    regiao.setAttribute('aria-live','polite');
    regiao.setAttribute('aria-atomic','true');
    regiao.style.position = 'absolute';
    regiao.style.left = '-9999px';
    document.body.appendChild(regiao);
  }
  regiao.textContent = mensagem;
}


function feedbackSonoro(correto){
  try{
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.connect(g); g.connect(ctx.destination);
    o.type = 'sine';
    o.frequency.value = correto ? 880 : 220;
    g.gain.value = 0.06;
    o.start();
    setTimeout(()=>{ o.stop(); ctx.close(); }, 160);
  }catch(e){}
}


document.addEventListener('keydown', (e) => {
  if(e.altKey && !e.shiftKey && !e.ctrlKey){
    switch(e.key){
      case '1': window.location.href = '/materias/alfabetizacao/'; break;
      case '2': window.location.href = '/materias/matematica/'; break;
      case '3': window.location.href = '/materias/cores-formas/'; break;
      case '4': window.location.href = '/materias/ciencias/'; break;
      case '5': window.location.href = '/materias/historia-cidadania/'; break;
      case 'm':
      case 'M': lerConteudo(); break;
      default: break;
    }
  }


  if(e.key === 'Enter'){
    const alvo = document.activeElement;
    if(alvo && alvo.tagName === 'BUTTON'){
      alvo.click();
    }
  }
});


document.addEventListener('keydown', (e) => {
  if(e.code === 'Space'){
    const foco = document.activeElement;
    if(foco && foco.classList && foco.classList.contains('forma')){

      foco.classList.toggle('arrastando');
    }
  }
});
