let burger = document.querySelector('.burger')
let menu = document.querySelector('.header__ul')
burger.onclick = function () {
    burger.classList.toggle('active-burger');
    menu.classList.toggle('active-menu');
}