from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import UserPassesTestMixin


@method_decorator(login_required, name='dispatch')
class SuperUserRequiredMixin(UserPassesTestMixin):
    ''' Class to require that a user is both logged in and
        a superuser of the site.

        Inherits UserPassesTestMixin from django.
        '''

    def test_func(self):

        # check if user is a registered superuser
        return self.request.user.is_superuser

    def handle_no_permission(self):

        # return error message and redirect to home page if criteria not met
        messages.error(self.request, 'Sorry, only store owners can do that.')
        return redirect('home')
