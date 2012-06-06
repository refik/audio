from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.staticfiles import finders
from filebrowser.fields import FileBrowseField
from pyPdf import PdfFileReader, PdfFileWriter
import subprocess
import os

def dokuman_convert(instance):
    if True:
        dosya = instance.dosya
        klasor = dosya.filename_root + '-katalog-gorunumu-dosyalari'
        swfKlasor = os.path.dirname(dosya.path) + '/' + klasor
        default_storage.open(dosya.path).file.save_to_filename('/tmp/pdf')
        pdf = file('/tmp/pdf', 'rb')
        pdfPy = PdfFileReader(pdf)
        sayfa = pdfPy.getNumPages()
        size_x, size_y = pdfPy.getPage(0).mediaBox.upperRight
        if size_x > size_y:
            base = file(finders.find('yan.pdf'), 'rb')
        else:
            base = file(finders.find('portre.pdf'),'rb')
        pre_second_page = PdfFileReader(base).getPage(0)
        pre_second_page.mediaBox.upperRight = (size_x, size_y)
        second_page = PdfFileWriter()
        second_page.addPage(pre_second_page)
        stream = file('/tmp/fitted_page','wb')
        second_page.write(stream)
        stream.close()
        base.close()
        pdf.close()
        for i in range(0, sayfa + 1):
            args = ['/usr/local/bin/pdf2swf',
                    '/tmp/pdf', '-o',
                    '/tmp/' + '%d.swf' % (i + 1,),
                    '-f', '-T', '9', '-t', '-p',
                    '%d' % i, '-s', 'storeallcharacters']
            if i==0:
                args[1] = '/tmp/fitted_page'
                args[3] = '/tmp/2.swf'
                args[9] = '1'
                i = 1
            elif i == 1:
                args[3] = '/tmp/1.swf'
                i = 0
            # p = subprocess.Popen(args, stdout=subprocess.PIPE)
            # for line in iter(p.stdout.readline, ''):
            #     print line
            #     if line[:5] == 'ERROR' or line[:5] == 'FATAL':
            args += ['-s', 'poly2bitmap']
            p = subprocess.Popen(args)
            p.wait()
            name = swfKlasor + '/' + '%d.swf' % (i + 1,)
            swf_file = open('/tmp/%d.swf' % (i + 1,), 'rb')
            swf = swf_file.read()
            content = ContentFile(swf)
            default_storage.save(name, content)
            swf_file.close()
