from django import forms
from captcha.fields import CaptchaField
class UserForm(forms.Form):
	username = forms.CharField(label="用户名", max_length=128)
	password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
	captcha = CaptchaField(label="验证码")
