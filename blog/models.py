from django.db import models

from django.utils import timezone

#lines with from or import are lines that add some bits from other files
#class Post(models.Model): defines our model, an object
#class - special keyword that indicates we're defining an object
#post - name of our model, always start class w/ Uppercase
#models.Model means Post is a Django model, so Django knows it should be saved in the databases
#properties - author, title, text, created_date, published_date

#models.CharField – this is how you define text with a limited number of characters.
#models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
#models.DateTimeField – this is a date and time.
#models.ForeignKey – this is a link to another model.

#def means this is a function,method and publish is the name of the method
 

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #double underscore __str__ is called dunder, short for double underscore
        return self.title
