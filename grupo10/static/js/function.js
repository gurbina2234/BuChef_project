function increaseSize(element) {
    element.style.transform = 'scale(1.4)';
    setTimeout(function() {
        element.style.transform = 'scale(1)';
    }, 300);
}

function increaseSizeCard(element) {
    element.style.transform = 'scale(1.1)';
    setTimeout(function() {
        element.style.transform = 'scale(1)';
    }, 1000);
}