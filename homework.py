import datetime as dt


class Record:
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = float(amount)
        self.comment = comment
        if isinstance(date, dt.date) == False:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = date


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.new_record = new_record
        self.records.append(new_record)

    def get_today_stats(self):
        today_amount = 0
        for record in self.records:
            if record.date == dt.date.today():
                today_amount += abs(record.amount)
        return float(today_amount)

    def get_week_stats(self):
        week_amount = 0
        for record in self.records:
            if record.date >= (dt.date.today() - dt.timedelta(days=7)) and record.date <= dt.date.today():
                week_amount += abs(record.amount)
        return float(week_amount)


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        self.currency = currency
        today_limit = self.get_today_stats()
        if today_limit < self.limit:
            if currency == 'rub':
                return (f'На сегодня осталось {round((self.limit - today_limit), 2)} руб')
            elif currency == 'usd':
                return (
                    f'На сегодня осталось {round(((self.limit - today_limit) / CashCalculator.USD_RATE), 2)} USD')
            elif currency == 'eur':
                return (
                    f'На сегодня осталось {round(((self.limit - today_limit) / CashCalculator.EURO_RATE), 2)} Euro')



        elif today_limit == self.limit:
            return ('Денег нет, держись')

        elif today_limit > self.limit:
            if currency == 'rub':
                return (f'Денег нет, держись: твой долг - {round((today_limit - self.limit), 2)} руб')
            elif currency == 'usd':
                return (
                    f'Денег нет, держись: твой долг - {round(((today_limit - self.limit) / CashCalculator.USD_RATE), 2)} USD')
            elif currency == 'eur':
                return (
                    f'Денег нет, держись: твой долг - {round(((today_limit - self.limit) / CashCalculator.EURO_RATE), 2)} Euro')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        today_limit = int(self.get_today_stats())
        if self.limit > today_limit:
            return (
                f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {int(self.limit - today_limit)} кКал')
        else:
            return ('Хватит есть!')
