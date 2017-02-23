from django import template
register = template.Library()

@register.inclusion_tag("tags_test.html")
def test_tags(add_text):
    text="Проверка работы с Django TemplateTags   :"+ add_text
    return {'textTestTags':text}