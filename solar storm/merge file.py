import pandas as pd

# Load both files
symh_df = pd.read_csv("merged_storm_data.csv")
kpap_df = pd.read_csv("Kp_ap_Ap_SN_F107_since_1932.csv")

symh_df['Date'] = pd.to_datetime(
    symh_df['Year'].astype(str) + symh_df['Day'].astype(str), format='%Y%j'
)

# Create date in Kp file from explicit column mapping (FIX)
kpap_df['Date'] = pd.to_datetime({
    'year': kpap_df['YYYY'],
    'month': kpap_df['MM'],
    'day': kpap_df['DD']
})

# Merge
merged_df = pd.merge(symh_df, kpap_df, on='Date', how='left')

# Optional cleanup
merged_df.drop(columns=['YYYY', 'MM', 'DD', 'days', 'days_m'], inplace=True, errors='ignore')

# Save merged result
merged_df.to_csv("merged_symh_kpap.csv", index=False)
print("✅ Final merge complete. Saved as merged_symh_kpap.csv")