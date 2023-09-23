from django.db import models

class Query(models.Model):
    sql_text = models.TextField()
    result = models.TextField(blank=True, null=True)
    executed_at = models.DateTimeField(auto_now_add=True)
