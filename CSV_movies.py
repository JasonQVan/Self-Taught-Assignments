import csv
with open("C:\\Users\\Jason\\Desktop\\csv_movies.csv","w") as f:
  write = csv.writer(f, delimiter= ",")
  write.writerow["Top Gun", "Risky Business", "Minority Report"]
  write.writerow["Titanic", "The Revenant", "Inception"]
  write.writerow["Training Day", "Man on Fire", "Flight"]

