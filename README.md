# ML for Single-Cell and Spatial Genomics (Fall 2026)

**Instructor:** Uthsav Chitra ([uthsav@jhu.edu](mailto:uthsav@jhu.edu))  
**TA:** Sayuni (Sai) Dharmasena ([sdharma5@jhu.edu](mailto:sdharma5@jhu.edu))  
**Class Hours:** TTh 4:30 PM–5:45 PM | Homewood Campus, Gilman 55  
**Office Hours:**  
&bull; T (Sai): After class–6:45 PM in Malone 216 or on [Zoom](https://JHUBlueJays.zoom.us/j/94258459480?pwd=MaFvyXrLPvLXNI9T6ynaOep6Qn3UQk.1)  
&bull; Th (Uthsav): After class in Malone 319  
[Canvas](https://jhu.instructure.com/courses/128341)

---
## Course Overview

Recent experimental advances enable the measurement of DNA, RNA and other diverse molecular modalities inside individual cells at an unprecedented scale and resolution. Computational and machine learning (ML) methods are essential for analyzing and interpreting these high-dimensional, single-cell genomics datasets. This course introduces computational/ML frameworks that are often used to analyze modern single-cell and spatial datasets. Topics include but are not limited to: matrix factorization; autoencoders and contrastive learning; graphs and manifold learning; graph neural networks; computational optimal transport (OT); Gromov-Wasserstein and dynamic OT. Expected course background in python programming, probability, linear algebra, and multi-variable calculus. A machine learning/data science course is strongly recommended. No biology background is necessary.

## Course Resources

- [Syllabus & Policies](syllabus.pdf)
- [Assignments](assignments/)
- [Labs](labs/)
- [Lectures](lectures/)

---

## Schedule

![Course schedule](assets/course-schedule.svg)

<details>
<summary>Plain-text schedule</summary>

| Date | Class | Topic | Notes |
|------|-------|-------|-------|
| 9/1 | 1 | Introduction + single-cell primer | **HW1 released (due 9/17)** |
| 9/3 | 2 | Linear algebra/probability refresher; prelab | **Introduce Final Project** |
| 9/8 | 3 | Linear dimensionality reduction 1: PCA |  |
| 9/10 | 4 | Linear dimensionality reduction 2: NMF |  |
| 9/15 | 5 | Linear dimensionality reduction 3: probabilistic matrix factorization + in-class lab | **Lab 1 in class (Report due 9/21)** |
| 9/17 | 6 | Deep learning primer + AE | **Quiz 1**<br>**HW1 due**<br>**HW2 released (due 9/29)** |
| 9/22 | 7 | Deep dimensionality reduction: VAE + contrastive learning |  |
| 9/24 | 8 | Deep dimensionality reduction: FMs + in-class lab | **Lab 2 in class (Report due 9/28)** |
| 9/29 | 9 | Manifold learning / graphs 1: definitions + ISOMAP | **Quiz 2**<br>**HW2 due**<br>**HW3 released (due 10/13)** |
| 10/1 | 10 | Manifold learning / graphs 2: random walks | **Project proposal due** |
| 10/6 | 11 | Manifold learning / graphs 3: t-SNE/UMAP, Markov chains |  |
| 10/8 | 12 | Manifold learning / graphs 4 (cont.) + in-class lab | **Lab 3 in class (Report due 10/12)** |
| 10/13 | 13 | Graph clustering | **Quiz 3**<br>**HW3 due**<br>**HW4 released (due 11/3)** |
| 10/15 | 14 | Guest lecture: Atul Deshpande (SOM) |  |
| 10/20 | 15 | Graph clustering (cont.) + GNNs |  |
| 10/22 |  | **NO CLASS: Fall break** | **Oral Exam 1 (date TBD)** |
| 10/27 | 16 | Spatial SVGs + neural fields (e.g. GASTON) + point processes (segmentation) |  |
| 10/29 | 17 | Spatial (cont.) + in-class lab | **Lab 4 in class (Report due 11/2)** |
| 11/3 | 18 | Optimal transport I: Monge/Kantorovich/Wasserstein distance | **Quiz 4**<br>**HW4 due**<br>**HW5 released (due 11/17)** |
| 11/5 | 19 | Optimal transport II: Sinkhorn |  |
| 11/10 | 20 | OT 3: Gromov-Wasserstein, Dynamic OT, (semi-)balanced/unbalanced, applications |  |
| 11/12 | 21 | OT 4 + in-class lab: score/flow/conditional flow matching | **Lab 5 in class (Report due 11/16)**<br>**Project Preliminary Report due** |
| 11/17 | 22 | Guest lecture: Min-zhi Jiang (Biostats) | **Quiz 5**<br>**HW5 due** |
| 11/19 | 23 | Guest lecture: Vishaka Gopalan (NIH) + Shashwat Kumar (BME) |  |
| 11/24 |  | **NO CLASS: Thanksgiving break** |  |
| 11/26 |  | **NO CLASS: Thanksgiving break** |  |
| 12/1 | 24 | Guest lecture: Yiqun Chen (Biostats/CS) |  |
| 12/3 | 25 | **Project presentations** |  |
| 12/8 | 26 | **Project presentations** |  |
| 12/10 | 27 | **Project presentations** | **Final report due 12/12**<br>**Oral Exam 2 (on final project)** |

</details>

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
