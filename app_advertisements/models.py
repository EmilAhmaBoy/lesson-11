from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):
    def __str__(self):
        return f'Advertisement(id={self.id}, title=\'{self.title}\', price={self.price})'

    class Meta:
        db_table = 'advertisements'

    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements_93/')

    @admin.display(description='Изображение')
    def image_display(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="100px"></img>')
        else:
            return 'Изображение отсутствует'

    @admin.display(description='Дата создания')
    def created_at(self):
        from django.utils import timezone
        if self.creation_date.date() == timezone.now().date():
            creation_time = self.creation_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', creation_time
            )
        return self.creation_date.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата изменения')
    def modified_at(self):
        from django.utils import timezone
        if self.creation_date.date() == timezone.now().date():
            creation_time = self.creation_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', creation_time
            )
        return self.creation_date.strftime('%d.%m.%Y в %H:%M:%S')

# Create your models here.
