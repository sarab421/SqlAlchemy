import sqlalchemy as sa

# Update connection string for PostgreSQL
engine = sa.create_engine("postgresql://postgres:plmnko421@localhost:5432/mydatabase")
connection = engine.connect()

metadata = sa.MetaData()

user_table = sa.Table(
    "users",  
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String),
    sa.Column("email", sa.String),
)

def insert_user(username: str, email: str) -> None:
    query = user_table.insert().values(username=username, email=email)
    with engine.begin() as conn:  # Ensures commit after execution
        conn.execute(query)



def select_user(username: str) -> sa.engine.Result:
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    # print("Results of select user are: ",result.fetchone())
    return result.fetchone()


def main() -> None:
    metadata.create_all(engine)
    insert_user("Abdullah", "nawazabdullah1800@gmail.com")
    # print(select_user("Abdullah"))
    connection.close()


if __name__ == "__main__":
    main()
