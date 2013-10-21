from django.core.exceptions import ImproperlyConfigured


def get_post_model():
    from django.conf import settings
    from django.db.models import get_model

    post_model = getattr(settings, 'NEWS_POST_MODEL', 'news.Post')

    try:
        app_label, model_name = post_model.split('.')
    except ValueError:
        raise ImproperlyConfigured("NEWS_POST_MODEL must be of the form 'app_label.model_name'")
    user_model = get_model(app_label, model_name)
    if user_model is None:
        raise ImproperlyConfigured("NEWS_POST_MODEL refers to model '%s' that has not been installed" % post_model)
    return user_model
