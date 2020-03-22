from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView
from .models import Job_posting 
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render



class JobListView(LoginRequiredMixin, ListView):
	model = Job_posting
	template_name = 'job_posting.html'
	login_url = 'login'
	paginate_by = 5

class HomePageView(TemplateView):
	template_name = 'index.html'

class JobDetailView(LoginRequiredMixin, DetailView):
	model = Job_posting
	template_name = 'job_detail.html'
	login_url = 'login'

def search_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		jobs = Job_posting.objects.filter(title__icontains=url_parameter)
	else:
		jobs = Job_posting.objects.all()

	ctx["jobs"] = jobs

	if request.is_ajax():
		html = render_to_string(
			template_name="jobs-results-partial.html", 
			context={"jobs": jobs}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "job_search.html", context=ctx)





