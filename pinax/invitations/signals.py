import django
import django.dispatch


def Signal(providing_args=None):
    if django.VERSION < (4, 0, 0):
        return django.dispatch.Signal(providing_args=providing_args)
    else:
        return django.dispatch.Signal()


invite_sent = Signal(providing_args=["invitation"])
invite_accepted = Signal(providing_args=["invitation"])
joined_independently = Signal(providing_args=["invitation"])
