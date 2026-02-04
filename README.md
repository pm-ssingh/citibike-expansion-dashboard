# Citi Bike NYC Expansion Dashboard

Strategic data analytics project for optimizing Citi Bike's network expansion through data-driven station placement recommendations.

## Overview

This analysis leverages 2022 Citi Bike trip data combined with meteorological information to identify optimal locations for new bike-sharing stations in New York City. The project employs statistical analysis and geospatial techniques to maximize infrastructure ROI and improve service coverage.

### Problem Statement

Current bike shortages at high-traffic stations indicate insufficient supply relative to demand. This project addresses the network expansion challenge by quantifying usage patterns, identifying underserved areas, and providing actionable recommendations for strategic station placement.

## Research Objectives

The analysis addresses four key questions:

1. **Station Demand Analysis**: Identify high-traffic stations experiencing capacity constraints
2. **Weather Impact Assessment**: Quantify seasonal and weather-related effects on ridership patterns
3. **Route Optimization**: Map frequently traveled corridors to identify network gaps
4. **Coverage Analysis**: Evaluate geographic distribution and identify underserved areas

## Repository Structure

```
citibike-expansion-dashboard/
├── citibike_data_collection.ipynb    # Primary analysis notebook
├── data/                              # Source data files (excluded from VCS)
│   ├── JC-202201-citibike-tripdata.csv
│   ├── JC-202202-citibike-tripdata.csv
│   └── [10 additional monthly files]
├── outputs/                           # Generated datasets (excluded from VCS)
│   ├── merged_citibike_weather_2022.csv
│   └── weather_data_2022.csv
├── .gitignore                        # Version control exclusions
└── README.md                         # Project documentation
```

## Technical Stack

- **Python 3.13** - Core programming environment
- **pandas 3.0.0** - Data manipulation and analysis
- **requests 2.32.5** - HTTP client for API integration
- **json** - JSON parsing and serialization
- **datetime** - Temporal data handling
- **JupyterLab** - Interactive development environment

## Data Sources

### Primary Dataset
- **Provider**: Citi Bike System Data
- **Temporal Coverage**: January 2022 - December 2022
- **Records**: Approximately 786,983 trip records
- **Geographic Scope**: Jersey City, NJ
- **Format**: 12 monthly CSV files
- **Access**: [Citi Bike System Data Portal](https://citibikenyc.com/system-data)

### Supplementary Dataset
- **Provider**: NOAA Climate Data Online (CDO) API
- **Station**: LaGuardia Airport Weather Station (ID: GHCND:USW00014732)
- **Temporal Coverage**: January 1, 2022 - December 31, 2022
- **Metrics**: Daily average temperature (TAVG)
- **Access**: [NOAA CDO Web Services](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Git version control
- NOAA API authentication token

### Installation Steps

1. Clone the repository
   ```bash
   git clone https://github.com/pm-ssingh/citibike-expansion-dashboard.git
   cd citibike-expansion-dashboard
   ```

2. Configure Python virtual environment
   ```bash
   python -m venv citibike_env
   source citibike_env/bin/activate  # Unix/MacOS
   citibike_env\Scripts\activate     # Windows
   ```

3. Install dependencies
   ```bash
   pip install pandas requests jupyterlab
   ```

4. Acquire source data
   - Download 12 monthly CSV files from Citi Bike System Data portal
   - Create `data/` directory in project root
   - Place all CSV files in `data/` directory

5. Configure API authentication
   - Request authentication token from NOAA CDO Web Services
   - Open `citibike_data_collection.ipynb`
   - Update token variable with your credentials

### Execution

1. Launch Jupyter Lab environment
   ```bash
   jupyter lab
   ```

2. Execute analysis notebook
   - Open `citibike_data_collection.ipynb`
   - Run cells sequentially from top to bottom

3. Output artifacts
   - `merged_citibike_weather_2022.csv` - Integrated trip and weather dataset
   - `weather_data_2022.csv` - Daily temperature records

## Methodology

### Data Ingestion

The data collection pipeline implements efficient file handling through:
- List comprehension with `os.listdir()` for dynamic file discovery
- Generator expressions with `pd.concat()` for memory-efficient batch processing
- RESTful API integration with NOAA CDO for meteorological data retrieval

### Data Transformation

Processing workflow includes:
1. **Weather Data Extraction**: Parse JSON API response to extract temporal and temperature fields
2. **Date Normalization**: Convert ISO 8601 timestamps to date objects for join operations
3. **Unit Conversion**: Transform NOAA temperature values (stored as tenths of Celsius) to standard Celsius
4. **Dataset Integration**: Perform left join on date field with merge quality validation

### Quality Assurance

The pipeline implements multiple validation checkpoints:
- Merge indicator analysis confirms 100% join success rate
- Head/tail inspection validates data integrity across time series
- Shape validation ensures complete record processing
- Statistical summary confirms data distribution expectations

## Implementation Details

### Efficiency Considerations

- **Generator Pattern**: Reduces memory footprint by processing files sequentially rather than loading all into memory
- **List Comprehension**: Provides concise, optimized iteration for data extraction
- **Batch Processing**: Consolidates 12 monthly files into single dataset for simplified analysis

### API Integration

- **Authentication**: Token-based authentication via HTTP headers
- **Rate Limiting**: Respects NOAA API constraints (1000 record limit per request)
- **Error Handling**: Validates API response status before data processing

## Results and Insights

Analysis outcomes and recommendations will be documented following completion of visualization phase.

## Future Work

1. Develop interactive visualization dashboard
2. Implement machine learning models for demand forecasting
3. Conduct spatial analysis for optimal station placement
4. Generate executive summary with actionable recommendations

## Author

**Saurabh Singh**  
GitHub: [@pm-ssingh](https://github.com/pm-ssingh)

**Academic Context**: CareerFoundry Data Visualization Specialization  
**Course**: Achievement 2, Exercise 2.2

## License

This project is developed for educational purposes as part of the CareerFoundry Data Visualization with Python specialization program.

## Acknowledgments

- Citi Bike for providing open-access trip data
- National Oceanic and Atmospheric Administration (NOAA) for meteorological data access
- CareerFoundry for curriculum design and project guidance

## Contact

For inquiries regarding this analysis, please submit an issue through the GitHub repository issue tracker.

---

**Last Updated**: February 2026  
**Version**: 1.0.0  
**Status**: Active Development
