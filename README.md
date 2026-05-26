# Python-Code-Automation-In-Snowflake

This project demonstrates different approaches to automate Python inference code in Snowflake, using a simple Iris classification model as an example.

## Overview

The workflow has two phases:
1. **Training** — Train a RandomForest model on the Iris dataset and register it in Snowflake's Model Registry.
2. **Inference Automation** — Schedule the inference code to run automatically using one of three methods.

## Files

| File | Description |
|------|-------------|
| `train.ipynb` | Creates the `ML_LAB.DATA.IRIS` table, loads data, trains a RandomForestClassifier, and pushes it to the Snowflake Model Registry as `iris_classifier/v1`. |
| `inference.ipynb` | Standalone inference notebook — loads the registered model, scores `ML_LAB.DATA.IRIS`, and writes predictions to `ML_LAB.DATA.IRIS_PREDICTIONS`. |
| `inference.py` | Same inference logic as a standalone Python script, used by ML Jobs. |
| `Stored_Procedure.ipynb` | **Automation Path 1** — Wraps inference in a Python Stored Procedure (`ML_LAB.DATA.sproc_inference`) and schedules it with a Snowflake Task (daily at 7 AM UTC). |
| `ML_jobs.ipynb` | **Automation Path 2** — Submits inference as a Snowflake ML Job (via `submit_directory` or `submit_file`) wrapped in a Stored Procedure and scheduled with a Task. |
| `automation.ipynb` | **Automation Path 3** — Schedules the inference notebook directly using `EXECUTE NOTEBOOK` in a Snowflake Task (Python and SQL examples). |

## Automation Methods Compared

| Method | Runs On | Best For |
|--------|---------|----------|
| Stored Procedure + Task | Warehouse | Simple, lightweight inference |
| ML Job + Task | Compute Pool (container) | Heavy workloads, GPU, custom packages |
| EXECUTE NOTEBOOK + Task | Warehouse | When inference lives in a notebook |

## Prerequisites

- A Snowflake account with access to Model Registry and ML Jobs
- Packages: `snowflake-ml-python`, `snowflake-snowpark-python`, `scikit-learn`

## Getting Started

1. Run `train.ipynb` to create the database, load data, train the model, and register it.
2. Pick an automation path and run the corresponding notebook to set up scheduled inference.