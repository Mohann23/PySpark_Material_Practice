use task;
SELECT * FROM stg_final_report;
select * from product_data_csvformat;
select 
Supplier_Namee, 
Supplier_regionn, 
Supplier_idd, 
Product_idddd, 
total, 
monthly, 
total/pdc.price Quantity
from stg_final_report
join product_data_csvformat pdc on stg_final_report.Product_idddd = pdc.product_id
group by Supplier_idd,Product_idddd,monthly;