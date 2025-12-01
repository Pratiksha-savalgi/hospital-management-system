import unittest
import sqlite3

class TestDeleteAppointment(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("Apointment.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM APPOINTMENT_MANAGEMENT;")
        self.cursor.execute(
            "INSERT INTO APPOINTMENT_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)",
            ("TEMP USER", "email", "12345", "Female", "2024-02-01", "11:00 AM")
        )
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_delete_appointment(self):
        """TDD: delete an appointment"""
        self.cursor.execute(
            "DELETE FROM APPOINTMENT_MANAGEMENT WHERE NAME='TEMP USER'"
        )
        self.conn.commit()

        self.cursor.execute("SELECT * FROM APPOINTMENT_MANAGEMENT WHERE NAME='TEMP USER'")
        result = self.cursor.fetchone()

        self.assertIsNone(result)
