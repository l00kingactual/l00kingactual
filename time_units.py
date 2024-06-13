time_units = {
    "Year": {"Symbol": "yr", "Time in Seconds (s)": 31536000, "Scientific Notation": "3.15 × 10^7"},
    "Month (average)": {"Symbol": "mo", "Time in Seconds (s)": 2592000, "Scientific Notation": "2.59 × 10^6"},
    "Day": {"Symbol": "d", "Time in Seconds (s)": 86400, "Scientific Notation": "8.64 × 10^4"},
    "Hour": {"Symbol": "h", "Time in Seconds (s)": 3600, "Scientific Notation": "3.6 × 10^3"},
    "Minute": {"Symbol": "min", "Time in Seconds (s)": 60, "Scientific Notation": "6.0 × 10^1"},
    "Second": {"Symbol": "s", "Time in Seconds (s)": 1, "Scientific Notation": "1"},
    "Millisecond": {"Symbol": "ms", "Time in Seconds (s)": 0.001, "Scientific Notation": "1 × 10^-3"},
    "Microsecond": {"Symbol": "μs", "Time in Seconds (s)": 0.000001, "Scientific Notation": "1 × 10^-6"},
    "Nanosecond": {"Symbol": "ns", "Time in Seconds (s)": 0.000000001, "Scientific Notation": "1 × 10^-9"},
    "Picosecond": {"Symbol": "ps", "Time in Seconds (s)": 0.000000000001, "Scientific Notation": "1 × 10^-12"},
    "Femtosecond": {"Symbol": "fs", "Time in Seconds (s)": 0.000000000000001, "Scientific Notation": "1 × 10^-15"},
    "Attosecond": {"Symbol": "as", "Time in Seconds (s)": 0.000000000000000001, "Scientific Notation": "1 × 10^-18"},
    "Zeptosecond": {"Symbol": "zs", "Time in Seconds (s)": 0.000000000000000000001, "Scientific Notation": "1 × 10^-21"},
    "Yoctosecond": {"Symbol": "ys", "Time in Seconds (s)": 0.000000000000000000000001, "Scientific Notation": "1 × 10^-24"},
    "Planck Time": {"Symbol": "-", "Time in Seconds (s)": 5.39121e-44, "Scientific Notation": "5.39121 × 10^-44"},
    "10^-50 Arcseconds": {"Symbol": "-", "Time in Seconds (s)": 1.057e-58, "Scientific Notation": "1.057 × 10^-58"},
    "10^-60 Arcseconds": {"Symbol": "-", "Time in Seconds (s)": 1.057e-68, "Scientific Notation": "1.057 × 10^-68"}
}

# Accessing the values for a specific unit of time
print(time_units["Year"]["Symbol"])  # Output: "yr"
print(time_units["Second"]["Time in Seconds (s)"])  # Output: 1
