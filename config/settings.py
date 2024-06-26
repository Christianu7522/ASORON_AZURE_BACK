"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from django.utils import timezone
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pu%416k_k!mbqg1t_9@t-4_vph$ji8)wqxps*=bi*3j!(b)h$5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'import_export',
    'corsheaders',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'asoron',
    'rest_framework',
    'djoser',
    'rest_framework_simplejwt',
    'django_filters',
    
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS=False

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'admin/img'),
    os.path.join(BASE_DIR,'css'),
]

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

ROOT_URLCONF = 'config.urls'

INTERNAL_IPS = [
    "127.0.0.1",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

JAZZMIN_SETTINGS = {
    "site_title": "AsoRon UCAB",
    "site_header": "AsoRon UCAB",
    "site_brand": "AsoRon",
    "site_icon": 'logo.png',
    "site_logo": 'LogoSingin.png',
    "welcome_sign": " AsoRon Admin Site",
 
    "copyright": "AsoRon",
    "user_avatar": 'user_personal.jpg',
    "site_logo_classes": "img-circle",
    "topmenu_links": [
        {"name": "Admin", "url": "home", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
 
    "show_sidebar": True,
    
    "order_with_respect_to":['core','auth','asoron','asoron.historicopunto','asoron.historicodolar','asoron.tienda','asoron.compra','asoron.detallecompra','asoron.tipotienda','asoron.inventariotienda','asoron.ron','asoron.tiporon','asoron.clasificacionron','asoron.clasificaciontipo','asoron.anejamiento','asoron.barril','asoron.metodofermentacion','asoron.metododestilacion','asoron.color','asoron.comoservir','asoron.gradoalcohol','asoron.botella','asoron.oferta','asoron.tipobotella','asoron.material','asoron.materialron','asoron.materiaprima','asoron.materialtipobotella','asoron.tapamaterial','asoron.tapa','asoron.caja','asoron.lugar','asoron.sensacion','asoron.notacata','asoron.evento','asoron.entradaevento','asoron.premio','asoron.proveedor','asoron.personacontacto','asoron.empleado','asoron.notificacion','asoron.departamento','asoron.vacacion','asoron.horario','asoron.beneficio','asoron.cargo','asoron.asistencia','asoron.clientejuridico','asoron.tipocomercio','asoron.clientenatural','asoron.telefono','asoron.telefonocodigo'],
    "navigation_expanded": True,
    "icons": {
        'asoron.clasificacionron':'fas fa-regular fa-star',
        'asoron.tiporon':'fas fa-solid fa-industry',
        'asoron.clasificaciontipo':'fas fa-solid fa-signature',
        'asoron.empleado':'fas fa-regula fa-user-tie',
        'asoron.departamento':'fas fa-regular fa-cash-register',
        'asoron.clientejuridico':'fas fa-solid fa-person-booth',
        'asoron.clientenatural':'fas fa-regular fa-user',
        'asoron.telefono':'fas fa-solid fa-phone',
        'asoron.telefonocodigo':'fas fa-regular fa-flag',
        'asoron.tipocomercio':'fas fa-solid fa-store',
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-cog",
        "admin.LogEntry": "fas fa-file",
        "core.usuario": "fas fa-regular fa-users",
        'asoron.ron':"fas fa-solid fa-wine-bottle",
        'asoron.sensacion':"fas fa-solid fa-list",
        'asoron.material':"fas fa-regular fa-brush",
        'asoron.materialron':"fas fa-solid fa-recycle",
        'asoron.materiaprima':"fas fa-solid fa-seedling",
        'asoron.materialtipobotella':"fas fa-solid fa-recycle",
        'asoron.tapamaterial':"fas fa-solid fa-recycle",
        'asoron.caja':"fas fa-solid fa-box-open",
        'asoron.color':"fas fa-solid fa-palette",
        'asoron.comoservir':"fas fa-solid fa-glass-whiskey",
        'asoron.gradoalcohol':"fas fa-solid fa-temperature-low",
        'asoron.lugar':"fas fa-solid fa-map-marker-alt",
        'asoron.tipobotella':"fas fa-solid fa-wine-bottle",
        'asoron.anejamiento':"fas fa-solid fa-hourglass-half",
        'asoron.barril':"fas fa-regular fa-trash",
        'asoron.metodofermentacion':"fas fa-solid fa-water",
        'asoron.metododestilacion':"fas fa-solid fa-flask",
        'asoron.proveedor':"fas fa-solid fa-truck",
        'asoron.tapa':"fas fa-solid fa-ring",
        'asoron.vacacion':"fas fa-solid fa-tree",
        'asoron.horario':"fas fa-solid fa-clock",
        'asoron.beneficio':"fas fa-solid fa-gift",
        'asoron.asistencia':"fas fa-solid fa-calendar-check",
        'asoron.cargo':"fas fa-solid fa-user-tag",
        'asoron.personacontacto':"fas fa-solid fa-user-friends",
        'asoron.evento':"fas fa-solid fa-calendar-alt",
        'asoron.premio':"fas fa-solid fa-trophy",
        'asoron.notacata':"fas fa-solid fa-star",
        'asoron.tipotienda':"fas fa-solid fa-store",
        'asoron.tienda':"fas fa-solid fa-store-alt",
        'asoron.inventariotienda':"fas fa-solid fa-store-alt-slash",
        'asoron.botella':'fas fa-solid fa-wine-bottle',
        'asoron.oferta':'fas fa-solid fa-percent',
        'asoron.entradaevento':'fas fa-solid fa-ticket-alt',
        'asoron.compra':'fas fa-solid fa-shopping-cart',
        'asoron.detallecompra':'fas fa-solid fa-shopping-basket',
        'asoron.historicodolar':'fas fa-solid fa-dollar-sign',
        'asoron.historicopunto':'fas fa-solid fa-chart-line',
        'asoron.afiliado':'fas fa-solid fa-user-check',
        'asoron.carrito':'fas fa-solid fa-shopping-cart',
        'asoron.carritoitem':'fas fa-solid fa-shopping-basket',
        'asoron.venta':'fas fa-solid fa-shopping-cart',
        'asoron.notificacion':'fas fa-solid fa-bell',
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    "related_modal_active": False,
    "custom_js": None,
    "custom_css": "custom.css",
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-pink",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}
AUTH_USER_MODEL = 'core.Usuario'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        
    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}",
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer',
    },
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
SITE_NAME = "ASORON"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

current_time = timezone.now()

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AUTH_PASSWORD_VALIDATORS=[
    {
        'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS": {
            "min_length": 9,
        }
    },
    {
        'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
    },  
]