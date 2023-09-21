> it is a files lebel validation
> It will show you all field erros in single api hiting
> function name will be ->  validate_<name_of_the_field>

def validate_file(self, data):


        if data:
            # Get the file name and extension
            file_name = data.name

            file_extension = os.path.splitext(file_name)[1].lower()

            # Define the allowed file extensions
            allowed_extensions = ['.mp3','.mpeg','.mp4']

            # Check if the file extension is in the list of allowed extensions
            if file_extension not in allowed_extensions:
                raise ValidationError(f"Invalid file extension. Allowed extensions are: {', '.join(allowed_extensions)}")
        return data
