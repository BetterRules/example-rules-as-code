#!/usr/bin/env python

import requests
import json


if __name__ == "__main__":
  blawxfile = file.open('beard.blawx')
  if blawxfile.mode() == "r":
    blawx_code = blawxfile.read()
  
  tests = json.load('../shared/example_beards.json')
  
  dictionary_tests = {i: a[i+1] for i in range(0, len(a) #in PROGreSS
  
  dictionary_tests = {}
  for t in tests:
    dictionary_tests['test'] = t
  
  data = json.dumps(dictionary_tests)
  
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
