from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title = "Ke1vin7's Blog"

    link = "/"

    description = "Ke1vin7s Blog Test"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self, item):
        return item.body
