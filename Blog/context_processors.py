from .models import Avatar

def user_avatar(request):
    avatar = None
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=request.user)
        except Avatar.DoesNotExist:
            avatar = None
    return {'avatar': avatar}
