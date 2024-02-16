import pandas as pd

# Assuming you have the original DataFrame 'prices_df' with a DatetimeIndex
data = {'datetime': ['2019-01-01 00:00:00', '2019-01-01 01:00:00', '2019-01-01 02:00:00',
                     '2019-01-01 03:00:00', '2019-01-01 05:00:00'],
        'price_eur': [51.0, 46.27, 39.78, 20.0, 22.0]}

prices_df = pd.DataFrame(data)
prices_df['datetime'] = pd.to_datetime(prices_df['datetime'])
prices_df.set_index('datetime', inplace=True)

# Resample the DataFrame to fill missing rows with NaN values
resampled_df = prices_df.resample('1H').asfreq()

# Interpolate the missing values using linear interpolation
imputed_df = resampled_df.interpolate(method='linear')

# Print the resulting DataFrame
# print(imputed_df)


data = {'col': [{'aabc': {'a':1, 'b':1, 'c':2, 'd': 3}, 'bbac': {'a':2, 'b':2, 'c':5, 'd': 3}}]}

df = pd.DataFrame(data)
print([(k, v) for d in df['col'] for k, v in d.items()])

result = pd.DataFrame([(k, v) for d in df['col'] for k, v in d.items()], columns=['code', 'value'])

print(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        print(int(n ** 0.5) + 1)
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(7))  # True
print(is_prime(12))  # False


d = {'a':1, 'b':2, 'c': 3}
print(list(d.keys()))