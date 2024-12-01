var menuIcon = document.querySelector('.menu-icon');
var closeIcon = document.querySelector('.close-icon');
var menu = document.querySelector('.menu-drop');

// Certifique-se de que o overlay exista no DOM
var overlay = document.querySelector('.overlay');
if (!overlay) {
    overlay = document.createElement('div');
    overlay.classList.add('overlay');
    document.body.appendChild(overlay);
}

// Exibe o menu lateral e o overlay
menuIcon.addEventListener('click', function () {
    menu.style.display = 'block'; // Exibe o menu lateral
    overlay.style.display = 'block'; // Exibe o overlay
    menuIcon.style.display = 'none'; // Esconde o botão de menu
    closeIcon.style.display = 'block'; // Mostra o botão de fechar
});

// Esconde o menu lateral e o overlay ao clicar no overlay
overlay.addEventListener('click', function () {
    menu.style.display = 'none'; // Esconde o menu lateral
    overlay.style.display = 'none'; // Esconde o overlay
    menuIcon.style.display = 'block'; // Mostra o botão de menu
    closeIcon.style.display = 'none'; // Esconde o botão de fechar
});

// Esconde o menu lateral e o overlay ao clicar no botão de fechar
closeIcon.addEventListener('click', function () {
    menu.style.display = 'none'; // Esconde o menu lateral
    overlay.style.display = 'none'; // Esconde o overlay
    menuIcon.style.display = 'block'; // Mostra o botão de menu
    closeIcon.style.display = 'none'; // Esconde o botão de fechar
});
