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

# ==========================================================
# Time Query Templates
# ==========================================================

LAST_30_MIN_PATTERNS = [

    "show devices connected in the last 30 minutes",
    "find devices active during the past 30 minutes",
    "list devices seen in the last half hour",
    "show recently connected devices from the last 30 minutes",
    "return devices connected within 30 minutes"
]

LAST_HOUR_PATTERNS = [

    "show devices connected in the last hour",
    "find devices seen in the past hour",
    "list devices active during the last hour",
    "show recently connected devices",
    "return devices connected within the last hour",
    "which devices were online in the last hour",
    "display devices active over the past hour",
    "retrieve devices connected during the previous hour",
    "show all devices connected recently",
    "list recently active devices"
]

LAST_6_HOURS_PATTERNS = [

    "show devices connected in the last 6 hours",
    "find devices active during the past 6 hours",
    "list devices seen in the last 6 hours",
    "show devices online in the previous 6 hours",
    "retrieve devices connected over the last 6 hours"
]

LAST_DAY_PATTERNS = [

    "show devices connected in the last 24 hours",
    "find devices active in the past day",
    "list devices seen during the last day",
    "return devices connected within 24 hours",
    "show devices connected recently",
    "which devices were online yesterday",
    "display devices active over the last day",
    "retrieve devices connected during the previous day",
    "show all devices connected in the past day",
    "list recently active devices from the last day"
]

LAST_WEEK_PATTERNS = [

    "show devices connected this week",
    "find devices active this week",
    "list devices seen during the last week",
    "return devices connected in the past week",
    "show devices connected within 7 days",
    "which devices were online this week",
    "display devices active during the previous week",
    "retrieve devices connected over the last 7 days",
    "show all devices connected recently this week",
    "list devices active during the week"
]

LAST_MONTH_PATTERNS = [

    "show devices connected in the last 30 days",
    "find devices active during the last month",
    "list devices seen in the previous month",
    "return devices connected over the last 30 days",
    "show devices active this month"
]

TODAY_PATTERNS = [

    "show devices connected today",
    "find devices active today",
    "list today's connected devices",
    "return devices seen today",
    "show all devices connected today",
    "which devices were online today",
    "display today's active devices",
    "retrieve devices connected during today",
    "show devices seen since morning",
    "list devices active today"
]

# ==========================================================
# BETWEEN Templates
# ==========================================================

BETWEEN_PATTERNS = [

    "show {table} with {field} between {lower} and {upper}",

    "find {table} where {field} is between {lower} and {upper}",

    "list {table} having {field} between {lower} and {upper}",

    "return {table} with {field} ranging from {lower} to {upper}",

    "show all {table} whose {field} lies between {lower} and {upper}",

    "identify {table} with {field} between {lower} and {upper}",

    "which {table} have {field} between {lower} and {upper}",

    "give me {table} where {field} is between {lower} and {upper}"
]

# ==========================================================
# GROUP BY Templates
# ==========================================================

GROUP_COUNT_PATTERNS = [

    "count {table} by {field}",

    "show count of {table} grouped by {field}",

    "display number of {table} per {field}",

    "list total {table} by {field}",

    "group {table} by {field} and count them",

    "how many {table} exist for each {field}",

    "show {field} wise count of {table}",

    "count {table} for every {field}",

    "display {table} counts by {field}",

    "return grouped count of {table} by {field}"
]

GROUP_AVG_PATTERNS = [

    "show average {value_field} by {group_field}",

    "display average {value_field} grouped by {group_field}",

    "find average {value_field} for each {group_field}",

    "list average {value_field} per {group_field}",

    "group by {group_field} and calculate average {value_field}",

    "show mean {value_field} by {group_field}",

    "display {group_field} wise average {value_field}",

    "find average {value_field} across each {group_field}",

    "return average {value_field} grouped by {group_field}",

    "calculate average {value_field} for every {group_field}"
]


# ==========================================================
# HAVING Templates
# ==========================================================

HAVING_PATTERNS = [

    "show {group_field} having more than {threshold} records",

    "find {group_field} with count greater than {threshold}",

    "list {group_field} containing over {threshold} entries",

    "display groups where count exceeds {threshold}",

    "show groups with more than {threshold} records",

    "which {group_field} have over {threshold} devices",

    "return {group_field} whose count is above {threshold}",

    "find groups having at least {threshold} entries",

    "display {group_field} with more than {threshold} records",

    "list groups where count is greater than {threshold}",

    "show all {group_field} exceeding {threshold} records",

    "identify groups with over {threshold} members",

    "retrieve {group_field} having count above {threshold}",

    "which groups contain more than {threshold} rows",

    "return grouped results with count greater than {threshold}"
]

HAVING_AVG_PATTERNS = [

    "show {group_field} where average {field} exceeds {threshold}",

    "find {group_field} having average {field} above {threshold}",

    "list groups whose average {field} is greater than {threshold}",

    "display {group_field} with mean {field} above {threshold}",

    "return {group_field} where average {field} exceeds {threshold}",

    "identify groups with average {field} higher than {threshold}",

    "show groups whose average {field} is above {threshold}",

    "find grouped results where average {field} exceeds {threshold}",

    "list {group_field} having mean {field} greater than {threshold}",

    "retrieve groups whose average {field} is above {threshold}"
]