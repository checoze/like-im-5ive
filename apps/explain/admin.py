from django.contrib import admin
from explain.models import Entry, Explanation, Comment, Vote

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