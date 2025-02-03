import json

dt = '{"x": 10, "y": 30}'
print(json.loads(dt)["y"]   )
