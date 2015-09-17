import http_client as http
from  datetime import datetime, timedelta
from time import strptime
import calendar

url = "http://move1t.herokuapp.com/monthly_summary.json"

months =  ['May', 'June', 'July', 'August', 'September']
user_details = []

def date_range():
    first_day_of_tracking = datetime.strptime('2015 ' + months[0] + ' 1', "%Y %B %d").date()

    last_day_of_tracking = datetime.today().date()

    return [first_day_of_tracking, last_day_of_tracking]

def zero_datas(email, work_out_dates):
    zero_data = []
    work_out_dates.extend(date_range())
    sorted_dates = sorted(work_out_dates)

    date_set = set(sorted_dates[0]+timedelta(x) for x in range((sorted_dates[-1]-sorted_dates[0]).days))
    missing_dates = sorted(date_set-set(sorted_dates))
    if(len(missing_dates) > 0):
        for missing_date in missing_dates:
            zero_data.append({'email': email, 'date': missing_date, 'duration': '0' })
    return zero_data


with open('user_emails.txt') as user_emails:
    with open('very_new_user_data.txt', 'w') as user_data_file:
        user_emails_list = filter(None, user_emails.read().split('\n'))
        for email in user_emails_list:
            email = email.rstrip()
            work_out_dates = []
            for month in months:
                data = { 'email': email, 'month': month + ' 2015' }
                user_data = http.get(url, data)
                for details in user_data['user']['monthly_summary']:
                    date = datetime.strptime(details['date'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
                    work_out_dates.append(date)
                    duration = details['duration']
                    print email, month, date, duration
                    user_details.append({'email': email, 'date': date, 'duration': duration })
            user_details.extend(zero_datas(email, work_out_dates))
        for user_detail in user_details:
            user_data_file.write(user_detail['email'] + ' ' + user_detail['date'].strftime('%Y/%m/%d') + ' ' + str(user_detail['duration']) + '\n')

