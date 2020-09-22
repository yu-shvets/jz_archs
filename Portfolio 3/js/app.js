// burger
const navToggle = document.getElementById('navToggle');
const nav = document.getElementById('nav');

navToggle.addEventListener('click', e => {
  e.preventDefault();

  nav.classList.toggle('show');
});

// active class
let links = document.querySelectorAll('.nav__link');

links.forEach(link => {
  link.addEventListener('click', function() {
    links.forEach(l => l.classList.remove('active'));
    this.classList.add('active');
  });
});


