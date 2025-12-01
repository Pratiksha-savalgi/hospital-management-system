import unittest
import pymysql

class TestDeletePatient(unittest.TestCase):

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
            "INSERT INTO patients VALUES ('6666666666','DELETE USER','1995-09-09','FEVER','DOLO')"
        )
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_delete_patient(self):
        """TDD: delete patient"""
        self.cursor.execute("DELETE FROM patients WHERE MOBILE='6666666666'")
        self.conn.commit()

        self.cursor.execute("SELECT * FROM patients WHERE MOBILE='6666666666'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)
