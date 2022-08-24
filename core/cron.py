from datetime import date,datetime

def post_in_linkedin():
        from .models import Post
        today = date.today()
        now = datetime.now()
        hours = now.hour
        posts = Post.objects.filter(date=today)
        for post in posts:
            if str(post.hours).split(':')[0] == str(hours):
                post.delete()
