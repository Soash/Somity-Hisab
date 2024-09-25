from primary_setup.models import CustomUser
from .models import Branch, ActiveBranch
from django.contrib.auth.models import AnonymousUser
from django.utils import translation
from django.utils import timezone
from .models import DPSInstallmentSchedule

def branches(request):
    language = request.session.get('language', 'en')
    translation.activate(language)
    request.LANGUAGE_CODE = language
    return {
        'branches': Branch.objects.all()
    }


# def active_branch_processor(request):
#     if isinstance(request.user, AnonymousUser):
#         active_branch = None
#     else:
#         active_branch = ActiveBranch.objects.filter(user=request.user).first()
#     return {'active_branch': active_branch}



from django.contrib.auth.models import AnonymousUser
from app1.models import ActiveBranch, Customer

def active_branch_processor(request):
    
    if isinstance(request.user, AnonymousUser):
        active_branch = None
    elif isinstance(request.user, Customer):
        active_branch = None
    elif isinstance(request.user, CustomUser):
        active_branch = ActiveBranch.objects.filter(user=request.user).first()
    else:
        active_branch = None

    return {'active_branch': active_branch}

