# MEV Sandwich Attack Analysis on Ethereum

Analysis of Maximal Extractable Value (MEV) sandwich attacks on Ethereum blockchain using Dune Analytics data.

## Overview

This project analyzes MEV sandwich attacks - a form of frontrunning where bots extract profit by placing transactions before and after victim trades. Analysis covers 246 sandwich attacks over 2 days (April 17-19, 2026) with $5M+ in extracted profit.

## Key Findings

- **Total MEV profit extracted**: $5,008,033
- **Total attacks detected**: 246 sandwich attacks
- **Unique MEV bots**: 15 sophisticated bots
- **MEV extraction rate**: 28.55% of victim trade volume
- **Peak activity**: 8:00 UTC (52 attacks, $2.7M profit)
- **Most targeted pair**: USDT/USDC (93 attacks, $2.7M profit)
- **Top performing bot**: 0x1f2f...f387 extracted $3.4M from 165 attacks

## Data Source

Data retrieved from Dune Analytics using custom SQL query detecting sandwich attack patterns through DEX trades and transaction ordering.

## Tech Stack

- **Python**: Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly
- **Data**: Dune Analytics API (dune-client)
- **Visualization**: Streamlit, Tableau Public
- **Analysis**: Jupyter Notebook

## Project Structure
mev-ethereum-analysis/
├── data/
│   ├── mev_sandwich_data.csv
│   ├── mev_bots_stats.csv
│   ├── mev_hourly_stats.csv
│   └── mev_token_stats.csv
├── notebooks/
│   └── mev_analysis.ipynb
├── streamlit_app/
│   └── app.py
├── visualizations/
└── README.md

## Installation

```bash
pip install dune-client pandas numpy matplotlib seaborn plotly streamlit
```

## Usage

Run Jupyter Analysis:
```bash
jupyter notebook notebooks/mev_analysis.ipynb
```

Run Streamlit App:
```bash
cd streamlit_app
streamlit run app.py
```

## Live Demo

- **Streamlit App**: [Add your deployed Streamlit link]
- **Tableau Dashboard**: [Add your Tableau Public link]

## Results

### MEV Bot Performance
Top bot (0x1f2f...f387) dominated with 67% of total profit, executing 165 attacks with $20,415 average profit per attack.

### Temporal Patterns
MEV activity peaks at 8 AM UTC coinciding with US/European market opening, suggesting bots target high-liquidity periods when victim trades are larger.

### Token Targeting
USDT/USDC stablecoin pair accounts for 38% of all attacks due to high volume and predictable price impact, making sandwich opportunities easier to detect.

## Author

Anna Versens - Web3 Data Analyst

## License

MIT License