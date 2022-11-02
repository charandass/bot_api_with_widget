from rest_framework import serializers

class AddBotSerializer(serializers.Serializer):
    bot_welcome_message = serializers.CharField(required=True, error_messages={'required': 'bot_welcome_message is required!'})
    terms_url = serializers.CharField(required=True, error_messages={'required': 'terms_url is required!'})
    bot_name = serializers.CharField(required=True, error_messages={'required': 'bot_name is required!'})
    auto_login = serializers.CharField(required=True, error_messages={'required': 'auto_login is required!'})
    b2c_enabled = serializers.BooleanField(required=True, error_messages={'required': 'b2c_enabled is required!'})
    b2b_enabled = serializers.BooleanField(required=True, error_messages={'required': 'b2b_enabled is required!'})
    is_top_bot = serializers.BooleanField(required=True, error_messages={'required': 'is_top_bot is required!'})
    small_picture = serializers.ImageField(required=False, error_messages={'required':'small_picture is not required'})
    large_picture = serializers.ImageField(required=False, error_messages={'required':'large_picture is not required'})
    bot = serializers.CharField(required=True, error_messages={'required': 'bot is required!'})
    # industry_name = serializers.CharField(required=True, error_messages={'required': 'industry_name is required!'})

class EditBotSerializer(serializers.Serializer):
    bot_welcome_message = serializers.CharField(required=True, error_messages={'required': 'bot_welcome_message is required!'})
    terms_url = serializers.CharField(required=True, error_messages={'required': 'terms_url is required!'})
    bot_name = serializers.CharField(required=True, error_messages={'required': 'bot_name is required!'})
    small_picture = serializers.ImageField(required=False, error_messages={'required':'small_picture is not required'})
    large_picture = serializers.ImageField(required=False, error_messages={'required':'large_picture is not required'})
    bot = serializers.CharField(required=True, error_messages={'required': 'bot is required!'})

class EditWidgetSerializer(serializers.Serializer):
    profile_icon = serializers.ImageField(required=False, error_messages={'required':'profile_icon is not required'})
    widget_icon = serializers.ImageField(required=False, error_messages={'required':'widget_icon is not required'})
    font_name = serializers.CharField(required=True, error_messages={'required': 'font_name is required!'})
    background_color_code = serializers.CharField(required=True, error_messages={'required': 'background_color_code is required!'})
    employee_text_color_code = serializers.CharField(required=True, error_messages={'required': 'employee_text_color_code is required!'})
    employee_background_color_code = serializers.CharField(required=True, error_messages={'required': 'employee_background_color_code is required!'})
    enduser_text_color_code = serializers.CharField(required=True, error_messages={'required': 'enduser_text_color_code is required!'})
    enduser_background_color_code = serializers.CharField(required=True, error_messages={'required': 'enduser_background_color_code is required!'})
    header_text_color_code = serializers.CharField(required=True, error_messages={'required': 'header_text_color_code is required!'})
    header_background_color_code = serializers.CharField(required=True, error_messages={'required': 'header_background_color_code is required!'})
    message_text_color_code = serializers.CharField(required=True, error_messages={'required': 'message_text_color_code is required!'})
    message_background_color_code = serializers.CharField(required=True, error_messages={'required': 'message_background_color_code is required!'})
    widget_toggle_color_code = serializers.CharField(required=True, error_messages={'required': 'widget_toggle_color_code is required!'})
    widget_width_code = serializers.CharField(required=True, error_messages={'required': 'widget_width_code is required!'})


class AddIndustriesSerializer(serializers.Serializer):
    industry_name = serializers.CharField(required=True, error_messages={'required': 'industry_name is required!'})
    