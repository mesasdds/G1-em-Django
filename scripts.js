var menuIcon = document.querySelector('.menu-icon');
var closeIcon = document.querySelector('.close-icon'); /* Selecione o ícone de fechamento */
var menu = document.querySelector('.menu');

menuIcon.addEventListener('click', function() {
  menu.style.display = 'block'; /* Abra o menu */
  menuIcon.style.display = 'none'; /* Oculte o ícone do menu hambúrguer */
  closeIcon.style.display = 'block'; /* Mostre o ícone de fechamento */
});

closeIcon.addEventListener('click', function() {
  menu.style.display = 'none'; /* Feche o menu */
  menuIcon.style.display = 'block'; /* Mostre novamente o ícone do menu hambúrguer */
  closeIcon.style.display = 'none'; /* Oculte o ícone de fechamento */
});
