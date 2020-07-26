"""Every news release from Los Angeles County Public Health is identified by a
    unique PRID. The maps associate a date and the corresponding COVID-19
    daily news release.
"""

DAILY_STATS = {
    (2020, 3, 30): 2289,
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
    (2020, 4, 29): 2349,
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
    (2020, 5, 27): 2406,
    (2020, 5, 28): 2408,
    (2020, 5, 29): 2409,
    (2020, 5, 30): 2411,
    (2020, 5, 31): 2412,
    (2020, 6, 1): 2413,
    (2020, 6, 2): 2419,
    (2020, 6, 3): 2422,
    (2020, 6, 4): 2423,
    (2020, 6, 5): 2426,
    (2020, 6, 6): 2428,
    (2020, 6, 7): 2429,
    (2020, 6, 8): 2430,
    (2020, 6, 9): 2432,
    (2020, 6, 10): 2436,
    (2020, 6, 11): 2438,
    (2020, 6, 12): 2440,
    (2020, 6, 13): 2442,
    (2020, 6, 14): 2443,
    (2020, 6, 15): 2445,
    (2020, 6, 16): 2447,
    (2020, 6, 17): 2449,
    (2020, 6, 18): 2451,
    (2020, 6, 19): 2452,
    (2020, 6, 20): 2455,
    (2020, 6, 21): 2456,
    (2020, 6, 22): 2458,
    (2020, 6, 23): 2462,
    (2020, 6, 24): 2465,
    (2020, 6, 25): 2467,
    (2020, 6, 26): 2469,
    (2020, 6, 27): 2470,
    (2020, 6, 28): 2471,
    (2020, 6, 29): 2472,
    (2020, 6, 30): 2476,
    (2020, 7, 1): 2477,
    (2020, 7, 2): 2480,
    (2020, 7, 6): 2485,
    (2020, 7, 7): 2487,
    (2020, 7, 8): 2489,
    (2020, 7, 9): 2492,
    (2020, 7, 10): 2496,
    (2020, 7, 11): 2500,
    (2020, 7, 12): 2501,
    (2020, 7, 13): 2503,
    (2020, 7, 14): 2506,
    (2020, 7, 15): 2508,
    (2020, 7, 16): 2510,
    (2020, 7, 17): 2514,
    (2020, 7, 18): 2516,
    (2020, 7, 19): 2518,
    (2020, 7, 20): 2521,
    (2020, 7, 21): 2522,
    (2020, 7, 22): 2526,
    (2020, 7, 23): 2527,
    (2020, 7, 24): 2529,
    (2020, 7, 25): 2531,
    (2020, 7, 26): 2533,
}
