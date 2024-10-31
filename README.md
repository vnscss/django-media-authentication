
# Django Media Authentication


Este projeto implementa um sistema de controle de acesso para arquivos de mídia em um projeto Django. Ele utiliza o Django para definir permissões de acesso e o NGINX para servir arquivos protegidos de forma segura.

## Créditos

Este projeto é uma modificação de [protect-django-media-files-per-user-basis-with-nginx](https://b0uh.github.io/protect-django-media-files-per-user-basis-with-nginx.html) criado por [b0uh](https://github.com/b0uh).

## Funcionalidade

A view `media_access` define regras de acesso para arquivos de mídia, permitindo que:
1. Usuários autenticados acessem todos os arquivos.
2. Qualquer usuário (autenticado ou não) acesse arquivos em subpastas públicas.

Arquivos protegidos são servidos diretamente pelo NGINX após validação de permissão pelo Django.

## Estrutura do Código

- **`views.py`**: Contém a view `media_access`, que verifica a autenticação do usuário e a pasta solicitada antes de permitir ou negar o acesso.
- **`urls.py`**: Define a URL padrão para que `media_access` seja chamada quando arquivos de `/media/` forem acessados.
- **Configuração do NGINX**: Inclui um bloco `location /protected/` no arquivo de configuração do NGINX para servir arquivos protegidos.

## Configuração

1. **Configurar NGINX**:
   - Adicione o seguinte bloco, substituindo o `/media/`, ao seu arquivo de configuração do NGINX:
     ```nginx
     location /protected/ {
         internal;
         alias /CAMINHO/PARA/SEU-PROJETO;
     }
     ```
   - Substitua `/CAMINHO/PARA/SEU-PROJETO` pelo caminho correto dos arquivos de mídia.

2. **URLs no Django**:
   - Em `urls.py`, adicione o seguinte código para configurar a URL de acesso:
     ```python
     from django.urls import re_path
     from . import views

     urlpatterns = [
         re_path(r'^media/(?P<path>.*)', views.media_access, name='media')
     ]
     ```

## Observações

- Este exemplo utiliza o cabeçalho `X-Accel-Redirect` para que o NGINX sirva os arquivos protegidos diretamente.
- Para permissões de acesso, você pode modificar a lista de pastas públicas (`public`) no código conforme necessário.
