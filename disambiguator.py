#!/usr/bin/python


import requests
import argparse
import sys
import json

def api_call(jsonobject):
  payload = {'data': json.dumps(jsonobject)}
  try:
    r = requests.get('http://121.254.173.77:2357/agdistis/run', params=payload)
  except Exception,e:
    print "Error in api call: %s"%e
    sys.exit(1)
  if r.status_code != 200:
    print "HTTP error code: %s"%r.status_code
    sys.exit(1)
  else:
    response = r.content
    return response
  
parser = argparse.ArgumentParser("disambiguator.py", description="Calls the OKBQA disambiguator web service")
parser.add_argument("--jsonstring", help="The input json string", type=str, dest='jsonstring')
parser.add_argument("--jsonfile", help="Path of the file containing the json input as string", type=str, dest='jsonfile')
try:
  args = parser.parse_args()
except Exception,e:
  print "Parse error: %s"%e
  sys.exit(1)


if not args.jsonstring and not args.jsonfile:
  print "Both input arguments were found to be empty: --jsonstring and --jsonfile. Please read README file for sample usage."
  parser.print_help()
  sys.exit(1)

if args.jsonstring and args.jsonfile:
  print "Only one of the two options may be used at a time: --jsonstring or --jsonfile."
  parser.print_help()
  sys.exit(1)

if args.jsonstring:
  try:
    json_object = json.loads(args.jsonstring)
  except ValueError, e:
    print "Json was not valid: %s"%e
    sys.exit(1)
  print api_call(json_object)
  sys.exit(1)
else:
  try:
    f = open(args.jsonfile)
  except Exception,e:
    print "File open failed: %s"%e
    sys.exit(1)
  json_string = f.read()
  f.close()
  try:
    json_object = json.loads(json_string)
  except ValueError, e:
    print "Json was not valid: %s"%e
    sys.exit(1)
  print api_call(json_object)
  sys.exit()
