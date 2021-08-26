import csv

# function allows reading random samples from a big file to be processed
def read_big_csv(file_name: str, sample_row = 1000, random_sample = False):
    '''
    Parameters
    ----------
    file_name : str
        location of the file being processed/directory.
    sample_row : int, optional
        defines the number of rows to be read into the dataframe from the original file. 
        The default is 1000.
    random_sample : bool, optional
        if True sample_row will be doubled and sampled using df.choice. 
        The default is False.

    Returns
    -------
    pd.DataFrame
        dataframe object.
    '''
    with open(file_name, encoding='utf-8') as csvfile:
        temp = csv.reader(csvfile)
        counter = -1 #skipping column as the first count
        row_list = []
        
        if random_sample == True:
            value = 2
        else:
            value = 1
        
        with tqdm(total=sample_row * value) as pbar:
            
            while counter < sample_row * value:
                row_list.append(next(temp))
                counter += 1
                pbar.update(1)
                
        df = pd.DataFrame(columns = row_list[0], data = row_list[1:])
        
        if value == 2:
            df1 = df.sample(n = sample_row)
            return df1
        else:
            return df

# ontain 10K rows from dataset
# df1 = read_big_csv('dataunpacked_df_title.csv', sample_row = 2000, random_sample = False)
# df2 = read_big_csv('dataunpacked_df_body.csv', sample_row = 2000, random_sample = False)
# df3 = read_big_csv('dataunpacked_df_tags.csv', sample_row = 2000, random_sample = False)

# df = pd.concat([df1, df2, df3], axis=1)

# label = read_big_csv(r'C:\Users\behna\OneDrive\Documents\Data Science - Projects\20210608 StackOverflow\2. Prepared Data\train.csv', 
#                   sample_row = 2000)