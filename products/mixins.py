from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import UserPassesTestMixin



@method_decorator(login_required, name='dispatch')
class SuperUserRequiredMixin(UserPassesTestMixin):

    def test_func(self):

        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, only store owners can do that.')
        return redirect('home')
