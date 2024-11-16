def parsetrack():
  field = []
  for line in open("field.in"):
    field.append(line.strip())

  track = []
  seen = set()
  x, y = 0, 0
  DIRS = [(+1,0),(-1,0),(0,+1),(0,-1)]

  while True:

    for dx, dy in DIRS:
      nx = x + dx
      ny = y + dy

      if (nx, ny) in seen: continue

      if not (0 <= ny < len(field)): continue
      if not (0 <= nx < len(field[ny])): continue

      if field[ny][nx] != " ":
        x, y = nx, ny
        track.append(field[ny][nx])
        break

    if (x, y) in seen:
      break
    seen.add((x, y))

  return "".join(track)

def totscore(plan):
  OP = {
    "+": lambda x: x+1,
    "-": lambda x: x-1,
    "=": lambda x: x,
  }

  cur_points = 10
  tot_points = 0
  i = 0
  while i < 2024*len(track):

    if track[i%len(track)] == "+":
      cur_points += 1
    elif track[i%len(track)] == "-":
      cur_points -= 1
    else:
      cur_points = OP[plan[i%len(plan)]](cur_points)

    tot_points += cur_points
    i+=1

  return tot_points

def allplans(plus, minus, eq):
  if plus == minus == eq == 0:
    return ""

  plans = []

  if plus > 0:
    plans.extend("+" + ap for ap in (allplans(plus-1, minus, eq) or [""]))
  if minus > 0:
    plans.extend("-" + ap for ap in (allplans(plus, minus-1, eq) or [""]))
  if eq > 0:
    plans.extend("=" + ap for ap in (allplans(plus, minus, eq-1) or [""]))

  return plans

track = parsetrack()

enemy_plan = input().split(":")[1].split(",")
enemy_score = totscore(enemy_plan)

res = 0
for p in allplans(5,3,3):
  if totscore(p) > enemy_score:
    res += 1

print(res)
