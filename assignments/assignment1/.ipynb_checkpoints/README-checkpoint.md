<p align="center">
  <img src="../../assets/banner.svg" alt="ML for Single-Cell and Spatial Genomics — Fall 2026" width="100%"/>
</p>

# Assignment 1: scRNA-seq Preprocessing and Quality Control

**Released:** September 9, 2026  
**Due:** September 23, 2026 at 11:59 PM  
**Submission:** GradeScope

---

## Overview

In this assignment you will work with a real scRNA-seq dataset and implement a complete preprocessing pipeline, from raw count matrices through quality control, normalization, and feature selection.

## Learning Objectives

- Load and inspect raw scRNA-seq count matrices (AnnData format)
- Apply quality control filters (mitochondrial fraction, cell/gene thresholds)
- Normalize and log-transform expression data
- Identify highly variable genes
- Understand how preprocessing choices affect downstream analysis

## Data

TBD — dataset and download instructions will be provided with the assignment notebook.

## Tasks

> Full instructions are in `assignment1.ipynb`

1. **Data Loading** — Load the provided count matrix into an AnnData object using Scanpy.
2. **Quality Control** — Compute and visualize QC metrics; filter low-quality cells and genes.
3. **Normalization** — Normalize to total counts per cell; apply log1p transformation.
4. **Feature Selection** — Identify highly variable genes using Scanpy's `highly_variable_genes`.
5. **Written Questions** — Answer conceptual questions about preprocessing choices.

## Submission

Submit to GradeScope:
- `assignment1.ipynb` (with all cells run)
- `assignment1.pdf` or `assignment1.html` (exported notebook)

## Grading

| Task | Points |
|------|--------|
| Data Loading | 10 |
| Quality Control | 25 |
| Normalization | 20 |
| Feature Selection | 20 |
| Written Questions | 25 |
| **Total** | **100** |
