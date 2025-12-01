import unittest
import pymysql

class TestUpdatePatient(unittest.TestCase):

    def setUp(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='PATIENTS_DB'
        )
        self.cursor = self.conn.cursor()

        self.cursor.execute("DELETE FROM patients;")
        self.cursor.execute(
            "INSERT INTO patients VALUES ('7777777777','OLD NAME','1980-10-10','BP','XYZ')"
        )
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_update_patient(self):
        """TDD: update name"""
        self.cursor.execute(
            "UPDATE patients SET NAME='NEW NAME' WHERE MOBILE='7777777777'"
        )
        self.conn.commit()

        self.cursor.execute("SELECT NAME FROM patients WHERE MOBILE='7777777777'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], "NEW NAME")
