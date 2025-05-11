import csv

# Input and output file paths
input_file = 'Kp_ap_Ap_SN_F107_since_1932.txt'       # <-- Replace with your actual .txt filename
output_file = 'kp_ap_full_data.csv'     # <-- Desired output filename

# Define headers
headers = [
    'Year', 'Month', 'Day',
    'Kp1', 'Kp2', 'Kp3', 'Kp4', 'Kp5', 'Kp6', 'Kp7', 'Kp8',
    'ap1', 'ap2', 'ap3', 'ap4', 'ap5', 'ap6', 'ap7', 'ap8',
    'Ap', 'SN', 'F10.7obs', 'F10.7adj', 'D'
]

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)

    for line in infile:
        # Strip and split line by whitespace
        parts = line.strip().split()

        # Skip header or malformed lines
        if len(parts) < 29 or parts[0] == 'YYYY':
            continue

        try:
            # Extract values
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])

            kp_values = parts[8:16]      # Kp1 to Kp8
            ap_values = parts[16:24]     # ap1 to ap8
            ap_daily = parts[24]         # Ap
            sn = parts[25]               # Sunspot number
            f10_7_obs = parts[26]        # F10.7 observed
            f10_7_adj = parts[27]        # F10.7 adjusted
            d_flag = parts[28]           # Data quality flag

            # Combine row
            row = [year, month, day] + kp_values + ap_values + [ap_daily, sn, f10_7_obs, f10_7_adj, d_flag]
            writer.writerow(row)

        except Exception as e:
            print(f"⚠️ Skipping line due to error: {e}")
            continue

          

print(f"✅ Conversion complete. File saved as: {output_file}")
