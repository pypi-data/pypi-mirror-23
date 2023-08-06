#!/usr/bin/env python
import sys, json, re
def parse(content, ignore_errors=False, process=True):
  buf = ""
  quote = False
  data = {}
  for x in content:
    if not quote and x == ";":
      try:
        k,v = map(str.strip, buf.split("=", 1))
      except ValueError:
        if not ignore_errors:
          raise ValueError("not a key=value:\n=== BEGIN ===\n%s\n=== END ===" % buf)
      else:
        if v.startswith("{") and v.endswith("}"):
          v = '[%s]' % v[1:-1]
        elif not v.startswith('"') or not v.endswith('"'):
          v = '"%s"' % v.replace('"', '\\"')
        try:
          data[k] = json.loads(v)
        except ValueError as e:
          if not ignore_errors:
            raise ValueError("JSON parser gave %s:\n=== BEGIN ===\n%s\n=== END ===" % (e,v))
      buf = ""
    elif x == '"' and not buf.endswith("\\"):
      buf += x
      quote = not quote
    else:
      buf += x
  if process:
    data_del = []
    for k in data:
      m = re.search("^(.*)_(append|override)$", k)
      if m and m.group(1) in data and m.group(2) == "append":
        data[m.group(1)] += data[k]
        data_del.append(k)
      elif m and m.group(1) in data and m.group(2) == "override":
        data[m.group(1)] = data[k]
        data_del.append(k)
    for k in data_del:
      del data[k]
  return data
