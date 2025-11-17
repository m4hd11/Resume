from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('website:index')  # Change 'home' to your desired redirect URL
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Change 'home' to your desired redirect URL
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome aboard.')
            return redirect('home')  # Change 'home' to your desired redirect URL
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    
    def form_valid(self, form):
        messages.success(self.request, 'Password reset email has been sent. Please check your inbox.')
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:password_reset_complete')
    token_generator = default_token_generator  # اضافه کردن این خط
    
    def dispatch(self, *args, **kwargs):
        # برای دیباگ - ببینیم چه اتفاقی داره میفته
        from django.utils import timezone
        print(f"Reset link accessed at: {timezone.now()}")
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Your password has been reset successfully!')
        return super().form_valid(form)
    
def form_invalid(self, form):
    messages.error(self.request, 'Invalid username or password. Please try again.')
    return self.render_to_response(self.get_context_data(form=form))
