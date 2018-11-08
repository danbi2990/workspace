from project.audit_quote.ETL_quotes import ETL_quotes

file = 'quotation_kindergarten.tsv'
collection = 'b1_kindergarten'
ETL_quotes(file, collection)
