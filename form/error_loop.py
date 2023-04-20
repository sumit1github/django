error_list = []
for field, errors in form.errors.items():
    for error in errors:
        error_list.append(f'{field}: {error}')

       
for field, errors in form.errors.items():
    for error in errors:
        messages.error(request, f'{field}: {error}')
