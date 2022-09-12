Hi. I have build a simple register form with Django.

Before these codes you should be sure you added 'templates' in your project/settings/TEMPLATES and then be sure you added 'crispy_forms' and 'your_apps_name' to the INSTALLED_APPS. (If you want bootstrap you should add "CRISPY_TEMPLATE_PACK = 'bootstrap4'" under the installed_apps )

Second importhing issue that your forms file should be in the same app with models and views.

Thirdly issue is that when you are gonna use HTML with your apps do not use HTML use Django Template

