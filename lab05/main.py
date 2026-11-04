from logstats import count_levels, top_errors, format_report

filename = input().strip()
with open(filename, encoding= 'utf-8') as log:
    counts = count_levels(log)
total = 0
for level in counts:
    total += counts[level]
ercount =counts.get('ERROR', 0)
brokencount= counts.get('BROKEN', 0)
print(total)
print(ercount)
print(brokencount)
with open(filename, encoding ="utf-8") as log:
    er  = top_errors(log, 3)
report =format_report(counts, er)
with open("report.txt", "w", encoding = "utf-8") as f:
    f.write(report)