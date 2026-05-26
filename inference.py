# inference.py — submitted as a Snowflake ML Job

from snowflake.snowpark import Session
from snowflake.ml.registry import Registry

def main():
    session = Session.builder.getOrCreate()

    reg = Registry(session=session, database_name="ML_LAB", schema_name="DATA")
    model = reg.get_model("iris_classifier").version("v1")

    input_df = session.table("ML_LAB.DATA.IRIS").drop("SPECIES")
    predictions = model.run(input_df, function_name="predict")

    predictions.write.save_as_table(
        "ML_LAB.DATA.IRIS_PREDICTIONS",
        mode="overwrite"
    )
    print("ML Job: inference complete.")

if __name__ == "__main__":
    main()