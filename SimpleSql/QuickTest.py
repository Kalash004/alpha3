import SimpleSql


class Test2(SimpleSql.Base):
    table_name = "Test2"
    test2_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)


class Person(SimpleSql.Base):
    table_name = "Person"
    person_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    ref_to_test2 = SimpleSql.Param(SimpleSql.Types.INT, references=SimpleSql.Reference(Test2, "test2_Id"))


# SELECT * FROM PERSON WHERE STUFF = X

if __name__ == "__main__":
    config = SimpleSql.Config(username="root", password="Ka32167890", hostname="localhost",
                              port=0,
                              database_name="Testing", character_set="Testing")
    p = Person(person_Id=2, stuff="New text", ref_to_test2=2)
    t = Test2(test2_Id=2, stuff="Heeeeee")
    app = SimpleSql.App(config)
    app.start()
    app.delete_data(p)
