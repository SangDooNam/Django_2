from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint, Q
from django.core.exceptions import ValidationError

# Create your models here.

# task 3

# 1.  Audio.objects.all()
# 2.  count = Audio.objects.filter(type='podcast').count()   // Audio.objects.values('type').annotate(total=Count('type')) COUNT(*) GROUP BY
# 3.  count = Audio.objects.filter(~Q(type='song')).count()
# 4.  Audio.objects.all().order_by('duration')[:10]
# 5.  Audio.objects.filter(type='effect').order_by('-price')[1]
"""
6.  
from datetime import timedelta
two_min = timedelta(minutes=2)
three_min = timedelta(minutes=2)
Audio.objects.filter(Q(duration__gte=two_min) & Q(duration__lte=three_min)).count()
"""
"""
7.
from datetime import timedelta
two_min = timedelta(minutes=2)
three_min = timedelta(minutes=2)
Audio.objects.filter((Q(duration__gte=two_min) & Q(duration__lte=three_min)) | Q(price__gt=2)).count()
"""
"""
8. Audio.objects.filter(Q(duration__gt=thirty_min) & Q(type='podcast')).update(price=3.99)

"""
# task 2

class Audio(models.Model):
    ROCK = 'rock'
    POP = 'pop'
    INDIE = 'indie'
    FUNKY = 'funky'
    CLASSIC = 'classic'
    REGGAETON = 'reggaeton'
    FUNKY = 'funky' 
    STYLE_CHOICES = [
        (ROCK, 'Rock'),
        (POP, 'Pop'),
        (INDIE,'Indie'),
        (FUNKY, 'Funky'),
        (CLASSIC, 'Classic'),
        (REGGAETON, 'Reggaeton'),
        (FUNKY, 'Funky'),
    ]
    SONG = 'song'
    PODCAST = 'podcast'
    EFFECT = 'effect'
    TYPE_COICES =[
        (SONG, 'song'),
        (PODCAST, 'podcast'),
        (EFFECT, 'effect'),
    ]
    
    audio= models.FileField(upload_to='audio/', blank=False)
    title = models.CharField(max_length=250, blank=False)
    author = models.CharField(max_length=50, db_index=True, blank=True) 
    author_website = models.URLField(max_length=200, blank=True, null=True) # for task 2, author_website field don't need 'null=True' parameter.
    album = models.CharField(max_length=250, blank=True)
    duration = models.DurationField(blank=False)
    song_style = models.CharField(max_length=20, blank=True, null=True, choices=STYLE_CHOICES) # for task 2, song_style field don't need 'null=True' parameter.
    playbacks = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    deal_of_the_day = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified= models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10, choices=TYPE_COICES, blank=False)
    
    
    class Meta:
        
        constraints = [
            UniqueConstraint(
                fields=['title', 'author', 'duration'],
                name= 'Unique_title_author_duration'
                        ),
            
            CheckConstraint(
                check=Q(playbacks__gte=0),
                name = 'playbacks_gte_0'
            ),
        ]
    def clean(self):
        
        pirce_limits ={
            self.SONG : 4.99,
            self.PODCAST : 3.99,
            self.EFFECT : 94.99,
        }
        
        if isinstance(self.playbacks, int) and self.playbacks < 0:
            raise ValidationError({"playbacks": "Playbacks can't be negative value."})
        
        if self.price > 4.99:
            raise ValidationError({"price":"Price should be less then 5"})
        
        if self.duration is None:
            raise ValidationError({"duration":"duration can't contain none type value."})
        
        if Audio.objects.filter(title=self.title, author=self.author, duration=self.duration).exists():
            raise ValidationError("A record with this title, author, and duration already exists.")
        
        if self.song_style and self.type != self.SONG:
            raise ValidationError({"song_style": "Song_style only can be set when type is song."})
        
        if self.price > pirce_limits.get(self.type, 0):
            raise ValidationError({"price":f"price of {self.type} can not exceed {pirce_limits[self.type]}"})
        
        
        super().clean()
    
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
        






# task 1 


# from django.db import models
# from django.db.models import UniqueConstraint, CheckConstraint, Q
# from django.core.exceptions import ValidationError

# # Create your models here.

# class Song(models.Model):
#     ROCK = 'rock'
#     POP = 'pop'
#     INDIE = 'indie'
#     FUNKY = 'funky'
#     CLASSIC = 'classic'
#     REGGAETON = 'reggaeton'
#     STYLE_CHOICES = [
#         (ROCK, 'Rock'),
#         (POP, 'Pop'),
#         (INDIE,'Indie'),
#         (FUNKY, 'Funky'),
#         (CLASSIC, 'Classic'),
#         (REGGAETON, 'Reggaeton'),
#     ]
    
#     audio= models.FileField(upload_to='audio/', blank=False)
#     title = models.CharField(max_length=250, blank=False)
#     author = models.CharField(max_length=50, db_index=True, blank=True)
#     author_website = models.URLField(max_length=200, blank=True)
#     album = models.CharField(max_length=250, blank=True)
#     duration = models.DurationField(blank=False)
#     style = models.CharField(max_length=20, blank=True, choices=STYLE_CHOICES)
#     playbacks = models.PositiveIntegerField(null=True, blank=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
#     deal_of_the_day = models.BooleanField(blank=True, null=True)
#     notes = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     last_modified= models.DateTimeField(auto_now=True)
    
#     class Meta:
        
#         constraints = [
#             UniqueConstraint(
#                 fields=['title', 'author', 'duration'],
#                 name= 'Unique_title_author_duration'
#                         ),
            
#             CheckConstraint(
#                 check=Q(playbacks__gte=0),
#                 name = 'playbacks_gte_0'
#             ),
#             CheckConstraint(
#                 check=Q(price__lt=5),
#                 name = 'price_lt_5'
#             ),
            
#         ]
#     def clean(self):
#         if isinstance(self.playbacks, int) and self.playbacks < 0:
#             raise ValidationError({"playbacks": "Playbacks can't be negative value."})
#         if self.price > 4.99:
#             raise ValidationError({"price":"Price should be less then 5"})
#         if self.duration is None:
#             raise ValidationError({"duration":"duration can't contain none type value."})
#         if Song.objects.filter(title=self.title, author=self.author, duration=self.duration).exists():
#             raise ValidationError("A record with this title, author, and duration already exists.")
#         super().clean()
    
    
#     def save(self, *args, **kwargs):
#         self.full_clean()
#         super().save(*args, **kwargs)