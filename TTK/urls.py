from django.urls import path
from . import views
from .views import *

app_name = 'TTK'

urlpatterns = [
    path('Register', Register, name = 'Register'),
    path('Login', Login, name = 'Login'),
    path('Logout', Logout, name = 'Logout'),
    #ppppppppppppppppppppppppppppppppppppppp
    path('About', About, name = 'About'),
    path('Contact', Contact, name = 'Contact'),
    path('Team', Team, name = 'Team'),
    path('Services', Services, name = 'Services'),
    path('', index, name = 'index'),
]