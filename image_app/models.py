from django.db import models


class Batch1(models.Model):
    name  = models.CharField(max_length=200)
    gallery_img1 = models.ImageField()
    gallery_img2 = models.ImageField()
    gallery_img3 = models.ImageField()
    gallery_img4 = models.ImageField()
    gallery_img6 = models.ImageField()
    gallery_img7 = models.ImageField()
    gallery_img8 = models.ImageField()
    gallery_img9 = models.ImageField()
    gallery_img10 = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Batch1"
    

class Batch2(models.Model):
    name  = models.CharField(max_length=200)
    gallery_img1 = models.ImageField()
    gallery_img2 = models.ImageField()
    gallery_img3 = models.ImageField()
    gallery_img4 = models.ImageField()
    gallery_img6 = models.ImageField()
    gallery_img7 = models.ImageField()
    gallery_img8 = models.ImageField()
    gallery_img9 = models.ImageField()
    gallery_img10 = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Batch2"
    
    
class Batch3(models.Model):
    name  = models.CharField(max_length=200)
    gallery_img1 = models.ImageField()
    gallery_img2 = models.ImageField()
    gallery_img3 = models.ImageField()
    gallery_img4 = models.ImageField()
    gallery_img6 = models.ImageField()
    gallery_img7 = models.ImageField()
    gallery_img8 = models.ImageField()
    gallery_img9 = models.ImageField()
    gallery_img10 = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Batch3"
        
class Batch4(models.Model):
    name  = models.CharField(max_length=200)
    gallery_img1 = models.ImageField()
    gallery_img2 = models.ImageField()
    gallery_img3 = models.ImageField()
    gallery_img4 = models.ImageField()
    gallery_img6 = models.ImageField()
    gallery_img7 = models.ImageField()
    gallery_img8 = models.ImageField()
    gallery_img9 = models.ImageField()
    gallery_img10 = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Batch1"
    
class Batch5(models.Model):
    name  = models.CharField(max_length=200)
    gallery_img1 = models.ImageField()
    gallery_img2 = models.ImageField()
    gallery_img3 = models.ImageField()
    gallery_img4 = models.ImageField()
    gallery_img6 = models.ImageField()
    gallery_img7 = models.ImageField()
    gallery_img8 = models.ImageField()
    gallery_img9 = models.ImageField()
    gallery_img10 = models.ImageField()
    gallery_img11 = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Batch1"
