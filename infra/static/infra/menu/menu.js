(() => {
    const botaoMenu = document.querySelector('.navbar-burger')
    const menu = document.querySelector('.navbar-menu')
    botaoMenu.onclick = () => {
        botaoMenu.classList.toggle('is-active')
        menu.classList.toggle('is-active')
    }
})()
