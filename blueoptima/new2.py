from msilib import Table
from msilib.schema import tables


id_task
tx_key
tx_issue_type
tx_summary
tx_status
ts_created_at
nu_time_spent_sec
ts_resolved_at
tx_resolution_label
fk_asignee
fk_sprint
fk_project





Assignee table
===================
tx_assignee_name
tx_assignee_email

Sprint Table
======================
id_sprint
tx_sprint_name
tx_sprint_desc

Project table
============================
id_project
tx_project_name
tx_project_alias


select * from task_table, asignee table where task_id = 123 on task_table.fk_assigne = asignee_table.id