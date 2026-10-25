import pytest
from sqlalchemy import create_engine, text

db_connection_string = (
    "postgresql://postgres:Enjoyenglish5350%@localhost:5432/QA"
)

engine = create_engine(db_connection_string)


@pytest.fixture
def db():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture
def add_new_student(db):
    insert_sql = text(
        'INSERT INTO student("user_id") VALUES (:new_user_id) '
        'RETURNING user_id'
    )

    result = db.execute(insert_sql, {"new_user_id": 12345})

    student_id = result.fetchone()[0]
    db.commit()

    yield student_id

    delete_sql = text(
        'DELETE FROM student WHERE user_id = :user_id'
    )
    db.execute(delete_sql, {"user_id": student_id})

    db.commit()


@pytest.fixture
def update_subject_title(db):
    user_id = "test-student-1"

    insert_sql = text(
        'INSERT INTO student("user_id", level, education_form) '
        'VALUES (:user_id, :level, :education)'
    )

    db.execute(
        insert_sql,
        {
            "user_id": user_id,
            "level": "Beginner",
            "education": "group"
        }
    )
    db.commit()
    try:
        yield user_id

    finally:
        delete_sql = text(
            'DELETE FROM student WHERE user_id = :user_id'
        )
        db.execute(delete_sql, {"user_id": user_id})
        db.commit()
