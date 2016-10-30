# gsuite-utils

This repo contains simple scripts using 

1. Google Apps Admin SDK (Reports API) to retreive last N google drive activities
2. Google Calendar API to retrieve my next N calendar events (accepted invitations)

Please see [Quick Start: Google Apps Admin SDK - Reports API](https://developers.google.com/admin-sdk/reports/v1/quickstart/python) for the steps about 

1. enabling API access
2. create OAuth client ID and credential (client_secret.json)

## Locally Installing / Testing 

**Copy client_secret.json to gsuit_utils/**

**Linux**

    virtualenv env
    . env/bin/activate
    pip install -e .
    
    python gsuite_utils/gdrive.py
    python gsuite_utils/gcalendar.py
    
    # for running pytest
    pip install -r requirements-test.txt
    
    # for full testing with tox and building wheel
    ./test.sh

**Windows**

    virtualenv env
    env\Scripts\activate
    pip install -e .
    
    python gsuite_utils\gdrive.py
    python gsuite_utils\gcalendar.py
    
    # for running pytest
    pip install -r requirements-test.txt
    
    # for full testing with tox and building wheel
    test.bat
