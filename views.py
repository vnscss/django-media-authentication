from django.http import HttpResponse, HttpResponseForbidden

def media_access(request, path):

    #subpastas do /media/ que são públicas
    public = [
    "noticias",
    "thumbnails",
    "textura",
    "publicacoes",
    "elementos",
    "design",
    "editais"
    ]

    encoded_path = urllib.parse.quote(path)
    target_folder = encoded_path.split('/')[0]
    access_granted = ''
    user = request.user

    if user.is_authenticated:
            access_granted = True

    for x in public:
        if x == target_folder:
            access_granted = True

    if access_granted:
        response = HttpResponse()
        #redireciona para o nginx
        del response['Content-Type']
        response['X-Accel-Redirect'] = '/protected/media/' + encoded_path
        return response
    else:
        # raise PermissionDenied OU return HttpResponseForbidden()
        raise PermissionDenied
