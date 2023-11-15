from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .services.form_checker_service import FormCheckerService
from .services.tinydb_data_source import TinydbDataSource


@method_decorator(csrf_exempt, name='dispatch')
class FormCheckerView(View):
    """
    Представление обрабатывающее POST запросы
    """

    def post(self, request):
        service = FormCheckerService(
            data_source=TinydbDataSource(data=request.POST)
        )
        res = service.search()

        if isinstance(res, dict):
            return JsonResponse(res)

        return HttpResponse(res)
