# population-estimation-
this program takes two number of population from before and estimates a number for future using the differantial appoach that the function of population number regarding to time is f(t)= f(0)*e^(k*t)
basically i wanted to examine the validity of an approach to a population growth estimation method which i read in the Calculus: Early Transcendentals 8th
by James Stewart. The approach is that the only solutions of the differential equation dy/dt = ky are the exponential functions f(t)= f(0)*e^(k*t) which can be used to measure the population growth according to the book and to examine the validity i take the human population number data from vikipedia the link below (https://tr.wikipedia.org/wiki/Ge%C3%A7mi%C5%9F_n%C3%BCfuslar%C4%B1na_g%C3%B6re_%C3%BClkeler_listesi_(Birle%C5%9Fmi%C5%9F_Milletler) and i code a program that calculates the future number of population accordingly the given two numbers of population
the function pop_estimation(start,second_number,time_difference,estimation) takes four values the first start means that the first given population number and the second_number means second number of population time_difference means that the time difference between two given valus' years; so far given three numbers are used to form the function f(t) which estimates population numbers regarding to time the fourth value estimation makes the function estimate the number of population after the given number years.
consequently the miscalculation percentage is averagely %8.01 according to the number of populations for 5 year periods from 1950 to 2010.
