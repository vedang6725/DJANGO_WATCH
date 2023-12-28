from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('m', 'Mens'),
        ('f', 'Womens'),
        ('k', 'Kids'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="('m','Mens')")
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100, 
        default='xyz'
    )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500,default='''Lorem, ipsum dolor sit amet consectetur adipisicing elit. A nam voluptate assumenda recusandae officia et consequatur, 
                   nobis voluptatem incidunt laborum harum doloribus aspernatur iure aperiam adipisci quas alias ea delectus!''')
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.windhorsepublications.com/wp-content/uploads/2019/11/image-coming-soon-placeholder.png"
    )

    






