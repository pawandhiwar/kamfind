from django.contrib import admin



from .models import blog_post
admin.site.register(blog_post)


from .models import category

admin.site.register(category)


from .models import State

admin.site.register(State)

from .models import Top_job

admin.site.register(Top_job)

from .models import Sec_post

admin.site.register(Sec_post)

from .models import Result

admin.site.register(Result)


from .models import Anskey
admin.site.register(Anskey)

from .models import Admitcard
admin.site.register(Admitcard)

from .models import Syllabus
admin.site.register(Syllabus)

from .models import Social_medias
admin.site.register(Social_medias)

from .models import Carousel
admin.site.register(Carousel)

from .models import Breaking_news
admin.site.register(Breaking_news)

from .models import Tool_add
admin.site.register(Tool_add)

from .models import PreviousYear
admin.site.register(PreviousYear)

from .models import borad_wish_post

admin.site.register(borad_wish_post)


from .models import Sarkari_post
admin.site.register(Sarkari_post)

from .models import Vyapam
admin.site.register(Vyapam)

from .models import UPSC
admin.site.register(UPSC)

from .models import Railway
admin.site.register(Railway)

from .models import SSC
admin.site.register(SSC)

from .models import AdSense
admin.site.register(AdSense)