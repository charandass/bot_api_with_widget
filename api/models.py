from pyexpat import model
from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Bot(models.Model):
    bot_uuid = models.CharField(max_length=100)
    bot_welcome_message = models.CharField(max_length=100)
    terms_url = models.CharField(max_length=100)
    bot_name = models.CharField(max_length=100)
    auto_login = models.BooleanField(default=False)
    end_user_dialog_uuid = models.CharField(max_length=100)
    helper_dialog_uuid = models.CharField(max_length=100)
    b2c_enabled = models.BooleanField(default=False)
    b2b_enabled = models.BooleanField(default=False)
    is_top_bot = models.BooleanField(default=False)
    small_picture = models.ImageField(upload_to='images/',blank=True)
    large_picture = models.ImageField(upload_to='images/',blank=True)
    # industry_uuid = models.CharField(max_length=100)
    bot = models.CharField(max_length=100)
    # company_id = models.CharField(max_length=100)

class Widget(models.Model):
    widget_uuid = models.CharField(max_length=100)
    profile_icon_url = models.ImageField(upload_to='images/',blank=True)
    widget_icon_url = models.ImageField(upload_to='images/',blank=True)
    font_name = models.CharField(max_length=100)
    background_color_code= models.CharField(max_length=100)
    employee_text_color_code = models.CharField(max_length=100)
    employee_background_color_code  = models.CharField(max_length=100)
    enduser_text_color_code = models.CharField(max_length=100)
    enduser_background_color_code = models.CharField(max_length=100)
    header_text_color_code = models.CharField(max_length=100)
    header_background_color_code = models.CharField(max_length=100)
    message_text_color_code = models.CharField(max_length=100)
    message_background_color_code = models.CharField(max_length=100)
    widget_toggle_color_code = models.CharField(max_length=100)
    widget_width_code = models.CharField(max_length=100, default =400)
    widgetJs = models.CharField(max_length=100)




class Industries(models.Model):
    industry_name = models.CharField(max_length=100)
    industry_uuid = models.CharField(max_length=100)

class EndUserDialog(models.Model):
    dialog = models.CharField(max_length=100)
    end_user_dialog_uuid = models.CharField(max_length=100)

class HelperDialog(models.Model):
    pass

    