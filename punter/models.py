from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'


class Prediction(models.Model):
    RUNNING = "running"
    LOST = "lost"
    WON = "won"

    CHOICE_STATUS = (
        (RUNNING,"Running"),
        (LOST, "Lost"),
        (WON, "Won")
    )
    category = models.ForeignKey(Category,related_name="predictions", on_delete=models.CASCADE)
    booking_code = models.CharField(max_length=20)
    booking_company = models.CharField(max_length=100, default= "SportyBet")
    status = models.CharField(max_length=20,choices=CHOICE_STATUS, default=RUNNING)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_code
    
    class Meta:
        ordering = ('-created_at',)

    