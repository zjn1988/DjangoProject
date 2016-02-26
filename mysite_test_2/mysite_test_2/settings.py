"""
Django settings for mysite_test_2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import sqlserver_ado

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5)+doqk&p@cg3pn4t!m$uqnf^!!z1y4testqrb20$vj2cp4vga'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'App1',#注册app
	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite_test_2.urls'

WSGI_APPLICATION = 'mysite_test_2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		# 'NAME': 'master',#很重要！！！
        # 'ENGINE': 'sqlserver_ado',
        # 'HOST': '172.22.131.85',
        # 'USER': 'zjn',
        # 'PASSWORD': 'zhangjiannan',
		# 'PORT':'',
		# 'OPTIONS':{
			# 'use_mars':True,
			# 'provider':'sqloledb',#did not been tested ,do not know if this could be change
		#	'extra_params': 'Extended Properties=PLSQLRSet=1;Persist Security Info=True;',
		# }
    },
	'mssql': {
		'NAME': 'Position_DB',#很重要！！！
		#'NAME': 'master',#很重要！！！
		'ENGINE': 'sqlserver_ado',
        'HOST': '172.22.131.85',
        'USER': 'zjn',
        'PASSWORD': 'zhangjiannan',
		'PORT':'',
		#'schema':'PFP',
		'OPTIONS':{
			'use_mars':True,
			'provider':'sqloledb',#did not been tested ,do not know if this could be change
			#'schema':'PFP',
			#'options': '-c search_path=PFP'
			#'extra_params': 'Extended Properties=PLSQLRSet=1;Persist Security Info=True;',
		}
    }
	# python manage.py inspectdb --database mssql > App1/models.py
}
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'console':{
		'level':'DEBUG',
		'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
#多数据连接：确定数据库连接方式
DATABASE_ROUTERS = ['mysite_test_2.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # example:
    #'app_name':'database_name',
    'App1': 'mssql',
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#语言及时区
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
