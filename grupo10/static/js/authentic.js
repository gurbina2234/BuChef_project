document.addEventListener("DOMContentLoaded", function() {
    const reviewButtons = document.querySelectorAll('.resena-button');
    reviewButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (this.dataset.isAuthenticated === 'false') {
                event.preventDefault();
                alert('Debes iniciar sesión antes de apretar este lindo botón!');
            } else {
                window.location.href = this.dataset.url;
            }
        });
    });
});