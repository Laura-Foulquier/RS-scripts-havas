# Build SQL Scripts HAVAS



## What does it do
Simple python scripts which creates the SQL scripts needed to unload the data from Redshift to a specified s3 path.
Once created, import the SQL script to Redshift and just run the different commands.


## Which version of Python is this developed in
This script has been developed using Python 2.7

## Which libraries do I need to install
You will need to install the following addtional libraries:

* pandas

## What additional information do I need to provide 

* The playpen in which the tables exist
* Your AWS ACCESS KEY ID
* Your AWS SECRET ACCESS KEY
* The S3 path to unload the tables to

## What 

12 tables are used in the script:

* zz_ps_dwells_visitors_final
* zz_ps_dwells_workers_final
* zz_ps_dwells_residents_final
* zz_ps_dwells_workers_catchment_pen_final
* zz_ps_dwells_visitors_catchment_work_pen_final
* zz_ps_dwells_visitors_catchment_pen_final
* zz_ps_dwells_visitors_daily_hourly_final
* zz_ps_dwells_workers_daily_hourly_final
* zz_ps_dwells_residents_daily_hourly_final
* zz_ps_dwells_residents_web_final
* zz_ps_dwells_workers_web_final
* zz_ps_dwells_visitors_web_final

All tables will be saved in the following path:
<s3 path to unload to>/<playpen>/<table_name>_000





