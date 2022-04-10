"""
INSTRUCTIONS:

While pairing with and explaining your thinking to the interviewer, review the
below code and explain to the interviewer what it is trying to accomplish, as well
as the strengths and weaknesses of how it is written.

Then, take the code and improve and refactor it as you feel is appropriate.
If there are any bugs, those would be the most important things to fix, but
code performance, cleanliness, formatting, and anything else is fair game to change. 
The goal of this challenge is not only to see what you notice, but to see what matters 
to you when writing or editing code.
"""
import os

import requests

# pip3 install python-dotenv
# Load .env file using:
from dotenv import load_dotenv
load_dotenv('states_with_most_jobs.ini')


def states_with_most_jobs(clone, count, unique=False):
    '''
    Returns the state with the most jobs

    Params:
     clone - dict from main(..)
     unique - returns the states with most unique position titles
     count - number of states to return

    '''
    states = []
    biggest_job_counts = []

    while count > 0:
        big_state = None
        big_num = 0
        for state, _ in clone.items():
            if count == None:
                big_state = state
                big_num = len(clone[state])
            else:
                num = len(clone[state])
                if num > big_num and not (num in biggest_job_counts):
                    big_state = state
                    big_num = num
                    biggest_job_counts.append(big_num)
        states.append(big_state)
        count -= 1

    return states


def get_data(url, host_dns, _payload):
    # 'uAE5mkc61hl6qdUmp1okypCi6dMZbudqMa++R90IE7I='
    authKey = os.getenv('authKey')
    userAgent = os.getenv('userAgent')  # 'petercho39@gmail.com'

    r = requests.get(url, headers={'Host': host_dns, 'User-Agent': userAgent,
                                   'Authorization-Key': authKey}, params=_payload)

    return r.json()


def consume_job_api():
    '''
    Searches for jobs using https://data.usajobs.gov/api/search and returns the states with most jobs
    '''
    payload = {'PositionTitle': 'Software Engineer', 'Page': 1}
    json_data = get_data(
        'https://data.usajobs.gov/api/search', 'data.usajobs.gov', payload)
    number_of_pages = int(
        json_data['SearchResult']['UserArea']['NumberOfPages'])
    dict = {}
    page = 1
    while page < number_of_pages:
        print(f'Grabbing page {page}')
        payload['Page'] = page
        json_data = get_data(
            'https://data.usajobs.gov/api/search', 'data.usajobs.gov', payload)
        search_result_items = json_data.get('SearchResult', {})[
            'SearchResultItems']
        for item in search_result_items:
            for location in item['MatchedObjectDescriptor']['PositionLocation']:
                if location['CountryCode'] == 'United States':
                    if location['CountrySubDivisionCode'] in dict:
                        dict[location['CountrySubDivisionCode']].append(
                            item['MatchedObjectDescriptor']['PositionTitle'])
                    else:
                        dict[location['CountrySubDivisionCode']] = [
                            item['MatchedObjectDescriptor']['PositionTitle']]

        page += 1
    top_states = states_with_most_jobs(dict, 2)

    print('Top 2 states for Software Engineer jobs:')
    for i, state in enumerate(top_states, 1):
        print(f'{i}. {state}')


if __name__ == "__main__":
    consume_job_api()
