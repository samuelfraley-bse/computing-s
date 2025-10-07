import pandas

def filter_countries_by_active_cases(df, threshold):
    return df[df['active'] > threshold]

def average_death_confirmed_ratio(df):
    return (df['deaths'] / df['confirmed']).mean()

def analyze_by_thresholds(df, thresholds):
    for t in thresholds:
        filtered = filter_countries_by_active_cases(df, t)
        avg_ratio = average_death_confirmed_ratio(filtered)
        print(t, avg_ratio)

if __name__ == '__main__':
    df = pandas.read_csv('covid.csv')
    analyze_by_thresholds(df, [500, 1000, 5000])
