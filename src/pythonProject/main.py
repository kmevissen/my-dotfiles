import pandas as pd


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    dtypes = {
        'EventDate': 'str',
        'AffiliateCode': 'str', 'CabinClass': 'str', 'supplier': 'str',
        'OutboundDepartureCode': 'str', 'OutboundDepartureCity': 'str',
        'OutboundDepartureCountry': 'str', 'OutboundDepartureRegion': 'str',
        'OutboundArrivalCode': 'str', 'OutboundArrivalCity': 'str', 'OutboundArrivalCountry': 'str',
        'OutboundArrivalRegion': 'str', 'OutboundDepartureDate': 'str',
        'InboundDepartureCode': 'str', 'InboundDepartureCity': 'str',
        'InboundDepartureCountry': 'str', 'InboundDepartureRegion': 'str',
        'InboundArrivalCode': 'str', 'InboundArrivalCity': 'str', 'InboundArrivalCountry': 'str',
        'InboundArrivalRegion': 'str', 'InboundDepartureDate': 'str', 'ShopRequestCounts': 'int64',
        'SessionSearchCounts': 'int64', 'HasClicks': 'int64', 'TotalClickCount': 'int64', 'HasBookings': 'int64',
        'TotalBookingCount': 'int64', 'BookedSegmentsCount': 'int64'

    }

    df = pd.read_csv("~/Downloads/compare_oid_schedule_shop_data_20210616_000000000000.csv", dtype=dtypes)
    print(df.dtypes)

    s = df.head(10)
    print(df.shape)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
