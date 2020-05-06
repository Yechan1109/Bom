from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView, FormMixin
from django.views.generic import DetailView, ListView

from .forms import SetplanForm, DangerForm, GetplanForm, UserForm, PerformanceForm, IndexForm, ToadminForm
from .models import Counselor, BomUser, BomSetPlan, BomGetPlan, Danger, Performance
from bom_data.models import ChartData, SetUser


class IndexView(FormView):
    template_name = 'index.html'
    form_class = IndexForm
    success_url = '/main'

    # 유효성 검사 끝났을 때 들어오는 함수
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('counselor_name')

        return super().form_valid(form)

class ToadminView(FormView):
    template_name = 'toadmin.html'
    form_class = IndexForm
    success_url = '/admin'

    # 유효성 검사 끝났을 때 들어오는 함수
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('counselor_name')

        return super().form_valid(form)

# @login_required
def main(request):
    return render(request, 'main.html', {'counselor_name':request.session.get('user') })

class UserList(ListView):
    model = SetUser
    template_name = 'userlist.html'
    context_object_name = 'user_list'


# class UserListDetail(FormMixin, DetailView):
#     context_object_name = 'user'
#     template_name = 'userlist_detail.html'
#     form_class = GetplanForm
#     queryset = ChartData.objects.all()
    
class UserListDetail(FormMixin, DetailView):
    template_name='userlist_detail.html'
    model = SetUser
    form_class = GetplanForm

    context_object_name = 'user'
    queryset = SetUser.objects.all()

    # DetailView와 FormView를 동시에 사용하기 위한 코드 추가
    def get_success_url(self):
        return reverse('userlist_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(UserListDetail, self).get_context_data(**kwargs)
        context['form'] = GetplanForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(UserListDetail, self).form_valid(form)


    # def get_context_data(self, **kwargs):                           
    #     #생성된 context는 Template으로 전달됨.
    #     context = super().get_context_data(**kwargs)                 
    #     context['form']=GetplanForm(self.request)                      
    #     return context


    # def get_context_data(self):
    #     bomuser = BomUser.objects.all()
    #     setplan = BomSetPlan.objects.all()
    #     context = {
    #         'bomuser': bomuser,
    #         'setplan' : setplan,
    #     }
    #     return context

class DangerView(FormView):
    template_name = 'danger_cf.html'
    form_class = DangerForm
    success_url = '/main'

class PerformanceView(FormView):
    template_name = 'perfor.html'
    form_class = PerformanceForm
    success_url = '/perfor'

    def get_context_data(self):
        performances = Performance.objects.all()
        context = {
            'performances': performances,
        }
        return context

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')

class UserView(FormView):
    template_name = 'initial.html'
    form_class = UserForm
    success_url = '/main'

def UserInfo(request):
    return render(request, 'userinfo.html')

class SetPlanView(FormView):
    template_name = 'setplan.html'
    form_class = SetplanForm
    success_url = '/main'

class GetPlanView(FormView):
    template_name = 'getplan.html'
    form_class = GetplanForm
    success_url = '/main'

# 검색필터로 detail 불러오기
def DB(request):
    qs = BomUser.objects.all()
    q = request.GET.get('search', '')
    if q:
        qs = qs.filter(C_Name__icontains=q)
    return render(request, 'db.html', {
        'DB': qs,
})

def user_data(request):
    bomusers = BomUser.objects.all()
    getplans = BomGetPlan.objects.all()
    setplans = BomSetPlan.objects.all()
    context = {'getplans':getplans,'bomusers':bomusers, 'setplans':setplans}

    return render(request, 'user_data.html', context)



# class SearchResultsView(ListView):
#     model = BomUser
#     template_name = 'getplan.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('search')
#         object_list = BomUser.objects.all()
#         context_object_name = 'user'
#         return object_list