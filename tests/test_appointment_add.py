import unittest
import sqlite3

class TestAddAppointment(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("Apointment.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM APPOINTMENT_MANAGEMENT;")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_appointment(self):
        """TDD: Insert an appointment"""
        self.cursor.execute(
            "INSERT INTO APPOINTMENT_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)",
            ("PATIENT", "doctor@gmail.com", "99999", "Male", "2024-01-01", "10:00 AM")
        )
        self.conn.commit()

        self.cursor.execute("SELECT * FROM APPOINTMENT_MANAGEMENT WHERE NAME='PATIENT'")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
