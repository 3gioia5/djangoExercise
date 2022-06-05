from django.shortcuts import render, get_object_or_404
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from allauth.account.models import EmailAddress
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from coplate.models import Review, User
from coplate.forms import ReviewForm
from coplate.functions import confirmation_required_redirect


# Create your views here.
class IndexView(ListView):
  model = Review
  template_name = "coplate/index.html"
  context_object_name = "reviews"
  paginate_by = 4
  ordering = ["-dt_created"]


class ReviewDetailView(DetailView):
  model = Review
  template_name  = "coplate/review_detail.html"
  pk_url_kwarg = "review_id"


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Review
  form_class = ReviewForm
  template_name = "coplate/review_form.html"

  redirect_unauthenticated_users = True
  raise_exception = confirmation_required_redirect

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})
  
  def test_func(self, user):
    return EmailAddress.objects.filter(user=user, verified=True).exists()
  

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Review
  form_class = ReviewForm
  template_name = "coplate/review_form.html"
  pk_url_kwarg = "review_id"

  raise_exception = True

  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})

  def test_func(self, user):
    review = self.get_object()
    return review.author == user
  

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Review
  template_name = "coplate/review_confirm_delete.html"
  pk_url_kwarg = "review_id"

  raise_exception = True

  def get_success_url(self):
    return reverse("index")
  
  def test_func(self, user):
    review = self.get_object()
    return review.author == user


class ProfileView(DetailView):
  model = User
  template_name = "coplate/profile.html"
  pk_url_kwarg = "user_id"
  context_object_name = "profile_user"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.kwargs.get("user_id")
    context["user_reviews"] = Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]
    return context


class UserReviewListView(ListView):
  model = Review
  template_name = "coplate/user_review_list.html"
  context_object_name = "user_reviews"
  paginate_by = 4

  def get_queryset(self):
    user_id = self.kwargs.get("user_id")
    return Review.objects.filter(author__id=user_id).order_by('-dt_created')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
    return context


class CustomPasswordChangeView(PasswordChangeView):
  def get_success_url(self):
    return reverse("index")
