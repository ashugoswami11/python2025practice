from database import connect_db

# create operation
def add_student(name, age, course):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO students (name, age, course) Values (?, ?, ?)",
         (name, age, course)
    )
    
    conn.commit()
    conn.close()
  
# read operation
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    
    conn.close()
    return records

#update operation
def update_student(student_id, name, age, course):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )
    
    conn.commit()
    conn.close()
    
# delete operation
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    
    conn.commit()
    conn.close()
    
    
        