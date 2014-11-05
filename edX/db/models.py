from django.db import models

# Create your models here.
class Database(models.Model):
    DB_ENGINES = (
        ('M', 'MongoDB'),
        ('S', 'MySQL'),
        ('L', 'SQLite'),
        ('O', 'Oracle'),
    )
    id = models.CharField("Unique DB name", max_length=50, primary_key=True)
    name = models.CharField("Name or path of the database", max_length=50)
    # path = models.CharField("Path to the database (if local)", max_length=50)
    engine = models.CharField("Database engine", max_length=1, choices=DB_ENGINES)
    host = models.CharField("Database host", max_length=30)
    port = models.IntegerField("Connection port", max_length=8)
    user = models.CharField("Database username", max_length=30)
    password = models.CharField("Database password", max_length=100)


