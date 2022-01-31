from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):

        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, only store owners can do that.')
        return redirect('home')
