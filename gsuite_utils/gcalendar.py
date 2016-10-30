from __future__ import print_function
from datetime import datetime
import httplib2
import sys
from apiclient import discovery
from gsuite_utils.credentials import get_credentials

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gsuite_utilities_gcalendar.json
LOCAL_CREDENTIAL_FILE = 'gsuite_utilities_gcalendar.json'
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret_gsuite_utilities.json'
APPLICATION_NAME = 'G Suite Utilities'


def gcalendar_service():
    """
    Creates a Google Calendar API service object
    :return: a Google Calendar API service object
    """
    credentials = get_credentials(
        LOCAL_CREDENTIAL_FILE,
        CLIENT_SECRET_FILE,
        SCOPES,
        APPLICATION_NAME
    )
    http = credentials.authorize(httplib2.Http())
    return discovery.build('calendar', 'v3', http=http)


def gcalendar_events(service):
    """
    Outputs a list of the next 10 events on the user's calendar.
    :param service: a Google Calendar API service object
    :return: a list
    """
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=20,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return eventsResult.get('items', [])


def main():
    service = gcalendar_service()

    events = gcalendar_events(service)

    if not events:
        print('No upcoming events found.')
    for event in events:
        start_time = event['start'].get('dateTime', event['start'].get('date'))
        end_time = event['end'].get('dateTime', event['end'].get('date'))
        duration = calc_duration(start_time, end_time)
        print(start_time, end_time, duration, event['summary'], event['status'])


def calc_duration(start_time, end_time):
    DATETIME_STR_FORMAT_1 = '%Y-%m-%dT%H:%M:%S+11:00'
    DATETIME_STR_FORMAT_2 = '%Y-%m-%dT%H:%M:%S+10:00'

    t_delta_secs = 3600 # default to 1 hour

    for f in [DATETIME_STR_FORMAT_1, DATETIME_STR_FORMAT_2]:
        try:
            end_dt = datetime.strptime(end_time, f)
            start_dt = datetime.strptime(start_time, f)
            t_delta_secs = (end_dt - start_dt).seconds
            break
        except:
            pass

    return '{:02d}:{:02d}'.format(t_delta_secs/3600, t_delta_secs%3600/60)

if __name__ == '__main__':
    sys.exit(main())
