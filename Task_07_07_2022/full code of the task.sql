use task;
select * from supplier_data_csvformat;
select * from sales_data_csvformat;
select * from product_data_csvformat;

create table stg_final_report(
Supplier_Namee varchar(225),
Supplier_regionn varchar(225),
Supplier_idd varchar(225),
Product_idddd varchar(225),
total varchar(225),
monthly varchar(225),
Quantity varchar(225)
);

insert into stg_final_report
select no_table.Supplier_Namee Supplier_Namee,
no_table.Supplier_regionn Supplier_regionn,
no_table.Supplier_idd Supplier_idd,
no_table.Product_idddd Product_idddd,
sum(no_table.totalll) total,
no_table.monthly monthly,
Quantity
from 
(select sdc.supplier_name Supplier_Namee,sdc.region Supplier_regionn,temp_table.supplier_id Supplier_idd,
temp_table.product_id Product_idddd,
temp_table.total_sales_ammount totalll, 
temp_table.price price,
mid(date,4,2) as monthly,
temp_table.total_sales_ammount/temp_table.price Quantity
from 
(select supplier_id,ssd.product_id,total_sales_ammount,date,pdc.price 
from sales_data_csvformat ssd
join product_data_csvformat pdc on ssd.product_id = pdc.product_id) temp_table
join supplier_data_csvformat sdc on temp_table.supplier_id = sdc.supplier_id
group by Quantity) no_table

group by no_table.monthly,no_table.Supplier_Namee,no_table.Product_idddd
limit 100
;

