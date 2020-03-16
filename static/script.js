function remove_task(event) {
    const id = event.target.parentNode.parentNode.id
    fetch('/remove/' + id).then(response => window.location.reload())
}

function toggleModal(event) {
    const el = document.getElementsByTagName('form')[0]
    el.style.display = (el.style.display == 'block') ? 'none' : 'block'
    // el.style.display = 'block'
}

const a = document.getElementById('form-toggler')
a.addEventListener('click', toggleModal)