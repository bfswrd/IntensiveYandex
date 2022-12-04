from rating.models import Rating
from catalog.models import Item
from catalog.views import item_detail


def rate(request, post_id: int, rating: int):
    post = Item.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return item_detail(request)
