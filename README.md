# Citi Bike NYC Expansion Strategy Dashboard

An end-to-end data analytics project identifying optimal locations for Citi Bike network expansion in New York City, combining trip data analysis with weather correlation and interactive visualizations.

## Live Dashboard

🚀 **[View Interactive Dashboard](https://citibikeusa.streamlit.app/)**

## Overview

This project analyzes 786,983 Citi Bike trips from 2022 alongside NOAA weather data to answer a critical business question: **where and when should Citi Bike expand its network to resolve persistent bike shortages?**

### Key Findings

- Ridership is **3-4x higher in summer than winter**, indicating seasonal fleet management is essential
- The **top 20 stations** (waterfront, transit hubs, Lower Manhattan) account for a disproportionate share of all trips
- **Queens and Upper Manhattan** represent the largest underserved markets for expansion
- Strong temperature-ridership correlation means capacity planning can be data-driven

## Live Dashboard

🚀 **[View on Streamlit](https://citibikeusa.streamlit.app/)**

## Repository Structure

```
citibike-expansion-dashboard/
├── notebooks/
│   ├── 01_data_collection.ipynb          # API integration with NOAA + Citi Bike data
│   ├── 02_matplotlib_visualizations.ipynb # Static charts: bar, dual-axis, histogram
│   ├── 03_seaborn_visualizations.ipynb    # Statistical charts: boxplot, FacetGrid
│   ├── 04_geospatial_visualization.ipynb  # Interactive folium map of trip routes
│   ├── 05_plotly_charts.ipynb             # Interactive plotly charts for dashboard
│   ├── 06_data_preparation.ipynb          # Reduced dataset creation for deployment
│   └── 07_visualization_enhanced.ipynb    # Additional exploratory visualizations
├── outputs/
│   ├── reduced_data_to_plot.csv           # Sampled dataset for dashboard (<25MB)
│   ├── top20.csv                          # Top 20 stations aggregation
│   ├── daily_data.csv                     # Daily trip + weather aggregation
│   ├── top20_stations.html                # Interactive bar chart (GitHub viewable)
│   └── rides_vs_temp.html                 # Interactive line chart (GitHub viewable)
├── st_dashboard.py                        # Exercise 2.6: Initial dashboard
├── st_dashboard_Part_2.py                 # Exercise 2.7: Final multi-page dashboard
├── requirements.txt                       # Python dependencies for deployment
├── .gitignore                             # Excludes large data files and checkpoints
└── README.md
```

## Dashboard Pages

| Page | Description |
|------|-------------|
| **Introduction** | Problem statement and dashboard navigation guide |
| **Weather & Bike Usage** | Dual-axis chart showing temperature-ridership correlation |
| **Most Popular Stations** | Top 20 stations with seasonal filter and trip count metric |
| **Geographic Distribution** | Interactive map of high-volume routes and network gaps |
| **Recommendations** | Strategic actions for fleet optimization and expansion |

## Technical Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| pandas | Data manipulation and aggregation |
| matplotlib | Static visualizations |
| seaborn | Statistical visualizations |
| folium | Geospatial interactive map |
| plotly | Interactive dashboard charts |
| streamlit | Dashboard web application |
| requests | NOAA API integration |

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/pm-ssingh/citibike-expansion-dashboard.git
cd citibike-expansion-dashboard
```

### 2. Create virtual environment

```bash
python -m venv citibike_env
source citibike_env/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add source data

- Download 12 monthly CSV files from [Citi Bike System Data](https://citibikenyc.com/system-data)
- Place in a `data/` folder in the project root
- Add your [NOAA API token](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) to `notebooks/01_data_collection.ipynb`

### 5. Run notebooks in order

```bash
jupyter lab
```

Execute notebooks `01` through `07` sequentially.

### 6. Run the dashboard locally

```bash
streamlit run st_dashboard_Part_2.py
```

## Data Sources

| Dataset | Provider | Coverage |
|---------|----------|----------|
| Trip data | [Citi Bike System Data](https://citibikenyc.com/system-data) | Jan-Dec 2022, ~787K trips |
| Weather data | [NOAA CDO API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | Daily avg temp, LaGuardia station |

## Methodology

### Data Pipeline
1. **Collection**: 12 monthly CSV files concatenated via `pd.concat()` + NOAA REST API
2. **Merging**: Left join on date field combining trips with daily temperatures
3. **Aggregation**: Station-level counts via `groupby().size()`, daily totals via `groupby().agg()`
4. **Sampling**: 8% random sample (`np.random.seed(32)`) for deployment under 25MB

### Visualization Approach
- **Static**: matplotlib and seaborn for exploratory analysis
- **Geospatial**: folium with MarkerCluster and PolyLine layers for route mapping
- **Interactive**: plotly with custom hover templates and dual-axis support
- **Dashboard**: Streamlit multi-page app with seasonal filters and KPI metrics

## Recommendations Summary

1. **Immediate**: Increase docking capacity 30-50% at top 20 stations
2. **Seasonal**: Reduce fleet 40-50% in winter (Nov-Apr), maximize in summer
3. **Redistribution**: Morning restocking at commuter hubs, evening at residential areas
4. **Medium-term**: Fill waterfront corridor gaps along Hudson River Greenway
5. **Long-term**: Expand into Queens (Phase 1: Astoria, Long Island City)

## Author

**Saurabh Singh**
GitHub: [@pm-ssingh](https://github.com/pm-ssingh)
Project: CareerFoundry Data Visualization with Python - Achievement 2

## License

Educational project developed as part of the CareerFoundry Data Visualization specialization.
