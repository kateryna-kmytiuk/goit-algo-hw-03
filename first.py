from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        return (date - datetime.today().date()).days
    except ValueError:
        print('Incorrect date format.')

    

date = input('Input data in format YYYY-MM-DD: ')
res = get_days_from_today(date)
if res != None:
    if res < 0:
        print(f'It was {abs(res)} days ago')
    elif res > 0:
        print(f'It will be in {res} days')
    else:
        print('It is today')


