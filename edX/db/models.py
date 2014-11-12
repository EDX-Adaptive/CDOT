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

# student's courswware data model
class courseware_studentmodule(models.Model):
    module_type = models.TextField(null=False)
    module_id = models.TextField(null=False)
    student_id = models.IntegerField(null=False)
    state = models.TextField(null=True)
    grade = models.IntegerField(null=True)
    created = models.DateTimeField(null=False)
    modified = models.DateTimeField(null=False)
    max_grade = models.IntegerField(null=True)

    class Meta:
        db_table = 'courseware_studentmodule'