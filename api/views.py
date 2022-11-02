from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.http import JsonResponse
from .serializers import AddBotSerializer,EditBotSerializer,AddIndustriesSerializer,EditWidgetSerializer
from .models import Bot, Industries,Widget
import uuid
from django.core.files.storage import FileSystemStorage
import random


def error_formator(errors):
    error_list = []
    print(errors)
    for field_name, field_errors in errors.items():
        new_error = {}
        new_error[field_name] = str(field_errors[0])
        error_list.append(new_error)
    return error_list

def api_response(code,data,message,errors):
    res = {}
    res['code'] = code
    res['data'] = data
    res['message'] = message
    res['errors'] = errors
    return res

def gen_uuid4():
    my_uuid = str(uuid.uuid4())
    return my_uuid

def gen_random_color():
    chars = '0123456789ABCDEF'
    for i in range(1):
        color = '#'+''.join(random.sample(chars,6)) 
    return color


class AddIndustries(generics.GenericAPIView):
    def post(self,request, *args, **kwargs ):
        try:
            validation = AddIndustriesSerializer(data=request.data)
            industry_uuid = gen_uuid4()
            if validation.is_valid():
                Industries.objects.create(industry_name=validation.data['industry_name'],industry_uuid=industry_uuid)
                return JsonResponse(api_response(0,[],"Industry Created",[]))
            else:
                err = error_formator(validation.errors)
                print(err)
                return JsonResponse(api_response(1,[],"Error",err))
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e)))



class AddBotInformation(generics.GenericAPIView):    
    def post(self, request, *args, **kwargs):
        try:
            validation = AddBotSerializer(data= request.data)
            print(validation)
            new_bot_uuid = gen_uuid4()
            # new_company_uuid = gen_uuid4()
            font_name = "Verdana"
            background_color_code = gen_random_color()
            employee_text_color_code = gen_random_color()
            employee_background_color_code = gen_random_color()
            enduser_text_color_code = gen_random_color()
            enduser_background_color_code = gen_random_color()
            header_text_color_code = gen_random_color()
            header_background_color_code = gen_random_color()
            message_text_color_code = gen_random_color()
            message_background_color_code = gen_random_color()
            widget_toggle_color_code = gen_random_color()
            
            
            # print(new_uuid)
            if validation.is_valid():
                # industry_name = validation.data['industry_name']
                # industry_uuid = Industries.objects.filter(industry_name=industry_name).values('industry_uuid')
                # print(industry_uuid)
                if request.FILES:
                    small_picture_file = request.FILES['small_picture']
                    large_picture_file = request.FILES['large_picture']
                    profile_icon_file = request.FILES['profile_icon']
                    widget_icon_file = request.FILES['widget_icon']
                    fss = FileSystemStorage()
                    small_picture_file = fss.save(small_picture_file.name, small_picture_file)
                    small_file_url = fss.url(small_picture_file)
                    large_picture_file = fss.save(large_picture_file.name, large_picture_file)
                    large_file_url = fss.url(large_picture_file)
                    profile_icon_file = fss.save(profile_icon_file.name, profile_icon_file)
                    profile_icon_url = fss.url(profile_icon_file)
                    widget_icon_file = fss.save(widget_icon_file.name, widget_icon_file)
                    widget_icon_url = fss.url(widget_icon_file)
                    Bot.objects.create(bot_uuid=new_bot_uuid,bot_welcome_message=validation.data['bot_welcome_message'],terms_url=validation.data['terms_url'],bot_name=validation.data['bot_name'],auto_login=validation.data['auto_login'],end_user_dialog_uuid=new_bot_uuid,helper_dialog_uuid=new_bot_uuid,b2c_enabled=validation.data['b2c_enabled'],b2b_enabled=validation.data['b2b_enabled'],is_top_bot=validation.data['is_top_bot'],small_picture=small_file_url,large_picture=large_file_url,bot=validation.data['bot'])
                    Widget.objects.create(widget_uuid=new_bot_uuid,profile_icon_url=profile_icon_url,widget_icon_url=widget_icon_url,font_name=font_name,background_color_code=background_color_code,employee_text_color_code=employee_text_color_code,employee_background_color_code=employee_background_color_code,enduser_text_color_code=enduser_text_color_code,enduser_background_color_code=enduser_background_color_code,header_text_color_code=header_text_color_code,header_background_color_code=header_background_color_code,message_text_color_code=message_text_color_code,message_background_color_code=message_background_color_code,widget_toggle_color_code=widget_toggle_color_code,widgetJs=f"<div id=\"widget-root\" bootbot-id=\"{new_bot_uuid}\"></div><script type=\"text/javascript\" src=\"https://bizai-webwidget-dev-dot-vcbizai.appspot.com/wrapper.js\"></script>")
                    return JsonResponse(api_response(0,[],"Bot Created",[]))
                else:
                    Bot.objects.create(bot_uuid=new_bot_uuid,bot_welcome_message=validation.data['bot_welcome_message'],terms_url=validation.data['terms_url'],bot_name=validation.data['bot_name'],auto_login=validation.data['auto_login'],end_user_dialog_uuid=new_bot_uuid,helper_dialog_uuid=new_bot_uuid,b2c_enabled=validation.data['b2c_enabled'],b2b_enabled=validation.data['b2b_enabled'],is_top_bot=validation.data['is_top_bot'],bot=validation.data['bot'])
                    Widget.objects.create(widget_uuid=new_bot_uuid,font_name=font_name,background_color_code=background_color_code,employee_text_color_code=employee_text_color_code,employee_background_color_code=employee_background_color_code,enduser_text_color_code=enduser_text_color_code,enduser_background_color_code=enduser_background_color_code,header_text_color_code=header_text_color_code,header_background_color_code=header_background_color_code,message_text_color_code=message_text_color_code,message_background_color_code=message_background_color_code,widget_toggle_color_code=widget_toggle_color_code,widgetJs=f"<div id=\"widget-root\" bootbot-id=\"{new_bot_uuid}\"></div><script type=\"text/javascript\" src=\"https://bizai-webwidget-dev-dot-vcbizai.appspot.com/wrapper.js\"></script>")
                    return JsonResponse(api_response(0,[],"Bot Created",[]))

            else:
                err = error_formator(validation.errors)
                print(err)
                return JsonResponse(api_response(1,[],"Error",err))
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e))) 


