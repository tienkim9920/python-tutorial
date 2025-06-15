# chatbot/management/commands/import_email.py
from django.core.management.base import BaseCommand
from emailapp.models import Email
from datetime import datetime

class Command(BaseCommand):
    help = 'Import sample Email data'

    def handle(self, *args, **kwargs):
        Email.objects.all().delete()

        Email.objects.create(
            title='Thông báo lịch phỏng vấn',
            description='Phỏng vấn lúc 14h00',
            time=datetime.strptime('04/05/2025', '%d/%m/%Y'),
            status=False
        )

        Email.objects.create(
            title='Kết quả phỏng vấn',
            description='Chúc mừng bạn',
            time=datetime.strptime('04/05/2025', '%d/%m/%Y'),
            status=True
        )

        Email.objects.create(
            title='Thông báo lịch đi làm việc',
            description='Thứ 2 đến thứ 6',
            time=datetime.strptime('04/05/2025', '%d/%m/%Y'),
            status=False
        )

        self.stdout.write(self.style.SUCCESS('✅ Import Email data thành công!'))
