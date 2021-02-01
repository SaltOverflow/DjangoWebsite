window.onscroll = function() {shrinkNavbar()};

var navbarScrollTransition = 10;
function shrinkNavbar() {
  if (document.body.scrollTop > navbarScrollTransition || document.documentElement.scrollTop > navbarScrollTransition) {
    document.getElementById('navbar').classList.add('shrink');
  } else {
    document.getElementById('navbar').classList.remove('shrink');
  }
}