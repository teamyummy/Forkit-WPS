from .models import Restaurant, Menu, Review
from .models import RestaurantImg, RestaurantTag, ReviewImg
from .models import RestaurantFavor, ReviewLike
from .serializers import RestaurantSerializer, MenuSerializer
from .serializers import RestaurantImgSerializer
from .serializers import ReviewSerializer, TagSerializer
from .serializers import FavorSerializer
from .serializers import ReviewImgSerializer
from .serializers import LikeSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.serializers import ValidationError
from .perms import IsOwnerOrReadOnly

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(register=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)

#    def list(self, request, *args, **kwargs):
#        pk = kwargs['pk']
#        queryset = self.get_queryset()
#        queryset.filter(restaurant=pk)
#        serializer = 


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)


class RestaurantImgList(generics.ListCreateAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)


class RestaurantImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        review = serializer.save(author=self.request.user, restaurant=restaurant)
        restaurant.review_count += 1
        restaurant.review_score += review.score
        restaurant.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=restaurant)


class TagList(generics.ListCreateAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)


class FavorList(generics.ListCreateAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantFavor.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(user=self.request.user, restaurant=restaurant)
        restaurant.total_like += 1
        restaurant.save()


class FavorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer
    permission_classes = (IsOwnerOrReadOnly, )



class ReviewImgList(generics.ListCreateAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(review=review)
    

class ReviewImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)


class LikeList(generics.ListCreateAPIView):
    queryset = ReviewLike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewLike.objects.filter(review=review)
        
    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        user = self.request.user

        if ReviewLike.objects.filter(user=user, review=review).exists():
            raise ValidationError( { "non_field_errors":
                    "[ Like(user[{}],review[{}]) already exists ]"
                    .format(user.username, review.title) })

        like = serializer.save(user=user, review=review)
        if like.up_and_down > 0:
            review.like += like.up_and_down
        else:
            review.dislike += -like.up_and_down
        
        review.save()


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewLike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        self.review = get_object_or_404(Review, pk=review_id)
        return ReviewLike.objects.filter(review=self.review)

    def perform_update(self, serializer):
        org_score = serializer.instance.up_and_down
        new_score = serializer.validated_data['up_and_down']
        
        if org_score == new_score:
            return

        if org_score > 0:
            self.review.like -= org_score
        else:
            self.review.dislike += org_score

        if new_score > 0:
            self.review.like += new_score
        else:
            self.review.dislike += -new_score

        serializer.save()
        self.review.save()
        
    def perform_destroy(self, instance):
        if instance.up_and_down > 0:
            self.review.like -= instance.up_and_down
        else:
            self.review.dislike += instance.up_and_down

        instance.delete()
        self.review.save()