class GetAllBots(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            instance = Bot.objects.all().values()
            if instance:
                list_result = [entry for entry in instance]
                return JsonResponse(api_response(0,list_result,"Bots Info",[]))
            else:
                return JsonResponse(api_response(0,[],"No Bot found",[]))

            
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e)))

class GetWidget(generics.GenericAPIView):
    def get(self, request,bot_uuid, *args, **kwargs):
        try:
            instance = Widget.objects.filter(widget_uuid=bot_uuid).values()
            if instance:
                list_result = [entry for entry in instance]
                return JsonResponse(api_response(0,list_result,"Widget Info",[]))
            else:
                return JsonResponse(api_response(0,[],"No widget found",[]))

            
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e)))

class EditWidget(generics.GenericAPIView):
    def post(self, request,widget_uuid, *args, **kwargs):
        try:
            validation = EditWidgetSerializer(data=request.data)
            if validation.is_valid():
                if request.FILES:
                    profile_icon_file = request.FILES['profile_icon']
                    widget_icon_file = request.FILES['widget_icon']
                    fss = FileSystemStorage()
                    profile_icon_file = fss.save(profile_icon_file.name, profile_icon_file)
                    profile_icon_url = fss.url(profile_icon_file)
                    widget_icon_file = fss.save(widget_icon_file.name, widget_icon_file)
                    widget_icon_url = fss.url(widget_icon_file)
                    res = Widget.objects.filter(widget_uuid=widget_uuid).update(profile_icon_url=profile_icon_url,widget_icon_url=widget_icon_url,font_name=validation.data['font_name'],background_color_code=validation.data['background_color_code'],employee_text_color_code=validation.data['employee_text_color_code'],employee_background_color_code=validation.data['employee_background_color_code'],enduser_text_color_code=validation.data['enduser_text_color_code'],enduser_background_color_code=validation.data['enduser_background_color_code'],header_text_color_code=validation.data['header_text_color_code'],header_background_color_code=validation.data['header_background_color_code'],message_text_color_code=validation.data['message_text_color_code'],message_background_color_code=validation.data['message_background_color_code'],widget_toggle_color_code=validation.data['widget_toggle_color_code'],widget_width_code=validation.data['widget_width_code'])
                    if res:
                        return JsonResponse(api_response(0,[],"Widget Updated",[]))
                    else:
                        return JsonResponse(api_response(0,[],"widget not found",[]))
                else:
                    res = Widget.objects.filter(widget_uuid=widget_uuid).update(profile_icon_url=profile_icon_url,widget_icon_url=widget_icon_url,font_name=validation.data['font_name'],background_color_code=validation.data['background_color_code'],employee_text_color_code=validation.data['employee_text_color_code'],employee_background_color_code=validation.data['employee_background_color_code'],enduser_text_color_code=validation.data['enduser_text_color_code'],enduser_background_color_code=validation.data['enduser_background_color_code'],header_text_color_code=validation.data['header_text_color_code'],header_background_color_code=validation.data['header_background_color_code'],message_text_color_code=validation.data['message_text_color_code'],message_background_color_code=validation.data['message_background_color_code'],widget_toggle_color_code=validation.data['widget_toggle_color_code'],widget_width_code=validation.data['widget_width_code'])
                    if res:
                        return JsonResponse(api_response(0,[],"Widget Updated",[]))
                    else:
                        return JsonResponse(api_response(0,[],"widget not found",[]))
            else:
                err = error_formator(validation.errors)
                return JsonResponse(api_response(1,[],"Error",err))
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e)))




