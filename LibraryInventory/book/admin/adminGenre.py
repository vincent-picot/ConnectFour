from django.contrib import admin
from book.models import Genre


# For more information about all the attributes into the Admin models, refer to the Django documentation
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class GenreAdmin(admin.ModelAdmin):
    """
    Genre admin model, it is link to the Genre model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['id']


# Register the model to be shown in the admin interface
admin.site.register(Genre, GenreAdmin)