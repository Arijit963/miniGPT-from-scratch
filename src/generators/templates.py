# ==========================================================
# Language Templates
# ==========================================================

VERBS = [

    "show",
    "display",
    "find",
    "retrieve",
    "list",
    "fetch",
    "give me",
    "return",
    "identify",
    "provide",
    "tell me",
    "show me",
    "please list"
]

# ==========================================================
# Comparison Words
# ==========================================================

GREATER_THAN = [

    "above",
    "greater than",
    "more than",
    "over",
    "higher than",
    "exceeding",
    "at least"
]

LESS_THAN = [

    "below",
    "less than",
    "under",
    "lower than",
    "not exceeding",
    "at most"
]

# ==========================================================
# Numeric Query Templates
# ==========================================================

NUMERIC_PATTERNS = [

    "{verb} {table} with {field} {comparison} {value}",

    "{verb} all {table} where {field} is {comparison} {value}",

    "{verb} every {table} having {field} {comparison} {value}",

    "{verb} {table} whose {field} is {comparison} {value}",

    "which {table} have {field} {comparison} {value}",

    "return {table} where {field} {comparison} {value}",

    "I want {table} with {field} {comparison} {value}",

    "find {table} having {field} {comparison} {value}",

    "can you {verb} {table} with {field} {comparison} {value}",

    "please {verb} {table} with {field} {comparison} {value}"
]

# ==========================================================
# Device Status Templates
# ==========================================================

STATUS_PATTERNS = [

    "{verb} {status} devices",

    "{verb} all {status} devices",

    "{verb} every {status} device",

    "which devices are {status}",

    "list all {status} devices",

    "find {status} devices",

    "identify {status} devices",

    "return {status} devices",

    "give me {status} devices",

    "show me {status} devices"
]

# ==========================================================
# Room Templates
# ==========================================================

ROOM_PATTERNS = [

    "{verb} sensors in room {room}",

    "{verb} all sensors in room {room}",

    "{verb} every sensor in room {room}",

    "which sensors are in room {room}",

    "find sensors located in room {room}",

    "identify sensors in room {room}",

    "return sensors from room {room}",

    "give me sensors in room {room}",

    "show me sensors in room {room}",

    "list sensors inside room {room}"
]

# ==========================================================
# Location Templates
# ==========================================================

LOCATION_PATTERNS = [

    "{verb} devices in {location}",

    "{verb} all devices in {location}",

    "{verb} every device in {location}",

    "which devices are located in {location}",

    "find devices deployed in {location}",

    "identify devices in {location}",

    "return devices from {location}",

    "give me devices in {location}",

    "show me devices in {location}",

    "list devices installed in {location}"
]

# ==========================================================
# Aggregation Templates
# ==========================================================

COUNT_PATTERNS = [

    "count all {table}",
    "how many {table} are there",
    "show the total number of {table}",
    "find the number of {table}",
    "return the count of {table}",
    "give me the total {table}",
    "what is the number of {table}",
    "display the total {table}"
]


AVG_PATTERNS = [

    "show average {field}",
    "find the average {field}",
    "what is the average {field}",
    "display average {field}",
    "return average {field}",
    "give me average {field}",
    "calculate average {field}"
]


MAX_PATTERNS = [

    "show maximum {field}",
    "find highest {field}",
    "what is the maximum {field}",
    "display highest {field}",
    "return maximum {field}",
    "give me highest {field}",
    "calculate maximum {field}"
]


MIN_PATTERNS = [

    "show minimum {field}",
    "find lowest {field}",
    "what is the minimum {field}",
    "display lowest {field}",
    "return minimum {field}",
    "give me lowest {field}",
    "calculate minimum {field}"
]


SUM_PATTERNS = [

    "show total {field}",
    "calculate total {field}",
    "find sum of {field}",
    "what is the total {field}",
    "return sum of {field}",
    "display total {field}",
    "give me sum of {field}"
]

# ==========================================================
# Multi Condition Templates
# ==========================================================

MULTI_CONDITION_PATTERNS = [

    "{verb} devices that are {status} with battery above {battery}",

    "{verb} {status} devices having battery greater than {battery}",

    "find devices that are {status} and battery above {battery}",

    "show devices with status {status} and battery over {battery}",

    "list {status} devices with battery higher than {battery}",

    "{verb} sensors in room {room} with humidity above {humidity}",

    "find sensors in room {room} having humidity greater than {humidity}",

    "show sensors located in room {room} with humidity above {humidity}",

    "list sensors from room {room} where humidity exceeds {humidity}"
]

# ==========================================================
# Sorting Templates
# ==========================================================

SORT_DESC_PATTERNS = [

    "show top {limit} {table} with highest {field}",

    "list top {limit} {table} by {field}",

    "find {table} with highest {field}",

    "show {table} ordered by {field} descending",

    "display {table} sorted by {field} descending",

    "return {table} with maximum {field}",

    "show {table} ranked by {field}"
]


SORT_ASC_PATTERNS = [

    "show top {limit} {table} with lowest {field}",

    "list top {limit} {table} by lowest {field}",

    "find {table} with lowest {field}",

    "show {table} ordered by {field} ascending",

    "display {table} sorted by {field} ascending",

    "return {table} with minimum {field}",

    "show {table} ranked by lowest {field}"
]

# ==========================================================
# Advanced Multi Condition Templates
# ==========================================================

ADVANCED_DEVICE_PATTERNS = [

    "{verb} {status} devices with battery above {battery} in {location}",

    "find {status} devices located in {location} with battery greater than {battery}",

    "show devices that are {status} and have battery above {battery} in {location}",

    "list {status} devices in {location} with battery higher than {battery}",

    "return devices with status {status}, battery above {battery}, located in {location}"
]


ADVANCED_SENSOR_PATTERNS = [

    "{verb} sensors in room {room} with humidity above {humidity} and temperature below {temperature}",

    "find sensors located in room {room} where humidity exceeds {humidity} and temperature is below {temperature}",

    "show sensors from room {room} having humidity greater than {humidity} and temperature less than {temperature}",

    "list sensors in room {room} with humidity above {humidity} and temperature under {temperature}",

    "return sensors in room {room} where humidity > {humidity} and temperature < {temperature}"
]