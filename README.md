📈 Linear Regression from Scratch

The goal of this project was to gain a low-level understanding of how linear regression works without relying on machine learning libraries.

I implemented a simple linear regression algorithm using gradient descent to find the line of best fit. The only external libraries used were for loading and visualizing the dataset.
🔧 How It Works

Gradient descent is a trial-and-error optimization algorithm that adjusts the parameters of the line (slope m and intercept b) to reduce prediction error.

Here's how it works step by step:

    Start with random values for m and b.

    Use them to predict the output (in this case, test scores) for each input (study time).

    Calculate the error between predicted and actual values.

    Adjust m and b based on the error using gradient descent.

    Repeat this process over the dataset multiple times until the error is minimized.

The learning rate controls how much we adjust m and b on each iteration:

    A small learning rate results in slower but more stable convergence.

    A large learning rate speeds things up but can overshoot the best values and become unstable.

✅ Evaluating Accuracy

To evaluate how well our model fits the data, we use the R-squared (R²) score. It tells us how much of the variation in the dependent variable (test scores) can be explained by the independent variable (study time).

An R² value of:

    1.0 = perfect fit

    0.85+ = strong fit

    Below 0.5 = weak or poor fit

📊 Dataset

The dataset consists of two columns:

    Study Time (hours)

    Test Scores

The algorithm tries to predict test scores based on how much time a student studied.
