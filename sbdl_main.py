import sys

from lib import Utils
from lib.logger import Log4j

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: sbdl {local, qa, prod} {load_date} : Arguments are missing")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = Utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    accounts = Utils.load_df(spark, "csv","C:\\Users\\ni505\Downloads\SBDL - Starter\\test_data\\accounts\\account_samples.csv" )
    accounts.printSchema()

    parties = Utils.load_df(spark, "csv","C:\\Users\\ni505\Downloads\SBDL - Starter\\test_data\\parties\\party_samples.csv" )
    parties.printSchema()

    address = Utils.load_df(spark, "csv","C:\\Users\\ni505\Downloads\SBDL - Starter\\test_data\\party_address\\address_samples.csv")
    address.printSchema()

    account_party = accounts.account_id == parties.account_id
    party_address = parties.party_id == address.party_id

    final = accounts.join(parties, account_party, "inner").join(address, party_address, "inner"). show()

    logger.info("Finished creating Spark Session")
