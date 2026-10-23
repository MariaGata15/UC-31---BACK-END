/*
  Portfólio de Maria Clara.
  Uso de IA: OpenAI ChatGPT, para auxiliar na estruturação,
  na explicação dos requisitos e na revisão do código.
*/

// Seleciona os elementos do HTML que serão usados.
const menuBotao = document.querySelector("#menuBotao");
const menuNavegacao = document.querySelector("#menuNavegacao");
const temaBotao = document.querySelector("#temaBotao");
const saudacao = document.querySelector("#saudacao");
const formulario = document.querySelector("#formularioContato");
const retornoFormulario = document.querySelector("#retornoFormulario");
const anoAtual = document.querySelector("#anoAtual");

// MENU HAMBÚRGUER

// Abre ou fecha o menu e atualiza o atributo aria-expanded.
function alternarMenu() {
  const menuAberto = menuNavegacao.classList.toggle("aberto");

  menuBotao.setAttribute("aria-expanded", String(menuAberto));

  menuBotao.setAttribute(
    "aria-label",
    menuAberto ? "Fechar menu" : "Abrir menu"
  );
}

menuBotao.addEventListener("click", alternarMenu);

// Fecha o menu quando uma opção é selecionada.
menuNavegacao.querySelectorAll("a").forEach(function (link) {
  link.addEventListener("click", function () {
    menuNavegacao.classList.remove("aberto");
    menuBotao.setAttribute("aria-expanded", "false");
    menuBotao.setAttribute("aria-label", "Abrir menu");
  });
});

// SAUDAÇÃO DINÂMICA

// Recebe a hora e retorna uma saudação adequada.
function obterSaudacao(hora) {
  if (hora >= 5 && hora < 12) {
    return "Bom dia!";
  } else if (hora >= 12 && hora < 18) {
    return "Boa tarde!";
  } else {
    return "Boa noite!";
  }
}

// Descobre a hora atual e mostra a saudação na página.
const horaAtual = new Date().getHours();
saudacao.textContent = obterSaudacao(horaAtual);

// MODO CLARO E ESCURO

// Alterna a classe modo-escuro no body.
function alternarTema() {
  const modoEscuro = document.body.classList.toggle("modo-escuro");

  if (modoEscuro) {
    temaBotao.textContent = "☀";
    temaBotao.setAttribute("aria-label", "Ativar modo claro");
    temaBotao.setAttribute("title", "Ativar modo claro");
  } else {
    temaBotao.textContent = "☾";
    temaBotao.setAttribute("aria-label", "Ativar modo escuro");
    temaBotao.setAttribute("title", "Ativar modo escuro");
  }
}

temaBotao.addEventListener("click", alternarTema);

// VALIDAÇÃO DO FORMULÁRIO

// Exibe o erro abaixo do campo e informa se ele está inválido.
function mostrarErro(idCampo, idErro, mensagemErro) {
  const campo = document.getElementById(idCampo);
  const elementoErro = document.getElementById(idErro);

  elementoErro.textContent = mensagemErro;

  if (campo) {
    campo.setAttribute(
      "aria-invalid",
      String(mensagemErro !== "")
    );
  }
}

// Verifica os campos e retorna true se todos forem válidos.
function validarFormulario() {
  const nome = document.querySelector("#nome").value.trim();
  const email = document.querySelector("#email").value.trim();
  const mensagem = document.querySelector("#mensagem").value.trim();
  const consentimento = document.querySelector("#consentimento").checked;

  let formularioValido = true;

  // Limpa os erros anteriores.
  mostrarErro("nome", "erroNome", "");
  mostrarErro("email", "erroEmail", "");
  mostrarErro("mensagem", "erroMensagem", "");

  document.querySelector("#erroConsentimento").textContent = "";

  // Verifica o nome.
  if (nome === "") {
    mostrarErro("nome", "erroNome", "Preencha seu nome.");
    formularioValido = false;
  }

  // Verifica o e-mail.
  if (email === "") {
    mostrarErro("email", "erroEmail", "Preencha seu e-mail.");
    formularioValido = false;
  } else if (!email.includes("@") || !email.includes(".")) {
    mostrarErro("email", "erroEmail", "Digite um e-mail válido.");
    formularioValido = false;
  }

  // Verifica se a mensagem tem pelo menos 20 caracteres.
  if (mensagem === "") {
    mostrarErro("mensagem", "erroMensagem", "Escreva sua mensagem.");
    formularioValido = false;
  } else if (mensagem.length < 20) {
    mostrarErro(
      "mensagem",
      "erroMensagem",
      "A mensagem precisa ter pelo menos 20 caracteres."
    );

    formularioValido = false;
  }

  // Verifica se o consentimento foi marcado.
  if (!consentimento) {
    document.querySelector("#erroConsentimento").textContent =
      "Marque o consentimento para continuar.";

    formularioValido = false;
  }

  return formularioValido;
}

// Impede o envio real e mostra o resultado da validação.
formulario.addEventListener("submit", function (evento) {
  evento.preventDefault();

  retornoFormulario.textContent = "";

  if (validarFormulario()) {
    retornoFormulario.textContent =
      "Tudo certo! Os campos foram validados. " +
      "Este formulário é uma demonstração e não enviou seus dados.";

    formulario.reset();

    // Remove os indicadores de erro após limpar o formulário.
    ["nome", "email", "mensagem"].forEach(function (id) {
      document.getElementById(id).removeAttribute("aria-invalid");
    });
  } else {
    retornoFormulario.textContent =
      "Confira os campos destacados e corrija as informações.";

    // Leva o foco para o primeiro campo com erro.
    const primeiroErro = formulario.querySelector(
      '[aria-invalid="true"]'
    );

    if (primeiroErro) {
      primeiroErro.focus();
    }
  }
});

// ANO AUTOMÁTICO NO RODAPÉ

// Obtém o ano atual do computador.
anoAtual.textContent = new Date().getFullYear();