from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, FormView
from catalog.models import Item
from rating.forms import RatingForm
from rating.models import Rating
from django.shortcuts import reverse


def item_list(request):
    items = Item.objects.published().order_by("category__name", "name")

    context = {
        "items": items,
    }
    return render(request, "catalog/item_list.html", context=context)


class ItemDetail(FormView):
    form_class = RatingForm

    model = Item
    template_name = "catalog/item_detail.html"
    queryset = Item.objects.published

    def get(self, request, *args: str, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args: str, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_initial(self):
        return {"rating": Rating.objects.get_or_none_rating(
            self.request.user.id, self.kwargs["pk"]), }

    def form_valid(self, form):
        rating = form.cleaned_data["rating"]
        user_id = self.request.user.id
        item_id = self.kwargs["pk"]
        if Rating.objects.get_or_none_rating(
                self.request.user.id, self.kwargs["pk"]):
            Rating.objects.update(
                rating=rating, user_id=user_id, item_id=item_id)
        else:
            Rating.objects.create(
                rating=rating, user_id=user_id, item_id=item_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:item_detail', kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["item"] = get_object_or_404(
            self.queryset(), pk=self.kwargs.get('pk'))
        return data

    def get_queryset(self):
        return Item.objects.published()
