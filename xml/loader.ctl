load data
infile 'Z:\Temp\dodd\combine_interp.csv'
into table dodd.interp
fields terminated by ',' optionally enclosed by '"'
(ID,TYPE,VALUE)