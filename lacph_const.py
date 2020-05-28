from datetime import date
import re

LACPH_PR_URL_BASE = 'http://www.publichealth.lacounty.gov/phcommon/public/media/mediapubhpdetail.cfm?prid='

DATE = re.compile('[A-Z][a-z]+ \d{2}, 20\d{2}')

BY_DEPT_COUNT = re.compile('(Los Angeles County \(excl\. LB and Pas\)|Long Beach|Pasadena)[\s-]*(\d+)')

HEADER_CASES_COUNT = re.compile('Laboratory Confirmed Cases -- ([\d,]+) Total Cases')
HEADER_AGE_GROUP = re.compile('^Age Group')
HEADER_DEATHS = re.compile('Deaths\s+([\d,]+)')
HEADER_HOSPITAL = re.compile('^Hospitalization')
HEADER_CITIES = re.compile('CITY / COMMUNITY\** \(Rate\**\)')

AGE_RANGE = re.compile('(\d+) to (\d+)\s*--\s*(\d+)')
AGE_OVER = re.compile('over (\d+)\s*--\s*(\d+)')
UNDER_INVESTIGATION = re.compile('Under Investigation')
NO_COUNT = re.compile('--')

HOSPITAL_STATUS = re.compile('([A-Z][A-Za-z() ]+[)a-z])\s*(\d+)')

AREA_CITY = re.compile('City of +([A-Z][A-Za-z ]+[a-z]\**)\s+([0-9]+|--)\s+\(\s+([0-9\.]+|--)\s\)')
AREA_LA = re.compile('Los Angeles - +([A-Z][A-Za-z/\- ]+[a-z]\**)\s+([0-9]+|--)\s+\(\s+([0-9\.]+|--)\s\)')
AREA_UNINCORPORATED = re.compile('Unincorporated - +([A-Z][A-Za-z/\- ]+[a-z]\**)\s+([0-9]+|--)\s+\(\s+([0-9\.]+|--)\s\)')

TOTAL = 'Total'
CITY = 'City'
LOS_ANGELES = 'Los Angeles'
UNINCORPORATED = 'Unincorporated'

START_GENDER = date(2020, 4, 4)
START_RACE_CASES = date(2020, 4, 7)
START_RACE_DEATHS = date(2020, 4, 7)

# Formating Changes
START_FORMAT_HOSPITAL_NESTED = date(2020, 4, 4)
FORMAT_AGE_NESTED = date(2020, 4, 4)

DAILY_STATS_PR = {(2020, 3, 30): 2289,
                  (2020, 3, 31): 2290,
                  (2020, 4, 1): 2291,
                  (2020, 4, 2): 2292,
                  (2020, 4, 3): 2294,
                  (2020, 4, 4): 2297,
                  (2020, 4, 5): 2298,
                  (2020, 4, 6): 2300,
                  (2020, 4, 7): 2302,
                  (2020, 4, 8): 2304,
                  (2020, 4, 9): 2307,
                  (2020, 4, 10): 2309,
                  (2020, 4, 11): 2311,
                  (2020, 4, 12): 2312,
                  (2020, 4, 13): 2314,
                  (2020, 4, 14): 2317,
                  (2020, 4, 15): 2319,
                  (2020, 4, 16): 2321,
                  (2020, 4, 17): 2323,
                  (2020, 4, 18): 2325,
                  (2020, 4, 19): 2326,
                  (2020, 4, 20): 2329,
                  (2020, 4, 21): 2331,
                  (2020, 4, 22): 2333,
                  (2020, 4, 23): 2336,
                  (2020, 4, 24): 2337,
                  (2020, 4, 25): 2341,
                  (2020, 4, 26): 2343,
                  (2020, 4, 27): 2345,
                  (2020, 4, 28): 2347,
                  (2020, 4, 29): 2351,
                  (2020, 4, 30): 2352,
                  (2020, 5, 1): 2353,
                  (2020, 5, 2): 2355,
                  (2020, 5, 3): 2356,
                  (2020, 5, 4): 2357,
                  (2020, 5, 5): 2359,
                  (2020, 5, 6): 2361,
                  (2020, 5, 7): 2362,
                  (2020, 5, 8): 2365,
                  (2020, 5, 9): 2367,
                  (2020, 5, 10): 2369,
                  (2020, 5, 11): 2370,
                  (2020, 5, 12): 2373,
                  (2020, 5, 13): 2375,
                  (2020, 5, 14): 2377,
                  (2020, 5, 15): 2380,
                  (2020, 5, 16): 2381,
                  (2020, 5, 17): 2382,
                  (2020, 5, 18): 2384,
                  (2020, 5, 19): 2386,
                  (2020, 5, 20): 2389,
                  (2020, 5, 21): 2391,
                  (2020, 5, 22): 2393,
                  (2020, 5, 23): 2394,
                  (2020, 5, 24): 2399,
                  (2020, 5, 25): 2400,
                  (2020, 5, 26): 2403,
                  (2020, 5, 27): 2406
}
