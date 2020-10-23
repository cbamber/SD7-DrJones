from datetime import datetime
from workdays import networkdays


class DateTimeHelpers:
    @staticmethod
    def _getDateDiff(dtfrom, dtto):
        dt1 = datetime.strptime(dtfrom, "%Y-%m-%dT%H:%M:%S.%f%z")
        dt2 = datetime.strptime(dtto, "%Y-%m-%dT%H:%M:%S.%f%z")
        workdaydiff2 = networkdays(dt1, dt2)

        return workdaydiff2
