import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")
django.setup()
import json
from news.models import news,Text

with open("data.json",mode="r",encoding='utf-8') as f:
	data=json.load(f)
for item in data:
	news_article = news(
        id=item['id'],
        url=item['url'],
        title=item['title'],
        date=item['date'],
		category=int(item['date'][6]),
        image_url=item['image_url'],
        editor=item['editor'],
        content=Text.objects.create(text=item['text'])
    )
	news_article.save()