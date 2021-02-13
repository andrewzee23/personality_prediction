const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar-menu');

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});

const portfolioItems = document.querySelectorAll('.visual-item-wrapper');

portfolioItems.forEach(portfolioItem => {
  portfolioItem.addEventListener('mouseover', () => {
    console.log(portfolioItem.childNodes[1].classList)
    portfolioItem.childNodes[1].classList.add('image-blur');
  });

  portfolioItem.addEventListener('mouseout', () => {
    console.log(portfolioItem.childNodes[1].classList)
    portfolioItem.childNodes[1].classList.remove('image-blur');
  });
});

function jsDropDown(imgid,folder,newimg) {
  document.getElementById(imgid).src = '/static/' + folder + '/' + 'file_' + newimg + '.jpg'
}