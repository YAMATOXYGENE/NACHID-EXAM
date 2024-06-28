from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Joke

class JokeListView(ListView):
    model = Joke
    template_name = 'jokes/list_jokes.html'
    context_object_name = 'jokes'

class JokeDetailView(DetailView):
    model = Joke
    template_name = 'jokes/joke_detail.html'
    context_object_name = 'joke'

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    fields = ['question', 'answer']
    template_name = 'jokes/create_joke.html'
    success_url = reverse_lazy('jokes:list_jokes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(LoginRequiredMixin, UpdateView):
    model = Joke
    fields = ['question', 'answer']
    template_name = 'jokes/update_joke.html'
    success_url = reverse_lazy('jokes:list_jokes')

class JokeDeleteView(LoginRequiredMixin, DeleteView):
    model = Joke
    template_name = 'jokes/delete_joke.html'
    success_url = reverse_lazy('jokes:list_jokes')

class SignupView(FormView):
    template_name = 'jokes/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('jokes:list_jokes')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
