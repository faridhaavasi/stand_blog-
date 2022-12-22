from django.shortcuts import redirect


class cast_Login_required_Mixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super(cast_Login_required_Mixin, self).dispatch(request, *args, **kwargs)
