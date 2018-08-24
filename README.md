Real Estate Prediction using Street Easy data
-----------------------------------------------
Data updated monthly, found [here](https://streeteasy.com/blog/download-data/). Download csv files - organize by assigning prefixes "RepeatSales" and "Quarterly" - to distinguish between pricing methods as follows:

Steps for downloading data
-----------------------------------------------

* `mkdir data` in project folder. 
* `cd data`.
* Download Files for each borough (Manhattan, Brooklyn, Queens, and NYC)
    * e.g. for Manhattan:
    * `wget -c \ https://s3.amazonaws.com/streeteasy-market-data-api/data_repository/J1_priceIndex_Manhattan.zip -O stEZ_Manhattan.zip`

    * `unzip stEZ_Manhattan.zip`

    * Rename files
    * `rename 's/SEDollarPI_condos_co-ops_homes_Manhattan/Quarterly/' *`. 
    * `rename 's/SEDollarPI_condos_co-ops_homes/RepeatSales/' *`

    * `rm stEZ_Manhatten.zip`