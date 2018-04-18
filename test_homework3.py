import unittest
import homework3
import pandas as pd


# Define a class in which the tests will run
class Homework3Test(unittest.TestCase):

    def test_smoke(self):
        df = homework3.create_dataframe("class.db")
        self.assertTrue(df.shape[0] > 10)

    def testColumnNamesAndOrder(self):
        df = homework3.create_dataframe("class.db")
        self.assertTrue((df.columns[0] == 'video_id') & (df.columns[1] == 'category_id') &  (df.columns[2] == 'language') & (df.shape[1] == 3))


    def testPossibleKey(self):
        df = homework3.create_dataframe("class.db")
        nodupe_df = df.iloc[:, [0, 2]].drop_duplicates()
        self.assertTrue(nodupe_df.shape[0] == df.shape[0])

    def testBadPathException(self):
        self.assertRaises(ValueError, homework3.create_dataframe,"bad_path_class.db")


if __name__ == '__main__':
    unittest.main()