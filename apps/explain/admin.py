from django.contrib import admin
from explain.models import Entry, Explanation, Comment

class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)

class ExplanationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Explanation, ExplanationAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)