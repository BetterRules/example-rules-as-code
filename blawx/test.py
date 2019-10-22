#!/usr/bin/env python

import requests

if __name__ == "__main__":
  blawxfile = file.open('beard.blawx')
  if blawxfile.mode() == "r":
    blawx_code = blawxfile.read()
  
  datafile = file.open('../shared/example_beards.json')
  if datafile.mode() == "r":
    data = datafile.read()
  
  #may need to make changes to the json structure that gets sent
  #Blawx is expecting a dictionary, not a list.
  
  payload = {'code': blawx_code, 'data': data}
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  url = 'https://www.blawx.com/cgi-bin/reasoner6.php'
    
  r = requests.post(url,headers=headers,data=payload)
  output = r.json() 
  testcount = 0
  testsuccess = 0
  testfailure = 0
  for result in output['answers']:
    testcount += 1
    if result['passed'] == "true":
      testsuccess += 1
    else:
      testfailure += 1
  print('Run {line_count} tests. {passes} passes. {failures} failures.'.format(
            line_count=testcount, passes=testsuccess, failures=testfailure))
