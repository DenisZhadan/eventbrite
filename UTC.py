from datetime import datetime, timedelta


class UTC:
    @staticmethod
    def get_last_sunday_of_month(year, month):
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)

        last_day_of_month = next_month - timedelta(days=1)
        last_sunday = last_day_of_month - timedelta(days=(last_day_of_month.weekday() + 1) % 7)
        return last_sunday.day

    def is_dst(self, dt):
        # Daylight saving time in Estonia starts on the last Sunday of March and ends on the last Sunday of October
        year = dt.year
        dst_start = datetime(year, 3, self.get_last_sunday_of_month(year, 3), 3)
        dst_end = datetime(year, 10, self.get_last_sunday_of_month(year, 10), 4)

        return dst_start <= dt < dst_end

    def tallinn_to_utc(self, tallinn_time_str):
        tallinn_time = datetime.strptime(tallinn_time_str, '%Y-%m-%d %H:%M:%S')

        if self.is_dst(tallinn_time):
            offset = timedelta(hours=3)  # Summer Time  (EEST, UTC+3)
        else:
            offset = timedelta(hours=2)  # Winter Time (EET, UTC+2)

        utc_time = tallinn_time - offset

        return utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    def convert_to_utc(self, local_time_str, local_tz_str):
        match local_tz_str:
            case 'Europe/Tallinn':
                utc = self.tallinn_to_utc(local_time_str)
            case _:
                utc = self.tallinn_to_utc(local_time_str)

        return utc