class EditBotInformation(generics.GenericAPIView):
    def post(self, request,bot_uuid, *args, **kwargs):
        try:
            validation = EditBotSerializer(data=request.data)
            if validation.is_valid():
                if request.FILES:
                    small_picture_file = request.FILES['small_picture']
                    large_picture_file = request.FILES['large_picture']
                    fss = FileSystemStorage()
                    small_picture_file = fss.save(small_picture_file.name, small_picture_file)
                    small_file_url = fss.url(small_picture_file)
                    large_picture_file = fss.save(large_picture_file.name, large_picture_file)
                    large_file_url = fss.url(large_picture_file)
                    res = Bot.objects.filter(bot_uuid=bot_uuid).update(bot_welcome_message=validation.data['bot_welcome_message'],terms_url=validation.data['terms_url'],bot_name=validation.data['bot_name'],small_picture=small_file_url,large_picture=large_file_url)
                    if res:
                        return JsonResponse(api_response(0,[],"Bot updated",[]))
                    else:
                        return JsonResponse(api_response(0,[],"Bot not found",[]))
                else:
                    res = Bot.objects.filter(bot_uuid=bot_uuid).update(bot_welcome_message=validation.data['bot_welcome_message'],terms_url=validation.data['terms_url'],bot_name=validation.data['bot_name'])
                    if res:
                        return JsonResponse(api_response(0,[],"Bot updated",[]))
                    else:
                        return JsonResponse(api_response(0,[],"Bot not found",[]))
            else:
                err = error_formator(validation.errors)
                return JsonResponse(api_response(1,[],"Error",err))
                    
        except Exception as e:
            print(e)
            return JsonResponse(api_response(1,[],"Error",str(e)))
        

class DeleteBotInformation(generics.GenericAPIView):
    def post(self, request,bot_uuid, *args, **kwargs):
        try:
            bot_res = Bot.objects.filter(bot_uuid=bot_uuid).delete()
            widget_res = Widget.objects.filter(widget_uuid=bot_uuid).delete()

            if bot_res or widget_res:
                return JsonResponse(api_response(0,[],"Bot Deleted",[]))
            else:
                return JsonResponse(api_response(0,[],"Bot not found",[]))
        except Exception as e:
            print(e)
            # traceback.print_exc()
            return JsonResponse(api_response(1,[],"Error",str(e)))
        

       
