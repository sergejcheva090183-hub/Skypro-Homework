from sqlalchemy.sql import text


def test_add_new_student(add_new_student, db):
    query = text(
        "SELECT COUNT(*) FROM student WHERE user_id = :user_id"
    )
    result = db.execute(query, {"user_id": add_new_student})

    row_count = result.scalar_one()
    assert (
        row_count == 1
    ), f"Студент с user_id={add_new_student} не был найден!"


def test_update_subject_title(db):
    new_id, new_title = 9999, "IT"

    db.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": new_id, "title": new_title},
    )
    db.commit()

    result = db.execute(
        text(
            "SELECT subject_title FROM subject WHERE subject_id = :id"
        ),
        {"id": new_id},
    ).fetchone()

    assert result[0] == new_title

    db.execute(
        text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),
        {"id": new_id}
    )
    db.commit()


def test_delete_subject(db):
    subject_id = 88888

    db.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": subject_id, "title": "Temp"},
    )
    db.commit()

    db.execute(
        text(
            "DELETE FROM subject WHERE subject_id = :id"
        ),
        {"id": subject_id},
    )
    db.commit()

    result = db.execute(
        text("SELECT 1 FROM subject WHERE subject_id = :id"),
        {"id": subject_id}
    ).fetchone()

    assert result is None
