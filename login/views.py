from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.

def index(request):
	if not request.session.get('is_login', None):
		return redirect('/login/')
	return render(request, 'login/index.html')

def login(request):
	# 判断当前用户是否已登录，即判断session,如果是在线，则跳转到index页面
	if request.session.get('is_login', None):
		return redirect('/index/')
	if request.method == "POST":
		login_form = forms.UserForm(request.POST)
		message = "请检查填写的内容!"
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			try:
				user = models.User.objects.get(name=username)
			except:
				message="你输入的用户不存在！"
				# 用户不存在的错误信息提示给用户
				return render(request, 'login/login.html', locals())
			# 如果用户验证通过后再验证密码是否正确
			if user.password == password:
				request.session['is_login'] = True
				request.session['user.id'] = user.id
				request.session['user_name'] = user.name
				# print(username, password)
				# 用户密码正确，跳转到默认页index
				return redirect('/index/')
			else:
				message = "密码错误，请重新登录！"
				return render(request, 'login/login.html', locals())
		else:
			return render(request, 'login/login.html', locals())
	login_form = forms.UserForm()
	# 否则继续回到登录页面重新登录
	return render(request, 'login/login.html', locals())

def register(request):
	pass
	return render(request, 'login/register.html')
def logout(request):
	if not request.session.get('is_login', None):
		return redirect('/login/')
	request.session.flush()
	return redirect('/login/')