from django import template
from django.urls import reverse
register=template.Library()
@register.inclusion_tag('home/includes/breadcrumbs.html',takes_context=True)
def get_breadcrumbs(context):
    request=context['request']
    path_parts=request.path.strip('/').split('/')
    breadcrumbs=[]
    current_path=''
    breadcrumbs.append({'name':'Home','url':reverse('home')})
    for part in path_parts:
        if not part:
            continue
        current_path+='/{part}'
        name=part.replace('-',' ').title()

        if part='menu':
            name='Menu'
            url=reverse('menu-page')
        elif part='about':
            name='About Us'
            url=reverse('about')
        elif part='reservations':
            name='Reservations'
            url=reverse('reservations')
        elif part='feedback':
            name='Feedback'
            url=reverse('feedback')
        elif part='contact':
            name='Contact us'
            url=reverse('contact')
        elif part='faq':
            name='FAQ'
            url=reverse('faq')
        else:
            url=current_path
        
        if part !='' and part!='home':
            if not breadcrumbs or breadcrumbs[-1]['name']!=name:
                breadcrumbs.append({'name':name,'url':url})
    if breadcrumbs.request.path.strip('/')==path_parts[-1] and len(breadcrumbs)>1:
        breadcrumbs[-1]['url']=None
    return {'breadcrumbs':breadcrumbs}
    

