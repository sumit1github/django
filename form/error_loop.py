for field, errors in form.errors.items():
    for error in errors:
        messages.error(request, f'{field}: {error}')
