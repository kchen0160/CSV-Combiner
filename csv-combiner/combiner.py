import pandas as pd
import sys
import os

# create an empty dataframe
df = pd.DataFrame()

# loop through the input files
for file in sys.argv[1:]:
    # read the file into a dataframe
    temp_df = pd.read_csv(file)
    # add a new column with the filename
    temp_df['filename'] = os.path.basename(file)
    # append the rows to the main dataframe
    df = df.append(temp_df)

# write the output to stdout
df.to_csv(sys.stdout, index=False)