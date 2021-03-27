from django.core.management.base import BaseCommand

import json

import requests
from django.core.mail import send_mail
from django.template.loader import get_template

import django_app.settings as settings
from datetime import datetime,date

from django.shortcuts import render
from condition.models import Condition
from django.contrib.auth import get_user_model
User = get_user_model()

import datetime



class Command(BaseCommand):
    def handle(self, *args, **options):
        """ここに思い思いのスクリプトを記述する"""

        data = Condition.objects.all()
        data = data.filter(pub_date=date.today())
        user = User.objects.all()
        posted_list = data.values_list('owner', flat=True)
        user_list = list(User.objects.values_list('id', flat=True))
        incomplete_list = list(set(posted_list)^set(user_list))
        incomplete_user = [User.objects.get(id=i).username for i in incomplete_list]
        item = incomplete_user
        if "superuser" in incomplete_user:
            incomplete_user.remove("superuser")

        template = get_template('slack/message.html')
        context = {
            "item": item, 
        }
        message = template.render(context)
        weekday = datetime.date.today().weekday()
        if weekday == 5 or weekday == 6:
            requests.post(settings.SLACK_WEBHOOK_ENDPOINT,
                        data=json.dumps({
                            'text': message,  # 投稿するテキスト
                            'username': u'体調管理',  # 投稿のユーザー名
                            # 'icon_emoji': u':ghost:',  # 投稿のプロフィール画像に入れる絵文字
                        }))
        else:
            return

