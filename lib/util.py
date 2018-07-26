def save_df_to_tsv(df, destination, index=False):
    tsv = df.to_csv(sep='\t', index=index)
    with open(destination, 'w') as f:
        f.write(tsv)


def print_bulk_result(result):
    print('- bulk_write result:')
    print('match, insert, modify, upsert')
    print(f'{result.matched_count} {result.inserted_count} {result.modified_count} {result.upserted_count}')
