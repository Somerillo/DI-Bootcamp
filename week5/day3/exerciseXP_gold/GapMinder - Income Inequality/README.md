# Project: Investigate a Dataset - Income Inequality using Gapminder

## Introduction

This analysis focuses on income inequailty as measured by the Gini Index* and its association with economic metrics such as GDP per capita, investments as a % of GDP, and tax revenue as a % of GDP. One polical metric, EIU democracy index, is also included.

This investigation can be considered a starting point for complex questions such as:

1. Is a higher tax revenue as a % of GDP associated with less income inequality?
2. Is a higher EIU democracy index associated with less income inequality?
3. Is higher GDP per capita associated with less income inequality?
4. Is higher investments as a % of GDP associated with less income inequality?

This analysis uses the gapminder dataset from the Gapminder Foundation.  The Gapminder Foundation is a non-profit venture registered in Stockholm, Sweden, that promotes sustainable global development and achievement of the United Nations Millennium Development Goals by increased use and understanding of statistics and other information about social, economic and environmental development at local, national and global levels.

*The [Gini Index](https://en.wikipedia.org/wiki/Gini_coefficient) is a measure of statistical dispersion intended to represent the income or wealth distribution of a nation's residents, and is the most commonly used measurement of inequality. It was developed by the Italian statistician and sociologist Corrado Gini and published in his 1912 paper Variability and Mutability. 

## General Properties

The dataset contains data from the following GapMinder datasets:

###  EIU Democracy Index:

"This democracy index is using the data from the Economist Inteligence Unit to express the quality of democracies as a number between 0 and 100. It's based on 60 different aspects of societies that are relevant to democracy universal suffrage for all adults, voter participation, perception of human rights protection and freedom to form organizations and parties.
The democracy index is calculated from the 60 indicators, divided into five ""sub indexes"", which are:

1. Electoral pluralism index;
2. Government index;
3. Political participation indexm;
4. Political culture index;
5. Civil liberty index.

The sub-indexes are based on the sum of scores on roughly 12 indicators per sub-index, converted into a score between 0 and 100.
(The Economist publishes the index with a scale from 0 to 10, but Gapminder has converted it to 0 to 100 to make it easier to communicate as a percentage.)"
https://docs.google.com/spreadsheets/d/1d0noZrwAWxNBTDSfDgG06_aLGWUz4R6fgDhRaUZbDzE/edit#gid=935776888


### Income: GDP per capita, constant PPP dollars

GDP per capita measures the value of everything produced in a country during a year, divided by the number of people. The unit is in international dollars, fixed 2011 prices. The data is adjusted for inflation and differences in the cost of living between countries, so-called PPP dollars. The end of the time series, between 1990 and 2016, uses the latest GDP per capita data from the World Bank, from their World Development Indicators. To go back in time before the World Bank series starts in 1990, we have used several sources, such as Angus Maddison. 
https://www.gapminder.org/data/documentation/gd001/


### Investments (% of GDP)
Capital formation is a term used to describe the net capital accumulation during an accounting period for a particular country. The term refers to additions of capital goods, such as equipment, tools, transportation assets, and electricity. Countries need capital goods to replace the older ones that are used to produce goods and services. If a country cannot replace capital goods as they reach the end of their useful lives, production declines. Generally, the higher the capital formation of an economy, the faster an economy can grow its aggregate income.


### Tax revenue (% of GDP)
refers to compulsory transfers to the central governement for public purposes.  Does not include social security.
https://data.worldbank.org/indicator/GC.TAX.TOTL.GD.ZS
