const menu_bar_btn = document.getElementById('menu_button');
let bool = 1;

menu_bar_btn.addEventListener('click', function () {
    bool = !bool;
    if(bool){
      openNav();
    }else{
      closeNav();
    }
  }, true);

function openNav() {
    menu = document.getElementsByClassName("menu")[0];
    menu_btn = document.getElementById('menu_button');
    menu.style.width = "15vw";
    menu.style.opacity = 1;
    menu.style.transition = "0.25s";
}

function closeNav() {
    menu = document.getElementsByClassName("menu")[0];
    menu_btn = document.getElementById('menu_button');
    menu.style.width = "0vw";
    menu.style.opacity = 0;
    menu.style.transition = "0.25s";
}