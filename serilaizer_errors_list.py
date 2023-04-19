  if serializer.is_vlaid():
      serializer.save()
      return Response(utils.simple_response(
          200,
          "Billing Address is added",
      ))
  else:

    errors = []
    for field, field_errors in serializer.errors.items():
        for field_error in field_errors:
            errors.append(f"{field}: {field_error}")
    return Response({
      "error":error
    })
