
# coding: utf-8

# In[1]:


from datetime import datetime
import pandas as pd


# # User Input

# In[2]:


period_name = raw_input("Enter the playpen name, ie: playpen_1612 ... : \n")
aws_access_key_id = raw_input("Enter your aws access key ID : \n")
aws_secret_access_key = raw_input("Enter your aws secret access key: \n")
s3_path_to_unload = raw_input("Enter the s3 path to unload the data to, \n "
                              "by example: s3://tef.dev.core.uk/users/laura/forAlina : \n")


# In[3]:


# # Create Cell reference and range loading script

# In[4]:


unloading_script = []


unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_visitors_final') TO '%s/%s/dwells_visitors_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_workers_final') TO '%s/%s/dwells_workers_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name,s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_residents_final') TO '%s/%s/dwells_residents_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload,aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_workers_catchment_pen_final') TO '%s/%s/dwells_workers_catchment_pen_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_visitors_catchment_work_pen_final') TO '%s/%s/dwells_visitors_catchment_work_pen_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_visitors_catchment_pen_final') TO '%s/%s/dwells_visitors_catchment_pen_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name,s3_path_to_unload,  aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_visitors_daily_hourly_final') TO '%s/%s/dwells_visitors_daily_hourly_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_workers_daily_hourly_final') TO '%s/%s/dwells_workers_daily_hourly_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_residents_daily_hourly_final') TO '%s/%s/dwells_residents_daily_hourly_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name,s3_path_to_unload, aws_access_key_id, aws_secret_access_key))

# Weblogs
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_residents_web_final') TO '%s/%s/dwells_residents_web_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name,s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_workers_web_final') TO '%s/%s/dwells_workers_web_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name,s3_path_to_unload, aws_access_key_id, aws_secret_access_key))
unloading_script.append("UNLOAD ('SELECT * FROM %s.zz_ps_dwells_visitors_web_final') TO '%s/%s/zz_ps_dwells_visitors_web_final_' credentials 'aws_access_key_id=%s;aws_secret_access_key=%s' PARALLEL OFF BZIP2;" %(period_name,period_name, s3_path_to_unload, aws_access_key_id, aws_secret_access_key))



# In[6]:

unloading_script_print = '\n'.join(unloading_script)

with open(r'./loading_scripts/%s.sql' % (str(period_name)), 'w') as sql_script:
    sql_script.write(unloading_script_print)


print("All done !")