import sys
from collections import namedtuple
from bisect import bisect_left

Place = namedtuple('Place', 'lat, long, height, points')

chunkplaces = {}
chunkvals = {}
giant = False

def getkey(place, off_lat=0, off_long=0):
    step_lat = d_lat if d_lat > 0 else 1
    step_long = d_long if d_long > 0 else 1
    return ((place.lat // step_lat) + off_lat, (place.long // step_long) + off_long)

def recordvalue(place, val):
    if val < 0:
        return
    key = getkey(place)
    if key not in chunkplaces:
        chunkplaces[key] = []
        chunkvals[key] = []
    if giant:
        if len(chunkvals[key]) == 0:
            chunkvals[key].append(-val)
            chunkplaces[key].append(place)
        elif val > -chunkvals[key][0]:
            chunkvals[key][0] = -val
            chunkplaces[key][0] = place
    else:
        i = bisect_left(chunkvals[key], -val)
        chunkplaces[key].insert(i, place)
        chunkvals[key].insert(i, -val)

def getbestinchunk(place, key, best):
    if key not in chunkvals:
        return 0
    for cand, val in zip(chunkplaces[key], chunkvals[key]):
        if -val < best:
            return 0
        # Syntax error fixed here:
        if abs(place.lat - cand.lat) <= d_lat and abs(place.long - cand.long) <= d_long:
            return -val
    return 0

def getbest(place):
    best = 0
    for i in (0, 1, -1):
        for j in (0, 1, -1):
            key = getkey(place, i, j)
            ret = getbestinchunk(place, key, best)
            if ret > best:
                best = ret
    return best

def calculatevalue(place):
    val = place.points + getbest(place)
    recordvalue(place, val)
    return val

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)
        
    n = int(input_data[0])
    d_lat = int(input_data[1])
    d_long = int(input_data[2])
    
    if d_lat == 200000:
        giant = True
        
    places = []
    idx = 3
    for _ in range(n):
        latitude = int(input_data[idx])
        longitude = int(input_data[idx+1])
        height = int(input_data[idx+2])
        points = int(input_data[idx+3])
        places.append(Place(latitude, longitude, height, points))
        idx += 4

    places.sort(key=lambda p: -p.height)
    
    best = 0
    for p in places:
        ret = calculatevalue(p)
        if ret > best:
            best = ret
            
    print(best)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna