let selecionado = null;
let selecionados = new Set();
const audio = document.getElementById("audio");
const audioParabens = document.getElementById("audioParabens");
const grid = document.getElementById("grid");

function tocar(elemento, nome) {
  if (selecionado) {
    selecionado.classList.remove("selecionado");
    selecionado.classList.add("ativo");
  }

  elemento.classList.remove("ativo");
  elemento.classList.add("selecionado");
  selecionado = elemento;

  audio.pause();
  audio.src = "/static/audio/" + nome + ".mp3";
  audio.load();
  audio.play();

  selecionados.add(nome);
  if (selecionados.size >= totalItens) {
    setTimeout(() => {
      mostrarMedalha();
    }, 1500);
  }
}

function mostrarMedalha() {
  const medalha = document.getElementById("medalhaGanha");

  // Desativa todos os itens
  const itens = document.querySelectorAll(".item");
  itens.forEach(item => item.classList.add("desativado"));

  medalha.style.display = "flex";
  audioParabens.play();

  // Avança automaticamente após 5 segundos
  setTimeout(() => {
    window.location.href = "/?pagina=" + (pagina < total ? (pagina + 1) : 1);
  }, 5000);
}