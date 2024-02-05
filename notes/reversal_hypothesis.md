## Hypothesis
A ML classification model can be used to predict a reversal using one or more indicators as features with a > 50% accuracy.

## Parameters
- Futures only (cash settled, easy in, easy out, no T+1)
- Renko based data, initially targeting 30-40 ticks
    - Renko removes time noise
    - Trading the reversal on a Renko allows setting up for an entry with a 2:1 ratio nicely
- The classification ML problem can be used looking for this scenario (reversal=[true|false])
- Initially targeting NQ for volatility and volume
- Looking at narrowing indicators to use as features
- Possibly look at narrowing hours used for training and trading, i.e. no overnight, no trade during news, etc. to eliminate noise
- Indicators which are price based need to be made relative, i.e. a percentage of price
- Ideally focus on subset of indicators which are naturally more forward looking (see notes)

## Tools
-  Ninjatrader
    - C#
    - Fairly large community, futures.io useful
    - Auto executing strategy 
    - Market replay for accurate tick level backtesting
    - Exporter script done
- Rapidminer for auto modeling ideas and quick sandboxing
- Python + tensorflow for production model
- For auto trading, python model accessible via flask restful api called from C# strategy passing data to get predicted reversal, trade reversal detected with a 2:1 entry, exit upon next predicted reversal or stop loss hit or strictly by profit lost, toy with position sizing to maybe have a runner
- Other models which work with sequencing might be explored as well, such as RNN, LSTM, GRU etc.
- Github Co-Pilot and ChatGPT are huge time savers and can fill in the gap and help avoid pitfalls from prior attempts
- Leveraging a GPU is nice, useful space for some python / modeling dev: Google Colab 

## Ninja Indicators
1. **Oscillators:** These indicators fluctuate above and below a line or between set levels to identify overbought or oversold conditions.
   - Aroon Oscillator
   - Balance of Power (BOP)
   - Chande Momentum Oscillator (CMO)
   - Chaikin Oscillator
   - Commodity Channel Index (CCI)
   - Fisher Transform
   - Forecast Oscillator (FOSC)
   - Momentum
   - Money Flow Index (MFI)
   - Percentage Price Oscillator (PPO)
   - Price Oscillator
   - Psychological Line
   - Relative Strength Index (RSI)
   - Relative Vigor Index
   - Relative Volatility Index (RVI)
   - Stochastics
   - Stochastics Fast
   - Stochastics RSI (StochRSI)
   - Ultimate Oscillator
   - Volume Oscillator
   - Williams %R
   - Wiseman Awesom Oscillator

2. **Moving Averages and Related Indicators:** These are trend-following, or lagging, indicators as they are based on past prices.
   - Moving Average - Double Exponential (DEMA)
   - Moving Average - Exponential (EMA)
   - Moving Average - Hull (HMA)
   - Moving Average - Kaufman's Adaptive (KAMA)
   - Moving Average - Mesa Adaptive (MAMA)
   - Moving Average - Simple (SMA)
   - Moving Average - T3 (T3)
   - Moving Average - Triangular (TMA)
   - Moving Average - Triple Exponential (TEMA)
   - Moving Average - Triple Exponential (TRIX)
   - Moving Average - Variable (VMA)
   - Moving Average - Volume Weighted (VWMA)
   - Moving Average - Weighted (WMA)
   - Moving Average - Zero Lag Exponential (ZLEMA)
   - Moving Average Convergence-Divergence (MACD)
   - Moving Average Ribbon
   - Volume Moving Average (VOLMA)

3. **Volume Indicators:** These indicators are used to understand the buying and selling activity.
   - Accumulation/Distribution (ADL)
   - Block Volume
   - BuySell Volume
   - Chaikin Money Flow
   - On Balance Volume (OBV)
   - Volume (VOL)
   - Volume Rate of Change (VROC)
   - Volume Up Down

4. **Volatility Indicators:** These indicators measure the rate of price movement, regardless of direction.
   - Average True Range (ATR)
   - Bollinger Bands
   - Chaikin Volatility
   - Donchian Channel
   - Keltner Channel

5. **Trend Indicators:** These are used to identify the direction of market trends.
   - Aroon
   - Average Directional Index (ADX)
   - Average Directional Movement Rating (ADXR)
   - Darvas
   - Directional Movement (DM)
   - Directional Movement Index (DMI)
   - Parabolic SAR
   - ZigZag

6. **Momentum Indicators:** These indicators are used to identify the speed of price movement or the rate of change in price.
   - Choppiness Index
   - Rate of Change (ROC)
   - True Strength Index (TSI)

7. **Pivot Point Indicators:** These are used to determine overall market trend over different time frames.
   - Camarilla Pivots
   - Fibonacci Pivots
   - Pivots
   - Woodies Pivots

8. **Other Indicators:** These don't fit neatly into one of the above categories but are unique in their own way.
   - Adaptive Price Zone (APZ)
   - BuySell Pressure
   - CandleStickPattern
   - Correlation
   - Current Day OHL
   - Disparity Index
   - Double Stochastics
   - Dynamic Momentum Index (DMIndex)
   - Ease of Movement
   - Linear Regression
   - Linear Regression Intercept
   - Linear Regression Slope
   - MA Envelopes
   - Maximum (MAX)
   - Minimum (MIN)
   - Net Change Display
   - n Bars Down
   - n Bars Up
   - Order Flow Cumulative Delta
   - Order Flow Volumetric Bars
   - Order Flow VWAP
   - Polarized Fractal Efficiency (PFE)
   - Prior Day OHLC
   - Range
   - Range Indicator (RIND)
   - Regression Channel
   - Relative Spread Strength (RSS)
   - R-squared
   - Standard Deviation (StdDev)
   - Standard Error (StdError)
   - Summation (SUM)
   - Swing
   - Time Series Forecast


## Indicators that are more predictive in nature
1. Linear Regression and Related Indicators:

    - Linear Regression
    - Linear Regression Intercept
    - Linear Regression Slope
    - Time Series Forecast (TSF)

    These indicators are based on statistical techniques that fit a line through data points (in this case, price data) and can be extended to forecast future values.

2. Moving Averages Convergence Divergence (MACD):
    - Moving Average Convergence-Divergence (MACD)

    The MACD can provide signals for potential future trend changes based on the convergence and divergence of moving averages.

3. Parabolic SAR:
    - Parabolic SAR

    This indicator is designed to identify potential reversals in the market price direction.

4. Fisher Transform:
    - Fisher Transform

    The Fisher Transform is used to identify potential price reversals and can be predictive of future price movements.

5. Forecast Oscillator:
    - Forecast Oscillator (FOSC)

    This oscillator compares the actual price to the Time Series Forecast (TSF) line, which is a linear regression-based prediction of future prices.

6. Relative Strength Index (RSI):
    - Relative Strength Index (RSI)

    While primarily a momentum oscillator, the RSI can also be used to predict potential reversals when it reaches extreme overbought or oversold levels.

7. Volume Indicators:
    - On Balance Volume (OBV)

    OBV uses volume flow to predict changes in stock price.

8. Directional Movement Indicators:
    - Average Directional Index (ADX)
    - Directional Movement Index (DMI)

    These indicators can help predict the strength of a trend.
