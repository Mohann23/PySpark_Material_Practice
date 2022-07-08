use task;
select * from supplier_data_csvformat;
select * from sales_data_csvformat;
select * from product_data_csvformat;

select sdc.supplier_name,sdc.region,temp_table.supplier_id,
temp_table.product_id,
temp_table.total_sales_ammount total,temp_table.date, 
temp_table.total_sales_ammount/temp_table.price Quantity  
from 
(select supplier_id,ssd.product_id,total_sales_ammount,date,pdc.price 
from sales_data_csvformat ssd
join product_data_csvformat pdc on ssd.product_id = pdc.product_id) temp_table
join supplier_data_csvformat sdc on temp_table.supplier_id = sdc.supplier_id
group by temp_table.date;

