from .models import Company


def companies(request):
    return {"categories": Company.objects.all(is_active=True)}
