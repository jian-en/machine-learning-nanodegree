# variability of data

## If the mean, mode, median are the same, what are the differences?

1. Range (max - min)
    * cut off outliers

2. Q1, Q2, Q3: new range = Q3 - Q1

3. Interquartile range = IQR = Q3 - Q1
    * 50% of data will be in IQR

4. Outlier:
    * Q1 - 1.5 * IQR
    * Q3 + 1.5 * IQR
    * Boxplots

5. SS - Sum of Squared; Variance; -> Standard deviation
    * sigma
    * Why?
        - normal distribution: 68% -> +/- sigma, 95% -> +/- 2sigma, 99% -> +/- 3sigma
        - bessel's correction: n - 1 | sample standard deviation | 采样过于集中
