from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from email_professores import EMAIL_PROFESSORES
from TP2_ProgWeb.utils import sendPassword
from usuario.models import Professor, Aluno
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from usuario.choices import STATE_CHOICES
from debian.changelog import change

# Create your views here.

def index(request):
    return render_to_response('usuario/login.html', RequestContext(request))

def user_login(request):
    return render_to_response('usuario/login.html', RequestContext(request))

def cadastro(request):
    return render_to_response('usuario/confirma_email.html', RequestContext(request))

def cadastro_aluno(request):
    return render_to_response('usuario/cadastro_aluno.html', RequestContext(request))

def cadastrar_aluno(request):
    nome = request.POST.get('nome')
    matricula = request.POST.get('mat')
    inputEmail = request.POST.get('email')
    password = request.POST.get('novasenha')
    Aluno.objects.create_user(inputEmail, inputEmail, password, first_name=nome, aluno_matricula=matricula)
    return render_to_response('usuario/cadastro_aluno_confirmado.html', RequestContext(request))

def cadastro_invalido(request):
    return render_to_response('usuario/cadastro_invalido.html', RequestContext(request))

def login_invalido(request):
    return render_to_response('usuario/login_invalido.html', RequestContext(request))

def email_confirmado(request):
    return render_to_response('usuario/email_confirmado.html', RequestContext(request))

def verificar_login(request):
    u = request.POST.get('inputEmail')
    p = request.POST.get('inputPassword')
    print 'login'
    user = authenticate(username=u, password=p)
    if user is not None:
        login(request, user)
        print "login efetuado"
        print "usuario do tipo " + repr(type(request.user))
#         print Aluno.objects.filter(username=u).count()
#         print Professor.objects.filter(username=u).count()
        if Aluno.objects.filter(username=u).count():
            print "aluno"
        else:
            print "nao eh aluno"
        if Professor.objects.filter(username=u).count():
            print "professor"
        else:
            print "nao eh professor"
        return render_to_response('usuario/principal.html', RequestContext(request))
    print "login faiado"
    return render_to_response('usuario/login.html', RequestContext(request))

def verificar_email(request):
    inputEmail = request.POST.get('inputEmail')
    if inputEmail in EMAIL_PROFESSORES.keys():
        password = User.objects.make_random_password()
        Professor.objects.create_user(inputEmail, inputEmail, password)
        sendPassword(inputEmail, password)
        return render_to_response('usuario/email_confirmado.html', RequestContext(request)) # fazer pagina de email enviado com informacoes para login
    return render_to_response('usuario/cadastro_invalido.html', RequestContext(request)) # fazer pagina de email nao cadastrado na base de dados do sistema

@login_required(login_url='/user_login/')
def editar_perfil(request):
    if Aluno.objects.filter(username=request.user.username).count():
        print 'perfil de aluno'
        user_data = Aluno.objects.filter(username=request.user.username).values()[0]
        return render_to_response('usuario/editar_perfil_aluno.html', RequestContext(request, user_data))
    elif Professor.objects.filter(username=request.user.username).count():
        print 'perfil de professor'
        user_data = Professor.objects.filter(username=request.user.username).values()[0]
        user_data['estados'] = [x[0] for x in STATE_CHOICES]
        return render_to_response('usuario/editar_perfil_professor.html', RequestContext(request, user_data))
    else:
        print('Error: You are None =P')
    return render_to_response('usuario/principal.html', RequestContext(request))

def persistir_perfil_aluno(request):
    user_data = Aluno.objects.filter(username=request.user.username).values()[0]
    aluno = Aluno.objects.get(user_id=user_data['user_id'])
    
    aluno.first_name = request.POST.get('nome')
    aluno.aluno_matricula = request.POST.get('matricula')
    aluno.email = request.POST.get('email')
    password = request.POST.get('password')
    novasenha = request.POST.get('novasenha')
    confirmanovasenha = request.POST.get('confirmanovasenha')
    
    change_pass = False
    if aluno.check_password(password):
        if novasenha != '' and novasenha != None:
            if novasenha == confirmanovasenha:
                aluno.set_password(novasenha)
                change_pass = True
        aluno.save()
    user_data = Aluno.objects.filter(username=request.user.username).values()[0]
    if change_pass:
        login(request, authenticate(username=aluno.username, password=novasenha))
    return render_to_response('usuario/editar_perfil_aluno.html', RequestContext(request, user_data))
    

def persistir_perfil_professor(request):
    user_data = Professor.objects.filter(username=request.user.username).values()[0]
    professor = Professor.objects.get(user_id=user_data['user_id'])
    
    professor.first_name = request.POST.get('nome')
    professor.email = request.POST.get('email')
    professor.professor_numero_da_sala = request.POST.get('num')
    professor.professor_endereco_logradouro = request.POST.get('logradouro')
    professor.professor_endereco_bairro = request.POST.get('bairro')
    professor.professor_endereco_cidade = request.POST.get('cidade')
    professor.professor_endereco_estado = request.POST.get('estado')
    professor.professor_endereco_cep = request.POST.get('cep')
    password = request.POST.get('password')
    novasenha = request.POST.get('novasenha')
    confirmanovasenha = request.POST.get('confirmanovasenha')
    
    change_pass = False
    if professor.check_password(password):
        if novasenha != '' and novasenha != None:
            if novasenha == confirmanovasenha:
                professor.set_password(novasenha)
                change_pass = True
        professor.save()
    user_data = Professor.objects.filter(username=request.user.username).values()[0]
    if change_pass:
        login(request, authenticate(username=professor.username, password=novasenha))
    user_data['estados'] = [x[0] for x in STATE_CHOICES]
    return render_to_response('usuario/editar_perfil_professor.html', RequestContext(request, user_data))

@login_required(login_url='/user_login/')
def principal(request):
    return render_to_response('usuario/principal.html', RequestContext(request))

@login_required(login_url='/user_login/')
def user_logout(request):
    logout(request)
    print "logout"
    return render_to_response('usuario/login.html', RequestContext(request))