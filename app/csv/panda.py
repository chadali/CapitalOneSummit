import pandas as pd

def removeColumns():
    data = pd.read_csv('listings.csv', nrows=10)
    # Keeping data that would make for interesting graphs and requirements of course. Removed stuff that involves free text area submissions.
    # Throw away Weekly / Montly price discounts to keep every single entry uniform
    keep_col=['neighbourhood', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'amenities', 'price', 'weekly_price', 'monthly_price', 'cleaning_fee', 'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value']
    newFile = data[keep_col]
    newFile.to_csv("formatted.csv", index=False)

def displayFile():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    data = pd.read_csv('formatted.csv')
    print(data)

if __name__ == '__main__':
    command = input("Write or Read? \n")
    if command == 'write':
        removeColumns()
    elif command == 'read':
        displayFile()
    else:
        print("no command")

