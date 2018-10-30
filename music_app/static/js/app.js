console.log('hey everyone!')


$(document).ready(function () {
  $('body').on('click', function () {
    console.log('clicccccck')
  })
});


// Nav bar functionality 

const hamburger = document.querySelector('.hamburger-icon');

// Hamburger menu click event listener

hamburger.addEventListener('click', handleMenuClick);

// Handle menu click

function handleMenuClick() {
  var sidebar = document.querySelector('.side-bar')
  if (sidebar.classList.contains('.hidden')) {

  }
}