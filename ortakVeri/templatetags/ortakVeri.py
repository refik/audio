from django import template
register = template.Library()


#def link_url(parser,token):
#    tag_name, linkObject = token.split_contents()
#    return linkUrl(linkObject)

#class linkUrl(template.Node):
#    def __init__(self,linkObject):
#        self.link = template.Variable(linkObject)
#    def render(self,context):
#        link = self.link.resolve(context)
#        if link.sayfa:
#            return link.sayfa.url
#        elif link.dokuman:
#            return '/dokuman/' + link.dokuman.slug
#        elif link.kategori:
#            return '/urunler/' + link.kategori.slug
#        elif link.urun:
#            return '/urun/' + link.urun.slug
#        elif link.direklink:
#            return link.direklink
#        elif link.dosya:
#            return link.dosya.url
#        else:
#            return '#'

#register.tag('linkUrl',link_url)

def linkUrl(value):
    if value.sayfa:
        return value.sayfa.url
    elif value.dokuman:
        return '/dokuman/' + value.dokuman.slug + '/'
    elif value.kategori:
        return '/urunler/' + value.kategori.slug + '/'
    elif value.urun:
        return '/urun/' + value.urun.slug + '/'
    elif value.direklink:
        return value.direklink
    elif value.dosya:
        return value.dosya.url
    else:
        return '#'

register.filter('linkUrl',linkUrl)
