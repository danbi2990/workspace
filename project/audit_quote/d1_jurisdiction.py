from project.audit_quote.ETL_quotes import ETL_quotes

file = 'quotation_jurisdiction.tsv'
collection = 'd1_jurisdiction'
ETL_quotes(file, collection)
