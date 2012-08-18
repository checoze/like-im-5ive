from django.contrib import admin
from explain.models import Entry, Explanation, Comment, Vote, Tag

class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)

class ExplanationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Explanation, ExplanationAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vote, VoteAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)