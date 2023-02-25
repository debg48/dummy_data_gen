import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

print("*"*50)
print("\tWelcome to Dummy Data Generator!")
print("*"*50)

fake = Faker()
fake_data = defaultdict(list)

engine_params = ""
db_client =  input("Enter database client!\n")
if db_client != "mysql":
    print("Only mysql supported in this script for now other databases will be added soon! Please enter mysql ofr data base !")
else:
    db_user=input("Enter username for database\n")
    db_passwd=input("Enter password for database\n")
    route=input("Enter route (default=localhost)\n")
    if route.strip()=='':
        route = 'localhost'
    db_name=input("Enter the name db\n")
    data_size=input("Enter the number of row of the table you want to create \n")
    if not data_size.isnumeric():
        print("Invalid Number entered !")
    else :     
        engine_params=engine_params+db_client+"://"+db_user+":"+db_passwd+"@"+route+"/"+db_name
        for _ in range(data_size):
            # READ DOCUMENTATION TO CUSTOMIZE FIELDS OF THE TABLE ACCORDINGLY
            # THIS IS WHERE THE CUSTOMIATION NEEDS TO BE DONE
            fake_data["first_name"].append( fake.first_name() )
            fake_data["last_name"].append( fake.last_name() )
            fake_data["occupation"].append( fake.job() )
            fake_data["dob"].append( fake.date_of_birth() )
            fake_data["country"].append( fake.country() )
            fake_data["salary"].append(fake.random_int())

        # CREATING A PANDAS DATAFRAME TO STORE THE DATA
        df_fake_data = pd.DataFrame(fake_data)

        #CONNECTING TO THE SQL SERVER AND CREATING THE TABLE AND FILLING IT WITH DUMMY DATA
        engine = create_engine(engine_params, echo=False)
        try:
            df_fake_data.to_sql('employee', con=engine,index=False)
        except Exception as e:
            print(e)
