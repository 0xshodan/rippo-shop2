from datetime import datetime

from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from avito.api_client import avito_get_reviews


class FeedbacksView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = avito_get_reviews()
        for i, feedback in enumerate(data):
            try:
                data[i]["createdAt"] = datetime.fromtimestamp(feedback["createdAt"]).date()
            except:
                break
        template = loader.get_template("feedbacks.html")
        context = {"feedbacks": data}
        return HttpResponse(template.render(context, request))
