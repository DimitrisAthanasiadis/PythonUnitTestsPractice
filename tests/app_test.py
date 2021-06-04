import os
import json
from werkzeug import test
from app import app
import unittest
import tempfile
from bs4 import BeautifulSoup


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # self.test_db_file = tempfile.mkstemp()[1]
        # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self.test_db_file}"
        app.config["TESTING"] = True
        self.app = app.test_client()
        
    # def tearDown(self):
    #     os.remove(self.test_db_file)
    
    def test_index_get(self):
        rv = self.app.get("/")
        
        if "text/html" in rv.content_type:
            soup = BeautifulSoup(rv.data.decode('utf-8'), "html.parser")
            meta = soup.find("meta", {"id": "test_meta"}).get("data")
            self.assertTrue(meta == "testt")
        
    def test_index_post(self):
        rv = self.app.post("/", data={
            "text1": "texxtt1",
            "text2": "texxtt2"
        })
                
        if rv.content_type == "application/json":
            data = json.loads(rv.data.decode("utf-8"))
            self.assertTrue("success" in data.keys())
