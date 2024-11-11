import filetype
import re
from datetime import datetime
from django.contrib import messages

def validate_calification(calification):
    if calification < 0 or calification > 5:
        return False
    return True

def validate_message(message):
    if len(message) > 100 or len(message) < 1:
        return False
    return True

def validate_date(date):
    if date:
        fecha = datetime.strptime(str(date), '%Y-%m-%d')
        if fecha > datetime.now() or fecha < datetime(2024, 1, 1):
            return False
        else:
            return True
    return False
        
def validate_categories(categories):
    if categories is None:
        return False
    if len(categories) == 0:
        return False
    return True



def validate_review(request,calification, message, date, categories):
    if not validate_calification(calification):
        messages.error(request, "Selecciona una calificación para el local.")
        return False
    if not validate_message(message):
        messages.error(request, "El mensaje debe tener entre 3 y 100 caracteres.")
        return False
    if not validate_date(date):
        messages.error(request, "Selecciona una fecha. La fecha no puede ser mayor a la actual ni antes del 2024.")
        return False
    if not validate_categories(categories):
        print("Error en categorías")
        messages.error(request, "Selecciona al menos una categoría.")
        return False
    return True     