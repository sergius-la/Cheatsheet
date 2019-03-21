django-admin startproject <project name>
python manage.py startapp <app name>
./manage.py runserver <port>
./manage.py migrate

# Model object
pl = Post.objects.create(title="new post2", slug="new-post2", body="body text")

https://docs.djangoproject.com/en/2.1/ref/models/lookups/
Model.objects.get()

post = Post.objects.get(slug__iexact="New-Slug") # Case insensetive
post = Post.objects.get(slug__contains="New") 


Model.objects.all() # Return all objects



# Filter
 <p class="card-text">{{post.body|truncatewords:15}}</p>