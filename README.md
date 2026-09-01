# ML for Single-Cell and Spatial Genomics (Fall 2026)

**Instructor:** Uthsav Chitra ([uthsav@jhu.edu](mailto:uthsav@jhu.edu))  
**TA:** Sayuni (Sai) Dharmasena ([sdharma5@jhu.edu](mailto:sdharma5@jhu.edu))  
**Class Hours:** TTh 4:30 PM – 5:45 PM | Homewood Campus, Gilman 55  
**Office Hours:** TBD  
**Discussion Board:** TBD  
**Gradescope:** TBD

---

## Course Overview

Recent experimental advances enable the measurement of DNA, RNA and other diverse molecular modalities inside individual cells at an unprecedented scale and resolution. Computational and machine learning (ML) methods are essential for analyzing and interpreting these high-dimensional, single-cell genomics datasets. This course introduces computational/ML frameworks that are often used to analyze modern single-cell and spatial datasets. Topics include but are not limited to: matrix factorization; autoencoders and contrastive learning; graphs and manifold learning; graph neural networks; computational optimal transport (OT); Gromov-Wasserstein and dynamic OT. Expected course background in python programming, probability, linear algebra, and multi-variable calculus. A machine learning/data science course is strongly recommended. No biology background is necessary.

## Course Resources

| Resource | Link |
|---|---|
| Syllabus & Policies | [syllabus.pdf](syllabus.pdf) |
| Assignments | [assignments/](assignments/README.md) |
| Labs | [labs/](labs/) |
| Lectures | [lectures/](lectures/) |

---

## Schedule

**Legend:** $\color{blue}\textbf{\textsf{Homework}}$ &nbsp;&nbsp; $\color{green}\textbf{\textsf{Lab}}$ &nbsp;&nbsp; $\color{goldenrod}\textbf{\textsf{Quiz}}$ &nbsp;&nbsp; $\color{red}\textbf{\textsf{Oral Exam}}$ &nbsp;&nbsp; $\color{purple}\textbf{\textsf{Project}}$

