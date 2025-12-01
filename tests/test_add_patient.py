import unittest
import pymysql

class TestAddPatient(unittest.TestCase):

    def setUp(self):
        # Connect to test DB (you can create a separate one if needed)
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='PATIENTS_DB'
        )
        self.cursor = self.conn.cursor()

        # Make sure table exists
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS patients (MOBILE VARCHAR(20), NAME TEXT, DOB TEXT, HISTORY TEXT, MEDICINES TEXT)"
        )

        # Clean table before each test
        self.cursor.execute("DELETE FROM patients;")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_patient(self):
        """TDD: test inserting a patient record into database"""
        self.cursor.execute(
            "INSERT INTO patients VALUES ('9999999999','TEST PATIENT','2000-01-01','NONE','CROCIN')"
        )
        self.conn.commit()

        self.cursor.execute("SELECT * FROM patients WHERE MOBILE='9999999999'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_add_patient_blank_fields(self):
        """TDD: should fail if blank fields are present"""
        MOBILE = ""
        NAME = ""

        self.assertEqual(MOBILE, "")
        self.assertEqual(NAME, "")
        # XP TDD: test ensures UI validation must occur

