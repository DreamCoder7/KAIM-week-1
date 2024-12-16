# A project to analyze news data and its correlation with stock price movements

This project focuses on analyzing the relationship between news headlines and stock price movements using sentiment analysis and statistical methods. The project consists of three tasks:

1. **Task 1: Publisher Analysis**
2. **Task 2: Quantitative Analysis using PyNance and TaLib**
3. **Task 3: Correlation Between News and Stock Movement**

---

## **Project Structure**

The project structure is organized into the following directories:

---

## **Task 1: Publisher Analysis**

**Goal:** Identify which publishers contribute most to the news feed, analyze the type of news they report, and extract the domains from email addresses used as publisher names.

### **Steps**

1. **Load Data:**

   - Load news data and stock price data.
   - Ensure that both datasets are pre-processed and have the required columns: 'Date' and 'Publisher' for the news, and 'Date' and 'Close' for the stock prices.

2. **Publisher Count:**

   - Count the number of articles published by each publisher.

3. **Publisher News Type:**

   - Analyze the type of news reported by each publisher by aggregating by categories, such as 'Political', 'Sports', etc.

4. **Email Domain Extraction:**

   - Extract email domains from publisher names if applicable to check for the organization frequency.

5. **Visualization:**
   - Visualize the number of articles per publisher using a bar plot.
   - Visualize the type of news reported by each publisher.

**Libraries Used:**

- `pandas` for data manipulation.
- `seaborn` for data visualization.
- `nltk`, `TextBlob` for sentiment analysis.

---

## **Task 2: Quantitative Analysis using PyNance and TaLib**

**Goal:** Analyze stock data with technical indicators like Moving Averages, RSI, and MACD to evaluate stock performance.

### **Steps**

1. **Data Loading and Preparation:**
   - Load stock price data, ensuring the necessary columns (`Open`, `High`, `Low`, `Close`, `Volume`) are present.
2. **Calculate Technical Indicators:**

   - **Moving Averages (SMA, EMA):** Calculate simple and exponential moving averages.
   - **RSI (Relative Strength Index):** Calculate the RSI to identify overbought or oversold conditions.
   - **MACD (Moving Average Convergence Divergence):** Calculate the MACD and signal line for identifying trends and momentum.

3. **Visualization:**
   - Visualize stock data along with the calculated technical indicators.

**Libraries Used:**

- `pandas` for data manipulation.
- `TA-Lib` for calculating technical indicators.
- `PyNance` for financial metrics.
- `matplotlib`, `seaborn` for visualization.

---

## **Task 3: Correlation Between News and Stock Movement**

**Goal:** Explore the correlation between sentiment in news articles and stock price movements by calculating daily stock returns and performing sentiment analysis.

### **Steps**

1. **Data Preparation:**
   - Align the news and stock data by their respective dates, ensuring that each news headline corresponds to a trading day.
2. **Sentiment Analysis:**

   - Perform sentiment analysis on news headlines using `TextBlob` or other sentiment analysis libraries to generate sentiment scores (e.g., positive, negative, neutral).

3. **Stock Returns:**

   - Calculate daily stock returns based on the percentage change in daily closing prices.

4. **Correlation Analysis:**

   - Aggregate sentiment scores by day, then calculate the Pearson correlation coefficient between the average sentiment of news articles and stock returns.

5. **Visualization:**
   - Visualize the sentiment scores and stock price movement to better understand the correlation.

**Libraries Used:**

- `pandas` for data manipulation.
- `TextBlob` or `nltk` for sentiment analysis.
- `matplotlib`, `seaborn` for visualization.

---

## **Requirements**

Ensure that the following Python packages are installed:

- `pandas`
- `matplotlib`
- `seaborn`
- `TA-Lib`
- `PyNance`
- `TextBlob`
- `nltk`

Install them using:

```bash
pip install -r requirements.txt
```
