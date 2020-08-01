from django.db import models



class topic(models.Model):
    topicname=models.CharField(max_length=50)
    def __str__(c):
        return c.topicname
    class Meta:
        db_table='topic'

class author(models.Model):
    authorname=models.CharField(max_length=50)
    def __str__(c):
        return c.authorname

    class Meta:
        db_table='author'

class quotemodel(models.Model):
    title=models.CharField(max_length=300)
    topic=models.ForeignKey(topic,on_delete=models.CASCADE)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    description=models.TextField(max_length=300,default="")
    def __str__(c):
        return c.title
    class Meta:
        db_table='quotemodel'
