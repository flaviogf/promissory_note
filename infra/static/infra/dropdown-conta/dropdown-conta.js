(() => {
    const dropdownConta = document.querySelector('.navbar-item.has-dropdown')
    dropdownConta.onclick = () => {
        dropdownConta.classList.toggle('is-active')
    }
})()
