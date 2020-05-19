$csv = Import-Csv -Delimiter "`t" -Path U:\Downloads\Active+Listings+Report+02-22-2020.txt

$xml = Export-Clixml -Path xmlinventory3.xml -InputObject $csv
