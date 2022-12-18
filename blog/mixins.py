from django.shortcuts import redirect

class Login_required_Mixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super(Login_required_Mixin, self).dispatch(*args, **kwargs)