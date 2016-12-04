from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        owner = getattr(obj, 'register', None) or \
                getattr(obj, 'author', None) or \
                getattr(obj, 'user', None)

        if owner is None:
            if hasattr(obj, 'restaurant'):
                restaurant = getattr(obj, 'restaurant')
                owner = restaurant.register
            elif hasattr(obj, 'review'):
                review = getattr(obj, 'review')
                owner = review.author

        if owner is None:
            return False

        return owner == request.user

