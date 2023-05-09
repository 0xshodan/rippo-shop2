from django.views.generic import TemplateView


class QuestionView(TemplateView):
    template_name = "questions.html"
