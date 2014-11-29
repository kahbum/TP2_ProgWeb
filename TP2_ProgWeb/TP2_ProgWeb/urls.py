from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TP2_ProgWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'usuario.views.index'),
    url(r'^user_login/', 'usuario.views.user_login'),
    url(r'^user_logout/', 'usuario.views.user_logout'),
    url(r'^cadastro/', 'usuario.views.cadastro'),
    url(r'^verificar_login/$', 'usuario.views.verificar_login'),
    url(r'^verificar_email/$', 'usuario.views.verificar_email'),
    url(r'^cadastro_aluno/', 'usuario.views.cadastro_aluno'),
    url(r'^cadastrar_aluno/', 'usuario.views.cadastrar_aluno'),
    url(r'^cadastro_invalido/', 'usuario.views.cadastro_invalido'),
    url(r'^email_confirmado/', 'usuario.views.email_confirmado'),
    url(r'^principal/', 'usuario.views.principal'),
    url(r'^editar_perfil/', 'usuario.views.editar_perfil'),
    url(r'^persistir_perfil_aluno/', 'usuario.views.persistir_perfil_aluno'),
    url(r'^persistir_perfil_professor/', 'usuario.views.persistir_perfil_professor'),
    url(r'^user_logout/', 'usuario.views.user_logout'),
#     url(r'^editar_perfil/$', 'usuario.views.editar_perfil'),
)
