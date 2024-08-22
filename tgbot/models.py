from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True

class TelegramProfile(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    branch = models.CharField("Branch name", max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Full Name")
    time = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Telegram Profile"
        verbose_name_plural = "Telegram Profiles"
        db_table = "telegram_profiles"
        
class SectionNumberChoices(models.TextChoices):
        FIRST = 'first', 'first'
        SECOND = 'second', 'second'
        THIRD = 'third', 'third'
        FOUR = 'four', 'four'
        FIVE = 'five', 'five'
        SIX = 'six', 'six'
        SEVEN = 'seven', 'seven'
        TEXT_QUESTION = 'text_question', 'text_question'
        
class Section(BaseModel):
   
        
    title = models.CharField("Section name", max_length=255)
    type = models.CharField("Section number", max_length=255, 
                            choices=SectionNumberChoices.choices, blank=True, null=True)
    total_questions = models.PositiveSmallIntegerField("Total Questions", 
                                                       default=0, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Question(BaseModel):
    title = models.CharField("Question", max_length=255)
    order = models.PositiveSmallIntegerField("Question order", default=1)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name='section_questions')
    
    def __str__(self):
        return self.title
        