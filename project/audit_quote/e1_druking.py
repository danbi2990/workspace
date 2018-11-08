from project.audit_quote.ETL_quotes import ETL_quotes

file = 'quotation_druking.tsv'
collection = 'e1_druking'
ETL_quotes(file, collection)
