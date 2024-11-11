// Validación de la calificación
function validateCalification(calification) {
    return calification > 0 && calification <= 5;
}

// Validación del mensaje
function validateMessage(message) {
    return message.length > 0 && message.length <= 100;
}

// Validación de la fecha
function validateDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const startDate = new Date('2024-01-01');
    return date <= now && date >= startDate;
}

// Validación de las categorías (asumiendo que las categorías son checkboxes o un campo similar)
function validateCategories(categories) {
    // Esta función asume que 'categories' es un arreglo de valores seleccionados
    return categories && categories.length > 0;
}

// Función para mostrar mensajes de error
function displayError(message) {
    // Aquí puedes personalizar cómo deseas mostrar los mensajes de error
    alert(message); // Ejemplo simple usando alert
}

// Función de validación principal que se llama al enviar el formulario
function validateReview() {
    const calification = document.querySelector('input[name="score"]:checked').value;
    const message = document.getElementById('id_message').value;
    const date = document.getElementById('id_date').value;
    const categoryCheckboxes = document.querySelectorAll('input[name="category"]:checked');
    const categories = Array.from(categoryCheckboxes).map(checkbox => checkbox.value);
    let isValid = true;
    let errorMessage = "";
    if (!validateCalification(parseInt(calification))) {
        errorMessage += "* Selecciona una calificación para el local.\n";
        isValid = false;
    }
    if (!validateMessage(message)) {
        errorMessage += "* El mensaje debe tener entre 1 y 100 caracteres.\n";
        isValid = false;
    }
    if (!validateDate(date)) {
        errorMessage += "* Selecciona una fecha válida. La fecha no puede ser mayor a la actual ni antes del 2024.\n";
        isValid = false;
    }
    if (!validateCategories(categories)) {
        errorMessage += "* Selecciona al menos una categoría.\n";
        isValid = false;
    }
    if (!isValid) {
        displayError(errorMessage);
    }
    return isValid;
    
}

document.getElementById('sendButton').addEventListener('click', () => {
    if (validateReview()) {
        document.getElementById('reviewForm').submit();
    }
  });

document.getElementById('id_image').addEventListener('change', function() {
    const files = this.files;
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    for (let i = 0; i < files.length; i++) {
        if (!allowedTypes.includes(files[i].type)) {
            alert('Por favor, selecciona una imagen válida (JPEG, PNG, GIF).');
            this.value = ''; 
            break;
        }
    }
});

document.getElementById('id_date').addEventListener('change', function() {
    const selectedDate = new Date(this.value);
    const currentDate = new Date();
    currentDate.setHours(0, 0, 0, 0); 

    if (selectedDate > currentDate) {
        alert('Por favor, selecciona una fecha igual o anterior a la fecha actual.');
        this.value = ''; 
    }
});