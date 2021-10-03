import os

from django.db import models

from .settings import MEDIA_ROOT

"""
TITULO
PRINT(HOME) - capa - img do projeto
VIDEO
LINK DO CÓDIGO NO GIT HUB
"""

class Projeto(models.Model):

	titulo = models.CharField(
		max_length = 100,
		null = False,
		blank = False,
		unique = True,
	)
	
	capa = models.ImageField(
		upload_to= '',
		max_length=None,
		blank=False,
		unique=True,
		null=False,
	)
	
	@property
	def capa_path(self):
		if self.capa and hasattr(self.capa, 'url'):
			return self.capa.url
	
	iframe_video = models.TextField(
		unique=True,
		null = False,
		blank = False,
	)
	
	link_codigo = models.URLField(
		unique = True,
		null = False,
		blank = False,
		default = 'https://github.com/clcosta/'
	)

	objetos = models.Manager()
