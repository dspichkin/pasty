# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from core.models import Source
from core.sync import sync_rss_source


class Command(BaseCommand):
    help = u'Загрузка пирожков из источников'

    def handle(self, *args, **options):
        if len(args) > 0:
            for arg in args:
                source = Source.objects.get(pk=arg)
                print u'Загрузка пирожков из %s' % (source)
                sync_rss_source(source)
        else:
            for source in Source.objects.all():
                print u'Загрузка пирожков из %s' % (source)
                sync_rss_source(source)
