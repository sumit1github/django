
# serilaizer type

#### normal serializer

    from rest_framework import serializers

    class MySerializer(serializers.Serializer):
        char_field = serializers.CharField(
            max_length=100,
            required=True,
            allow_blank=False,
            trim_whitespace=True,
            help_text="This is a CharField for string data."
        )
        
        integer_field = serializers.IntegerField(
            required=True,
            min_value=0,
            max_value=100,
            help_text="This is an IntegerField for integer data."
        )

#### models serializer 

class SignupSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        help_text="Confirm Password."
    )

    class Meta:
        model = models.User
        fields = [
            'full_name',
            'email',
            'contact',
            'password',

        ]

        extra_kwargs = {
            'full_name': {'required': True},
            'email': {'required': True},
            'contact': {'required': True},
            'password': {'required': True},
        }

        def validate(self, data):
            password = data.get('password')
            password2 = data.get('confirm_password')

            if password != password2:
                raise ValidationError("Passwords do not match.")
            
            data['password'] = make_password(password2)

            return data

# validation

#### all filed validation
> fileld errors will be displayed one after another

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('confirm_password')

        if password != password2:
            raise ValidationError("Passwords do not match.")
        
        data['password'] = make_password(password2)   #<- `we are midifying the data` 

        return data

#### filed label validation
> You will get errors of all fileds.

> `file` is a filed

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


# SerializerMethodField
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['name']  # Include other fields as needed


    class CategoryListSerializer(serializers.ModelSerializer):
        product_list = serializers.SerializerMethodField()

        def get_product_list(self, obj):
            product=Product.objects.filter(cat=obj.id)
            serializer = ProductSerializer(product, many=True).data
            return serializer


        class Meta:
            model = Category
            fields = ['name','product_list']



# -------------------- serilaizer available fileds --------------

    class MySerializer(serializers.Serializer):
        char_field = serializers.CharField(
            max_length=100,
            required=True,
            allow_blank=False,
            trim_whitespace=True,
            help_text="This is a CharField for string data."
        )
        
        integer_field = serializers.IntegerField(
            required=True,
            min_value=0,
            max_value=100,
            help_text="This is an IntegerField for integer data."
        )

        float_field = serializers.FloatField(
            required=True,
            min_value=0.0,
            max_value=100.0,
            help_text="This is a FloatField for floating-point data."
        )

        boolean_field = serializers.BooleanField(
            required=False,
            default=False,
            help_text="This is a BooleanField for boolean data."
        )

        choice_field = serializers.ChoiceField(
            choices=[('option1', 'Option 1'), ('option2', 'Option 2')],
            default='option1',
            help_text="This is a ChoiceField for predefined choices."
        )

        date_field = serializers.DateField(
            required=False,
            help_text="This is a DateField for date data."
        )

        datetime_field = serializers.DateTimeField(
            required=False,
            help_text="This is a DateTimeField for date and time data."
        )

        time_field = serializers.TimeField(
            required=False,
            help_text="This is a TimeField for time data."
        )

        duration_field = serializers.DurationField(
            required=False,
            help_text="This is a DurationField for time duration data."
        )

        email_field = serializers.EmailField(
            required=False,
            help_text="This is an EmailField for email addresses."
        )

        url_field = serializers.URLField(
            required=False,
            help_text="This is a URLField for URLs."
        )

        slug_field = serializers.SlugField(
            required=False,
            help_text="This is a SlugField for slugs."
        )

        file_field = serializers.FileField(
            required=False,
            help_text="This is a FileField for file uploads."
        )

        image_field = serializers.ImageField(
            required=False,
            help_text="This is an ImageField for image file uploads."
        )

        serializer_method_field = serializers.SerializerMethodField(
            method_name='custom_method',
            help_text="This is a SerializerMethodField with a custom method."
        )

        list_field = serializers.ListField(
            child=serializers.CharField(),
            required=False,
            help_text="This is a ListField for lists of strings."
        )

        dict_field = serializers.DictField(
            child=serializers.CharField(),
            required=False,
            help_text="This is a DictField for dictionaries."
        )

        primary_key_related_field = serializers.PrimaryKeyRelatedField(
            queryset=RelatedModel.objects.all(),
            required=False,
            help_text="This is a PrimaryKeyRelatedField for related models by primary key."
        )

        string_related_field = serializers.StringRelatedField(
            source='related_model',
            read_only=True,
            help_text="This is a StringRelatedField for related models as strings."
        )

        slug_related_field = serializers.SlugRelatedField(
            slug_field='slug',
            queryset=RelatedModel.objects.all(),
            required=False,
            help_text="This is a SlugRelatedField for related models by slug."
        )

        hyperlinked_identity_field = serializers.HyperlinkedIdentityField(
            view_name='related-model-detail',
            lookup_field='pk',
            help_text="This is a HyperlinkedIdentityField for related models."
        )

        hyperlinked_related_field = serializers.HyperlinkedRelatedField(
            view_name='related-model-detail',
            queryset=RelatedModel.objects.all(),
            required=False,
            help_text="This is a HyperlinkedRelatedField for related models."
        )

        uuid_field = serializers.UUIDField(
            required=False,
            help_text="This is a UUIDField for UUIDs."
        )

        ip_address_field = serializers.IPAddressField(
            required=False,
            help_text="This is an IPAddressField for IP addresses."
        )

        generic_ip_address_field = serializers.GenericIPAddressField(
            required=False,
            help_text="This is a GenericIPAddressField for IP addresses (IPv4/IPv6)."
        )

        json_field = serializers.JSONField(
            required=False,
            help_text="This is a JSONField for JSON data."
        )

        read_only_field = serializers.ReadOnlyField(
            source='computed_field',
            help_text="This is a ReadOnlyField with data from a computed field."
        )

        hidden_field = serializers.HiddenField(
            default='hidden_value',
            help_text="This is a HiddenField with a default value."
        )