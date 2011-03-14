# encoding: utf-8

__all__ = ['SMSTransporrt']

log = __import__('logging').getLogger(__name__)


class SMSTransport(object):
	def __init__(self, **kw):
		self.config = kw
	
	def startup(self):
		pass
	
	def __call__(self, message):
		pass # Deliver the message.
	
	def shutdown(self):
		pass