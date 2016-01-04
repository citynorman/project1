from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('test-temp.html')

def renderfile(email,name,cc):
    output_from_parsed_template = template.render(name=name)
    print email
    print output_from_parsed_template
    if(cc=="TRUE"):
        print '***cc***'
        

import csv
with open('test-temp.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        renderfile(row['Mail'],row['Name'],row['cc'])

# to save the results
#with open("test-temp-out.html", "wb") as fh:
#    fh.write(output_from_parsed_template)
