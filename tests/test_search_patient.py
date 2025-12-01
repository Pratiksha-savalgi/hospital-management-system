import unittest
import pymysql

class TestSearchPatient(unittest.TestCase):

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
            "INSERT INTO patients VALUES ('8888888888','SEARCH TEST','1999-05-05','ASTHMA','PARACETAMOL')"
        )
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_search_patient(self):
        """TDD: search patient by mobile"""
        self.cursor.execute("SELECT * FROM patients WHERE MOBILE='8888888888'")
        result = self.cursor.fetchone()
        self.assertEqual(result[1], "SEARCH TEST")
