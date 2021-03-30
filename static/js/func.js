/* Cards Functionality */

const triggers = Array.from(document.querySelectorAll('.runtin'));

window.addEventListener('click', (ev) => {
  
  const clickTarget = ev.target;

  if (triggers.includes(clickTarget)) {
    const selector = clickTarget.getAttribute('data-target');
    const serviceIcon = clickTarget.getAttribute("data-class");
    collapse(selector, 'toggle'); 
    collapse(serviceIcon, 'toggle');
    
  }

  const inactiveItems = triggers.filter(trigger => {
    if (trigger !== clickTarget) {
        return trigger;
    }
  });


  inactiveItems.forEach(inactiveItem => {
        const item = inactiveItem.getAttribute('data-target');
        const serviceIcon = inactiveItem.getAttribute("data-class");
        collapse(item, 'hide');
        collapse(serviceIcon, 'hide');
    });

});


const fnmap = {
  'toggle': 'toggle',
  'show': 'add',
  'hide': 'remove' 
};


const collapse = (selector, cmd) => {
  const targets = Array.from(document.querySelectorAll(selector));
  targets.forEach(target => {
    target.classList[fnmap[cmd]]('active');

  });
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


