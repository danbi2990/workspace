from project.audit_quote.ETL_quotes import ETL_quotes

file = 'quotation_seoul_transport.tsv'
collection = 'c1_seoul_transport'
ETL_quotes(file, collection)
