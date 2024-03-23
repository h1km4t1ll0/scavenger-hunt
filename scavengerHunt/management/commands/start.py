import time
from traceback import print_exc

from django.core.management.base import BaseCommand

import scavengerHunt.src.bot
from scavengerHunt.src.bot import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        scavengerHunt.src.bot.pohuy()
