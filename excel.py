import re
 from pandas import DataFrame

with open('log.txt', 'r', encoding='utf-8') as f:
     log = f.read()

search_pattern = (
 r"""\bItem #: (\d+)\s+"""
 r"""Job name: (.+)\s+"""
 r"""Status: (.+)\s+"""
 r"""Started: (.+)"""
 r"""\s+On date: (.+)\s+"""
 r"""Last ran: (.+)\s+"""
 r"""On date: (.+)\s+"""
 r"""Elapsed time: (.+)\s+"""
 """Description:(.*)"""
 )

pattern = re.compile(search_pattern)

item, job_name, status, \
 start_date_time, end_date_time, \
 elapsed_time, description  = ([] for _ in range(7))

matches = pattern.finditer(log)
for match in matches:
     item.append(match.group(1))
     job_name.append(match.group(2))
     status.append(match.group(3))
     start_date_time.append(match.group(4)+' '+match.group(5))
     end_date_time.append(match.group(6)+' '+match.group(7))
     elapsed_time.append(match.group(8))
     description.append(match.group(9))

df = DataFrame(
  {'Item': item,
  'Job Name': job_name,
  'Status': status,
  'Start Time': start_date_time,
  'End Time': end_date_time,
  'Elapsed Time': elapsed_time,
  'Description': description,
  })
#print(df)
df.to_excel('job_status.xlsx', sheet_name='sheet1', index=False)
