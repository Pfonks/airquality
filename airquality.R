library(RSQLite)

conn <- dbConnect(RSQLite::SQLite(), "airquality.db")

air <- dbGetQuery(conn, "SELECT date, co2 FROM airquality")

medians <- aggregate(air$co2, by=list(as.Date(air$date)), median) 
colnames(medians) <- c('date', 'co2')

means <- aggregate(air$co2, by=list(as.Date(air$date)), mean) 
colnames(means) <- c('date', 'co2')

max <- aggregate(air$co2, by=list(as.Date(air$date)), max) 
colnames(max) <- c('date', 'co2')

min <- aggregate(air$co2, by=list(as.Date(air$date)), min) 
colnames(min) <- c('date', 'co2')

plot(type='s', means$date , means$co2, xlab="Date", ylab="CO2 in ppm", ylim=c(400, 2550), col='darkgreen')
lines(type='s', max$date, max$co2, col='darkred')
lines(type='s', min$date, min$co2, col='darkblue')