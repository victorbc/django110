import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instace, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	KirrURL = instace.__class__
	qs_exists = KirrURL.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code