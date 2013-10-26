from django.contrib import admin

import settings
from models import *

class VideoLogAdmin(admin.ModelAdmin):
    list_display = ("youtube_id", "user", "points", "total_seconds_watched", "complete",)
    list_filter = ("youtube_id", "user", "complete",)
admin.site.register(VideoLog, VideoLogAdmin)

class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = ("exercise_id", "user", "streak_progress", "complete",)
    list_filter = ("exercise_id", "user", "complete",)
admin.site.register(ExerciseLog, ExerciseLogAdmin)

class UserLogAdmin(admin.ModelAdmin):
    pass
if UserLog.is_enabled():  # only enable admin if the feature is enabled.
    admin.site.register(UserLog, UserLogAdmin)

class UserLogSummaryAdmin(admin.ModelAdmin):
    pass
if UserLog.is_enabled() or settings.CENTRAL_SERVER:  # only enable admin if the feature is enabled.
    admin.site.register(UserLogSummary, UserLogSummaryAdmin)

class VideoFileAdmin(admin.ModelAdmin):
    list_display = ("youtube_id", "flagged_for_download", "download_in_progress", "cancel_download", "percent_complete",)
    list_filter = ("flagged_for_download", "download_in_progress", "flagged_for_subtitle_download", "subtitle_download_in_progress",)
admin.site.register(VideoFile, VideoFileAdmin)

class LanguagePackAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "phrases", "approved_translations", "percent_translated", "crowdin_version", "software_version", "subtitle_count",)
    list_filter = ("code", "name", "phrases", "approved_translations", "percent_translated", "crowdin_version", "software_version", "subtitle_count",)
admin.site.register(LanguagePack, LanguagePackAdmin)
