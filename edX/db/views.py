from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from db.models import Database
from db.forms import DatabaseForm
from django.core.urlresolvers import reverse_lazy

from db.models import courseware_studentmodule
import json

# Create your views here.
class DatabaseFormView(FormView):
    template_name = 'database_form.html'
    form_class = DatabaseForm
    success_url = 'db/database/'

    #def form_valid(self, form):
        # when valid data is POSTed...
        #return super(DatabaseList, self).form_valid(form)

class DatabaseCreate(CreateView):
    model = Database
    fields = ['id', 'name', 'engine', 'host','port','user','password']

class DatabaseUpdate(UpdateView):
    model = Database
    fields = ['id', 'name', 'engine', 'host','port','user','password']
    template_name_suffix = '_update_form'

class DatabaseDelete(DeleteView):
    model = Database
    success_url = reverse_lazy('database_list')

class DatabaseList(ListView):
    model = Database

class DatabaseDetail(DetailView):
    model = Database

    def get_context_data(self, **kwargs):
        context = super(DatabaseDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):
    return HttpResponse("Hello")

def base(request):
    context = RequestContext(request)

    context_dict = {'test': "Hello Testing"}

    return render_to_response('db/base.html', context_dict, context)

def login_page(request):
    context = RequestContext(request)

    username = request.POST.get('username');
    if username == "pavlo":
        yes = "WOO"
    else:
        yes = "NOO"

    user = None

    if request.POST:
        user = authenticate(username=request.POST.get('username'),
                password=request.POST.get('password'))

    if user and user is not None:
        login(request, user)
        d = Database(id="new_test", name="test_db", engine="M",
                host="localhost", port="22", user="test", password="test")
        d.save()
        return redirect('base.html')

    context_dict = {'test': "Yes test!", 'uname': username,
            'pass': request.POST.get('password', None), 'yes': yes}

    return render_to_response('db/login.html', context_dict, context)

def logout_page(request):

    user = request.user

    if user and user is not None:
        logout(request)
        return redirect('base.html')

    return redirect('base.html')

def profile(request):
    return render_to_response('db/base.html')

def list(request):
    context = RequestContext(request)

    context_dict = {'test': "Hello Testing"}

    return render_to_response('db/list.html', context_dict, context)


def state(request):

    studentId = 6

    # in order to get records of all students
    # studentModule = courseware_studentmodule.objects.all()

    # in order to get records of a student with particular student_id
    # and the module_type is 'Problem'
    studentModule = courseware_studentmodule.objects.filter(
            student_id = studentId
        ).filter(
            module_type = 'Problem'
        )

    problems = []

    for row in studentModule:

        state = json.loads(row.state)
        attempts = 0
        #search in the state JSON array if there were attempts performed on
        #the current problem
        for key, value in state.iteritems ():
            if key == "attempts":

                attempts = value
                # checking if the student attempted to solve the problem
                if attempts > 0:
                    problem = {}
                    # problem is an associative array that stores values and keys (instead of indexes)
                    problem["problem_code"] = row.module_id
                    problem["attempts"] = attempts
                    problem["grade"] = int ( row.grade / row.max_grade * 100 )
                    problem["time_took"] = row.modified - row.created

                    problems.append(problem)

    htmlString = "Problems solving results of a student with a student_id = " + str(studentId)
    htmlString = htmlString + "<table border=\"1\" cellpadding=\"10\">\n"

    htmlString = htmlString + "  <tr align=\"center\">\n"
    # I am going to return an html code, it is a bad practice. I am doing it here to show the matrix.
    htmlString = htmlString +   "       <td>problem code</td>\n"
    htmlString = htmlString +   "       <td>attempts</td>\n"
    htmlString = htmlString +   "       <td>grade</td>\n"
    htmlString = htmlString +   "       <td>time took</td>\n"
    htmlString = htmlString +  "  </tr>\n"

    for row in problems:
        htmlString = htmlString + "  <tr>\n"
        htmlString = htmlString +   "       <td>" + row["problem_code"] + "</td>\n"
        htmlString = htmlString +   "       <td align=\"center\">" + str(row["attempts"]) + "</td>\n"
        htmlString = htmlString +   "       <td align=\"center\">" + str(row["grade"]) + " %" + "</td>\n"
        htmlString = htmlString +   "       <td align=\"center\">" + str(row["time_took"]) + "</td>\n"
        htmlString = htmlString + "  </tr>\n"


    htmlString = htmlString + "</table>\n"

    return HttpResponse(htmlString)