from django.contrib.sitemaps import Sitemap

class Site(object):
    def __init__(self,url):
        self.url = url

    def get_absolute_url(self):
        return self.url

class EkstraSitemap(Sitemap):
    def items(self):
        return [Site('/teklif-formu/'), Site('/iletisim-formu/'), Site('/akademi-formu/'), Site('/bulten-formu/')]
