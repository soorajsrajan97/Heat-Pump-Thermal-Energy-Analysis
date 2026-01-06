# Heat Pump & Thermal Energy System Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This repository contains three Python projects demonstrating engineering-oriented modeling and analysis of heat pump systems, thermal load forecasting, and thermal storage operation. These projects focus on practical, interpretable simulations for energy system applications.

## Projects Overview

### 1. Heat Pump Modeling
**Goal:** Simulate steady-state and simplified dynamic behavior of a vapor-compression heat pump.

**Highlights:**
- Steady-state cycle simulation using CoolProp to calculate COP using CoolProp (R134a)
- Simplified first-order thermal response to step changes in load
- Visualized p-h diagrams and transient temperature response
- Achieved COP: 6.59 (5°C evaporator, 40°C condenser)

**Outputs:**
- `heat_pump_steady_dynamic.ipynb` – file
- `hp_cycle.png` – heat pump cycle diagram
- `hp_dynamic.png` – simplified dynamic response

### 2. Thermal Load Forecasting
**Goal:** Predict short-term thermal demand using statistical and regression methods.

**Dataset:** 8,760 hours of synthetic thermal load data with seasonal temperature variations and stochastic noise.

**Highlights:**
- Rolling average and weekly average as baseline forecasts
- Linear regression using ambient temperature and hour-of-day as predictors
- Performance evaluation: RMSE of 37.8 kW (rolling avg) and 24.9 kW (linear regression)
- Visualization against actual demand

**Output:**
- `thermal_load_forecast.ipynb` – file
- `thermal_load_forecast.png` – forecast comparison plot

### 3. Thermal Storage Modeling
**Goal:** Model thermal storage behavior and evaluate simple charge/discharge strategies.

**Highlights:**
- Lumped thermal storage model with temperature limits and heat loss
- Rule-based charging and discharging strategies based on electricity price signals
- Visualized storage temperature and power flows over a 24-hour horizon

**Output:**
- `thermal_storage_control.ipynb` – file
- `thermal_storage_model.png` – storage operation visualization

## Technologies

- **Python 3.x** – Core programming language
- **CoolProp** – Thermodynamic property calculations
- **Pandas/NumPy** – Data manipulation and numerical computing
- **Matplotlib** – Data visualization
- **scikit-learn** – Machine learning for forecasting

## Data Generation

The `data_generation.py` script creates realistic synthetic data for thermal analysis:

**Features:**
- **Seasonal temperature patterns**: Sinusoidal variation with added noise
- **Time-dependent heat demand**: Peak demand during cold nights
- **Temperature correlation**: Demand increases ~2 kW per °C drop
- **Stochastic variation**: Random noise for realistic behavior

**Output:** `hourly_heat_demand.csv` with columns:
- `timestamp`: Hourly datetime index
- `temp_C`: Ambient temperature (°C)
- `hour`: Hour of day (0-23)
- `demand_kW`: Thermal load demand (kW)

## Repository Structure

```
├── data_generation.py                 # Synthetic data generation
├── hourly_heat_demand.csv             # Generated thermal load data
├── heat_pump_steady_dynamic.ipynb     # Heat pump cycle modeling
├── thermal_load_forecast.ipynb        # Load forecasting analysis
├── thermal_storage_control.ipynb      # Storage operation simulation
├── .gitignore                         # Python gitignore
├── LICENSE                            # MIT License
└── README.md
```

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/soorajsrajan97/Heat-Pump-Thermal-Energy-Analysis.git
cd Heat-Pump-Thermal-Energy-Analysis
```

### 2. Install Dependencies
```bash
pip install numpy pandas matplotlib scikit-learn CoolProp jupyter
```

### 3. Generate Synthetic Data (Optional)
The repository includes pre-generated data, but you can regenerate it:
```bash
python data_generation.py
```
This creates `hourly_heat_demand.csv` with:
- 8,760 hours (full year) of synthetic thermal load data
- Ambient temperature with seasonal variation
- Heat demand correlated with temperature and time of day

### 4. Run Notebooks
```bash
jupyter notebook
```
Open any `.ipynb` file to explore the analysis.

## Skills Demonstrated

✅ **Synthetic Data Generation**: Creating physics-informed datasets  
✅ **Thermodynamic Modeling**: Heat pump cycle simulation with CoolProp  
✅ **Time Series Forecasting**: Statistical and ML-based demand prediction  
✅ **Control Systems**: Rule-based thermal storage operation  
✅ **Data Visualization**: Clear presentation of engineering results  
✅ **Reproducible Research**: Structured code with documentation

## Learning Outcomes

- Modeling steady-state and transient heat pump performance
- Forecasting thermal loads using simple baselines and regression techniques
- Simulating thermal storage operation with rule-based control strategies
- Visualizing and interpreting energy system behavior for engineering analysis

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaboration opportunities, feel free to reach out via [GitHub](https://github.com/soorajsrajan97).
