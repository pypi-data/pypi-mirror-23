import logging

from django.core.management import BaseCommand

from atris.models import get_history_model

logger = logging.getLogger('old_history_deleting')
HistoricalRecord = get_history_model()


class Command(BaseCommand):
    help = """
        Deletes historical records older than the specified days or months.
        You must supply either the days or the weeks param.
    """

    PARAM_ERROR = 'You must supply either the days or the weeks param'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            dest='days',
            type=int,
            default=None,
            help='Any historical record older than the number of days '
                 'specified gets deleted.'
        )
        parser.add_argument(
            '--weeks',
            dest='weeks',
            type=int,
            default=None,
            help='Any historical record older than the number of months '
                 'specified gets deleted.'
        )

    def handle(self, *args, **options):
        days = options.get('days')
        weeks = options.get('weeks')
        if not (days or weeks):
            self.stderr.write("{msg}\n".format(
                msg=self.PARAM_ERROR,
            ))
            return
        old_history_entries = HistoricalRecord.objects.older_than(days, weeks)
        handled_entries_nr = old_history_entries.count()
        old_history_entries.delete()
        self.stdout.write('{} deleted.\n'.format(handled_entries_nr))
