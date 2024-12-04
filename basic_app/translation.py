from modeltranslation.translator import register, TranslationOptions

import basic_app.models as models


@register(models.Navbar)
class NavbarTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Posts)
class PostTranslationOptions(TranslationOptions):
    fields = ('title','subtitle', "post", "author_post")

@register(models.Banner)
class PostTranslationOptions(TranslationOptions):
    fields = ('title','subtitle', "post", "author_post")
@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','subtitle', "post", "author_post")

@register(models.Elon)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','subtitle', "post", "author_post")


@register(models.InteractiveMap)
class InteractiveMapTranslationOptions(TranslationOptions):
    fields = ("region_name",)


@register(models.Administrator)
class AdministratorTranslationOptions(TranslationOptions):
    fields = ("f_name", "position", "admission_days")
