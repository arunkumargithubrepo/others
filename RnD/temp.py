import urllib.request

link = urllib.request.urlopen('https://www.hireitpeople.com/resume-database/'
                              '73-datawarehousing-etl-informatica-resumes/69631-big-data-engineer-resume-cincinnati-oh')
for line in link:
    if 'Resume' in str(line):
        print(line)


