/*==================== SHOW NAVBAR ====================*/
const showMenu = (headerToggle, navbarId) =>{
    const toggleBtn = document.getElementById(headerToggle),
    nav = document.getElementById(navbarId)
    
    // Validate that variables exist
    if(headerToggle && navbarId){
        toggleBtn.addEventListener('click', ()=>{
            // We add the show-menu class to the div tag with the nav__menu class
            nav.classList.toggle('show-menu')
            // change icon
            toggleBtn.classList.toggle('bx-x')
        })
    }
}
showMenu('header-toggle','navbar')

/*==================== THEME CHANGE ====================*/
const themeToggler = document.querySelector(".theme-toggle");

// Check localStorage for theme preference on page load
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add("dark-theme-var");
    themeToggler.querySelector('i.sun-icon').classList.remove('active');
    themeToggler.querySelector('i.moon-icon').classList.add('active');
}

themeToggler.addEventListener('click', () => {
    document.body.classList.toggle("dark-theme-var");

    themeToggler.querySelector('i.sun-icon').classList.toggle('active');
    themeToggler.querySelector('i.moon-icon').classList.toggle('active');

    // Save the theme preference
    const isDarkTheme = document.body.classList.contains("dark-theme-var");
    localStorage.setItem('theme', isDarkTheme ? 'dark' : 'light');
});


/*==================== LINK ACTIVE ====================*/
const linkColor = document.querySelectorAll('.nav-link')

function colorLink(){
    linkColor.forEach(l => l.classList.remove('active'))
    this.classList.add('active')
}

linkColor.forEach(l => l.addEventListener('click', colorLink))




/*==================== SHOW POPUP WINDOW ====================*/
document.addEventListener("DOMContentLoaded", function() {
    var popup = document.getElementById("popup");
    var openPopupBtn = document.getElementById("openPopup");
    var closePopupBtn = document.getElementById("closePopup");

    openPopupBtn.addEventListener("click", function() {
        popup.style.display = "flex";
    });

    closePopupBtn.addEventListener("click", function() {
        popup.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    });
});
