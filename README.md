# Heat Pump & Thermal Energy System Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This repository contains four small Python projects on heat pump systems, thermal load forecasting and thermal storage operation. They are learning and portfolio projects: simple, interpretable models, not validated engineering tools. Assumptions and limitations are listed for each project.

## Projects Overview

### 1. Heat Pump Modeling (data sheet based)
**Goal:** Model a brine/water heat pump from a manufacturer data sheet and simulate a house heated by it.

**Unit:** Viessmann Vitocal 200-G (BWC 201.B08), refrigerant R410A. Data sheet values at B0/W35: 7.5 kW heating capacity, COP 4.6.

**Highlights:**
- Steady-state refrigeration cycle with CoolProp: state points, heating COP `(h2 - h3)/(h2 - h1)`, compressor power
- Superheat, subcooling and approach temperatures included; the compressor efficiency is chosen so the model COP matches the data sheet (an *effective* value, not an independent validation)
- p-h diagram with saturation dome
- Thermal response of a house with an on/off thermostat (stable implicit time stepping): room temperature, duty cycle and electricity use over 48 hours

**Outputs:**
- `heat_pump_steady_dynamic.ipynb`
- `hp_cycle.png` – p-h diagram
- `thermal_response.png` – house temperature and heat pump output

**Source:** Viessmann, *Technische Daten, Sole/Wasser-Wärmepumpen*, p. 44/45 [add full title and issue date]. The data sheet itself is not included in this repository.

### 2. Heat Pump Sizing Check
**Goal:** Compare a building's heat load with data sheet capacities and classify each unit as too small, well sized or too large.

**Highlights:**
- Input: heated area, building type (specific heat load in W/m²), optional extra load
- Data sheet table: Vitocal 200-G capacities at B0/W35 (replaceable with another product's values)
- Bar chart of unit capacity against the heat load, coloured by verdict

**Assumptions:** the specific loads (W/m²) and the oversizing limit (1.3 × load) are rules of thumb. Nominal data sheet capacity is used, so a ratio just above 1 is optimistic on the coldest day.

**Output:**
- `heat_pump_sizing_check.ipynb`

### 3. Thermal Load Forecasting
**Goal:** Predict short-term thermal demand using statistical and regression methods.

**Dataset:** 8,760 hours of synthetic thermal load data with seasonal temperature variations and stochastic noise.

**Highlights:**
- Rolling average and weekly average as baseline forecasts
- Linear regression using ambient temperature and hour-of-day as predictors
- Performance evaluation: RMSE of 37.8 kW (rolling avg) and 24.9 kW (linear regression)
- Visualization against actual demand

**Note:** the data are synthetic, so these errors say how the methods compare on this dataset, not how they would perform on real measurements.

**Output:**
- `thermal_load_forecast.ipynb`
- `thermal_load_forecast.png`

### 4. Thermal Storage Modeling
**Goal:** Model thermal storage behavior and evaluate simple charge/discharge strategies.

**Highlights:**
- Lumped thermal storage model with temperature limits and heat loss
- Rule-based charging and discharging strategies based on electricity price signals
- Storage temperature and power flows over a 24-hour horizon

**Output:**
- `thermal_storage_control.ipynb`
- `thermal_storage_model.png`

## Technologies

- **Python 3.x**
- **CoolProp** – thermodynamic properties
- **Pandas / NumPy** – data handling and numerical computing
- **Matplotlib** – visualization
- **scikit-learn** – regression for forecasting

## Data Generation

`data_generation.py` creates simple synthetic data for the load forecasting project:
- Seasonal temperature: sinusoidal variation plus noise
- Time-dependent demand: higher during cold nights
- Temperature correlation: demand rises about 2 kW per °C drop
- Random noise for variability

**Output:** `hourly_heat_demand.csv` with columns `timestamp`, `temp_C`, `hour`, `demand_kW`.

## Repository Structure

```
├── data_generation.py                 # Synthetic data generation
├── hourly_heat_demand.csv             # Generated thermal load data
├── heat_pump_steady_dynamic.ipynb     # Heat pump cycle, p-h diagram, house thermal response
├── heat_pump_sizing_check.ipynb       # Sizing check against data sheet capacities
├── thermal_load_forecast.ipynb        # Load forecasting
├── thermal_storage_control.ipynb      # Storage operation simulation
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

```bash
git clone https://github.com/soorajsrajan97/Heat-Pump-Thermal-Energy-Analysis.git
cd Heat-Pump-Thermal-Energy-Analysis
pip install numpy pandas matplotlib scikit-learn CoolProp jupyter
python data_generation.py      # optional: regenerate the synthetic data
jupyter notebook
```

Open any `.ipynb` file and run all cells.

## Limitations

- **Heat pump model:** full load at one operating point (B0/W35); losses are lumped into one effective efficiency; approach temperatures, superheat, subcooling, house heat loss (UA) and thermal mass are assumptions; COP is constant in the thermal simulation; no part load or defrost.
- **Sizing check:** rule-of-thumb heat loads and thresholds; no hot water, ventilation or emitter temperature effects.
- **Forecasting and storage:** based on synthetic data and simple rules.

## Next Steps

- Add a PVT collector model as the heat source (ISO 9806 coefficients) and hourly weather data
- Add more data sheet test points (B0/W45, B-5/W35) for a multi-point calibration
- Fit the COP map with regression or symbolic regression

## Development Note

[Add your own statement here about how the code was developed, including any AI assistance, in line with your university's policy.]

## License

MIT License, see [LICENSE](LICENSE).

## Contact

[GitHub](https://github.com/soorajsrajan97)
