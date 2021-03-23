/* Cards Functionality */

let togg = document.getElementsByClassName("runtin");
let x;



for (x = 0; x < togg.length; x++) {
  togg[x].addEventListener("click", function (){
    const content = this.nextElementSibling;
    const serviceIcon = this.querySelector(".fa")
    if (content.classList.contains("active")){
      content.classList.remove("active");
      serviceIcon.classList.remove("collapsed")
  }
  else {
      content.classList.add("active");
      serviceIcon.classList.add("collapsed");
  }
  
  })
}

/* Mobile Navigation Toggle Functionality*/

const navIcon = document.querySelector(".nav-toggle");

const navMenu = document.querySelector(".nav-items-container");

function toggleMenu() {

  if (navMenu.classList.contains("active")){
    navMenu.classList.remove("active");
  } 
  else{
    navMenu.classList.add("active");
  }
}

navIcon.addEventListener('click', toggleMenu, false);

/* Navigation Bar Position Change  */

const nav = document.querySelector('nav.navbar');
let navTop = nav.offsetTop;

function fixedNav(){
  if (window.pageYOffset >= navTop) {
    nav.classList.add('fixed');
  }
  else {
    nav.classList.remove('fixed');
  }
}

window.addEventListener('scroll', fixedNav);

