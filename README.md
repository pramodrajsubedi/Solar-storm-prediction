# 🌌 SYM-H Forecasting During Extreme Geomagnetic Storms Using ASTGNN-LSTM

This repository contains a complete pipeline to predict the **SYM-H index** (a high-resolution geomagnetic storm indicator) during **extreme events** using a hybrid **ASTGNN-LSTM** deep learning model. The model is trained on space weather data from 1998–2024 filtered to include only events with **SYM-H < -200 nT**.

---

## 📚 Project Summary

- **Objective**: Predict future SYM-H values using a deep learning model trained on solar wind, magnetic field, and geomagnetic activity data.
- **Model**: Combines *Attention-based Spatiotemporal Graph Neural Networks (ASTGNN)* and *Long Short-Term Memory (LSTM)* for capturing both spatial feature interactions and temporal dynamics.
- **Target Variable**: `SYM_H`  
- **Dataset Size**: 201,601 rows × 38 columns  
- **Input Features Used**:  
  - **Solar Wind & Magnetic Parameters**: `Velocity`, `Proton_density`, `Proton_temperature`, `Total_IMF`, `BZ(GSM)`, `Flow_pressure`, `dB`, `Bsr`
  - **Geomagnetic Indices**: `Kp1–Kp8`, `ap1–ap8`, `Ap`, `Ae_index`
  - **Solar Activity**: `SN`, `F10.7obs`, `F10.7adj`

---
> **Source of Raw Data:**
> - [NASA OMNIWeb Database](https://omniweb.gsfc.nasa.gov/)
> - [GFZ Helmholtz Centre for Geosciences](https://kp.gfz.de/)

Data was downloaded from the above sources and processed to extract only the intervals of extreme geomagnetic storms for model training and evaluation.

## 🧠 Model Overview

### ASTGNN-LSTM Architecture:
- **Input Size**: Shape (sequence length × number of features)
- **GNN Layer**: Learns spatial relationships via adjacency matrix between input variables
- **LSTM Layer**: Captures temporal dependencies across sequences
- **Fully Connected Output**: Predicts future SYM-H values

### Training Setup:
- **Loss Function**: `MSELoss`
- **Optimizer**: `Adam`, learning rate = `1e-3`
- **Epochs**: 95
- **Batch Size**: 128
- **Device**: GPU via Google Colab (CUDA)

---

## 📊 Evaluation Results

Evaluated on held-out test data:

| Metric   | Value         |
|----------|---------------|
| MSE      | 2352.99       |
| RMSE     | 48.51 nT      |
| MAE      | 28.80 nT      |
| R² Score | 0.567         |

> Trained only on **intense geomagnetic storms**, these scores reflect strong performance for high-magnitude prediction.

---

## 🛠 Getting Started

### Dependencies
Install with:

```bash
pip install torch pandas numpy scikit-learn matplotlib