| Date | Class Notes | Topic | Notes |
|------|-------|-------|-------|
| 9/1 | [1](lectures/) | Introduction + single-cell primer | $\color{blue}\textbf{\textsf{HW1 released (\colorbox{yellow}{due 9/17})}}$ |
| 9/3 | [2](lectures/) | Linear algebra/probability refresher; prelab | $\color{purple}\textbf{\textsf{Introduce Final Project}}$ |
| 9/8 | [3](lectures/) | Linear dimensionality reduction 1: PCA | |
| 9/10 | [4](lectures/) | Linear dimensionality reduction 2: NMF | |
| 9/15 | [5](lectures/) | Linear dimensionality reduction 3: probabilistic matrix factorization + in-class lab | $\color{green}\textbf{\textsf{Lab 1 in class (Report \colorbox{yellow}{due 9/21})}}$ |
| 9/17 | [6](lectures/) | Deep learning primer + AE | $\color{goldenrod}\textbf{\textsf{Quiz 1}}$<br>$\color{blue}\textbf{\textsf{HW1 \colorbox{yellow}{due}}}$<br>$\color{blue}\textbf{\textsf{HW2 released (\colorbox{yellow}{due 9/29})}}$ |
| 9/22 | [7](lectures/) | Deep dimensionality reduction: VAE + contrastive learning | |
| 9/24 | [8](lectures/) | Deep dimensionality reduction: FMs + in-class lab | $\color{green}\textbf{\textsf{Lab 2 in class (Report \colorbox{yellow}{due 9/28})}}$ |
| 9/29 | [9](lectures/) | Manifold learning / graphs 1: definitions + ISOMAP | $\color{goldenrod}\textbf{\textsf{Quiz 2}}$<br>$\color{blue}\textbf{\textsf{HW2 \colorbox{yellow}{due}}}$<br>$\color{blue}\textbf{\textsf{HW3 released (\colorbox{yellow}{due 10/13})}}$ |
| 10/1 | [10](lectures/) | Manifold learning / graphs 2: random walks | $\color{purple}\textbf{\textsf{Project proposal \colorbox{yellow}{due}}}$ |
| 10/6 | [11](lectures/) | Manifold learning / graphs 3: t-SNE/UMAP, Markov chains | |
| 10/8 | [12](lectures/) | Manifold learning / graphs 4 (cont.) + in-class lab | $\color{green}\textbf{\textsf{Lab 3 in class (Report \colorbox{yellow}{due 10/12})}}$ |
| 10/13 | [13](lectures/) | Graph clustering | $\color{goldenrod}\textbf{\textsf{Quiz 3}}$<br>$\color{blue}\textbf{\textsf{HW3 \colorbox{yellow}{due}}}$<br>$\color{blue}\textbf{\textsf{HW4 released (\colorbox{yellow}{due 11/3})}}$ |
| 10/15 | [14](lectures/) | Guest lecture: Atul Deshpande (SOM) | |
| 10/20 | [15](lectures/) | Graph clustering (cont.) + GNNs | |
| 10/22 | | **NO CLASS: Fall break** | $\color{red}\textbf{\textsf{Oral Exam 1 (date TBD)}}$ |
| 10/27 | [16](lectures/) | Spatial SVGs + neural fields (e.g. GASTON) + point processes (segmentation) | |
| 10/29 | [17](lectures/) | Spatial (cont.) + in-class lab | $\color{green}\textbf{\textsf{Lab 4 in class (Report \colorbox{yellow}{due 11/2})}}$ |
| 11/3 | [18](lectures/) | Optimal transport I: Monge/Kantorovich/Wasserstein distance | $\color{goldenrod}\textbf{\textsf{Quiz 4}}$<br>$\color{blue}\textbf{\textsf{HW4 \colorbox{yellow}{due}}}$<br>$\color{blue}\textbf{\textsf{HW5 released (\colorbox{yellow}{due 11/17})}}$ |
| 11/5 | [19](lectures/) | Optimal transport II: Sinkhorn | |
| 11/10 | [20](lectures/) | OT 3: Gromov-Wasserstein, Dynamic OT, (semi-)balanced/unbalanced, applications | |
| 11/12 | [21](lectures/) | OT 4 + in-class lab: score/flow/conditional flow matching | $\color{green}\textbf{\textsf{Lab 5 in class (Report \colorbox{yellow}{due 11/16})}}$<br>$\color{purple}\textbf{\textsf{Project Preliminary Report \colorbox{yellow}{due}}}$ |
| 11/17 | [22](lectures/) | Guest lecture: Min-zhi Jiang (Biostats) | $\color{goldenrod}\textbf{\textsf{Quiz 5}}$<br>$\color{blue}\textbf{\textsf{HW5 \colorbox{yellow}{due}}}$ |
| 11/19 | [23](lectures/) | Guest lecture: Vishaka Gopalan (NIH) + Shashwat Kumar (BME) | |
| 11/24 | | **NO CLASS: Thanksgiving break** | |
| 11/26 | | **NO CLASS: Thanksgiving break** | |
| 12/1 | [24](lectures/) | Guest lecture: Yiqun Chen (Biostats/CS) | |
| 12/3 | [25](lectures/) | **Project presentations** | |
| 12/8 | [26](lectures/) | **Project presentations** | |
| 12/10 | [27](lectures/) | **Project presentations** | $\color{purple}\textbf{\textsf{Final report \colorbox{yellow}{due 12/12}}}$<br>$\color{red}\textbf{\textsf{Oral Exam 2 (on final project)}}$ |

---

## Grading

| Component | Weight |
|-----------|--------|
| In-class assessments | 25% (5% each) |
| Oral exam | 25% |
| Homework | 10% |
| Labs | 10% |
| Attendance and participation | 5% |
| Final project + oral exam | 25% |
