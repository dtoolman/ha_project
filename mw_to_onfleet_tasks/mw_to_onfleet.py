import requests
import pandas as pd
import math
import json
from io import StringIO


def get_and_clean_data():
    
    ######################################
    #  Get CSV data from MembershipWorks #
    ######################################

    # TODO: Probably use Mrs. Pavett's login for the header
    headers = {
        'Host': 'api.membershipworks.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://membershipworks.com/',
    }
    url = 'https://api.membershipworks.com/v1/csv?SF=CqQWGT-YS7JxJ_bUsfioO19G7RRw20fxFqwfydzIOsevPF71KzKIEwB3pOXj0FhV&_rt=946706400&frm=618575991ea12250a05d87dd'

    req = requests.get(url, headers=headers)
    data = StringIO(req.text)
    df = pd.read_csv(data)

    #####################################################
    #  Convert the quantities in the CSV data to colors #
    #####################################################

    df['Task Details (Bag Color)'] = ''

    for i in range(len(df.index)):
        if not math.isnan(df.loc[i, 'Item: Small Bag']):
            color = 'White'
        elif not math.isnan(df.loc[i, 'Item: Medium Bag']):
            color = 'Green'
        elif not math.isnan(df.loc[i, 'Item: Large Bag']):
            color = 'Blue'
        else:
            raise ValueError('Bag quantities at row ' + str(i) + ' are invalid')
        df.loc[i, 'Task Details (Bag Color)'] = color

    #########################################
    #  Add data to the Notes column as JSON #
    #########################################

    def if_not_null(val):
        if pd.isnull(val):
            return ''
        return val

    for i in range(len(df.index)):
        notes = {
            'notes': if_not_null(df.loc[i, 'Notes']),
            'county': if_not_null(df.loc[i, 'County']),
            'referred_by': if_not_null(df.loc[i, 'Referred by (Select 1)']),
            'referred_by_other_source': if_not_null(df.loc[i, 'Referred by other source?']),
            'household_size': int(df.loc[i, 'Household Size'])
        }
        df.loc[i, 'Notes'] = json.dumps(notes)

    return df


if __name__ == '__main__':
    get_and_clean_data().to_csv(path_or_buf='finished.csv')
