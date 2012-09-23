#read a file, pick a column, partition the frequencies, plot a barplot
# calculate & print basic statistics: mean, variance, median
plot.data <- function( file, label ){

	file.data <-read.csv( file , head=FALSE, sep='\t' );	
	data<-file.data$V6; # num of twits, in this data frame
	avg<-mean(data);
	var<-sd(data);
	med<-median(data);
	
	cat( sprintf( "mean twits for %s is %f, variance is %f, median:%i \n",  label, avg , var, med ));

	data.len<-length(data);
	
	interval0 = length( which( data == 0 ) );
	interval1 = length( which( data >0 & data<=5 ) );
	interval2 = length( which( data >5 & data<=10 ) );
	interval3 = length( which( data >10 & data<=50 ) );
	interval4 = length( which( data >50 & data<=100 ) );
	interval5 = length( which( data >100 & data<=1000) );
	interval6 = length( which( data >1000) );

	space <- c( interval0, interval1, interval2, interval3, interval4, interval5, interval6 );
	

	labels  = c( '0', '1 to 5', '6 to 10', '11 to 50', '51 to 100', '100 to 1000', '>1000');
	 
	lbl = paste( 'twit distro', label );
	colors <- hcl(seq(0, 360, length = 8))
	lab = sprintf( "twit distribution  %s, number of followers %s", label, data.len );
	barplot( histSpace, col=colors, names.arg=labels, ylab="#num", xlab= lab );
	return (space);

}


